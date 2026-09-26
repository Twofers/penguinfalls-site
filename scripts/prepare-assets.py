"""Import the owner's current public App Store artwork, without altering screens."""
import concurrent.futures
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'data/app-store-snapshot.json').read_text(encoding='utf-8-sig'))['results']
SLUGS = ['twofer', 'sightlines', 'penguin-bounce', 'penguin-slide', 'penguin-express', 'penguin-crash']
SELECT = [[0, 1, 2], [0, 2, 3], [1, 2, 3], [1, 2, 3], [1, 0, 3], [2, 0, 1]]
OUT = ROOT / 'assets' / 'apps'
OUT.mkdir(parents=True, exist_ok=True)

def fetch_asset(job):
    name, url, max_size = job
    picture = Image.open(ROOT / '.asset-cache' / (name + '.jpg')).convert('RGB')
    picture.thumbnail(max_size, Image.Resampling.LANCZOS)
    picture.save(OUT / name, 'WEBP', quality=86, method=6)
    return {'file': '/assets/apps/' + name, 'source': url, 'width': picture.width, 'height': picture.height}

jobs = []
for app, slug, indexes in zip(CATALOG, SLUGS, SELECT):
    assert app['sellerName'] == 'Penguin Falls LLC'
    jobs.append((slug + '-icon-20260926.webp', app['artworkUrl512'], (256, 256)))
    for i, index in enumerate(indexes, 1):
        url = app['screenshotUrls'][index].replace('/320x480bb.jpg', '/640x1388bb.jpg')
        jobs.append((f'{slug}-screen-{i}-20260926.webp', url, (880, 1200)))

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    assets = list(pool.map(fetch_asset, jobs))
(ROOT / 'data' / 'asset-sources.json').write_text(json.dumps({'verified': '2026-09-26', 'source': 'Penguin Falls LLC public US App Store listings', 'assets': assets}, indent=2) + '\n')

# Social previews use existing icons and typesetting, with no generated product imagery.
serif = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 70)
sans = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 28)
small = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 24)
for slug, app in [(None, None)] + list(zip(SLUGS, CATALOG)):
    canvas = Image.new('RGB', (1200, 630), '#0b2949')
    draw = ImageDraw.Draw(canvas)
    draw.text((70, 48), 'PENGUIN FALLS', font=sans, fill='#9acbfc')
    if slug is None:
        draw.text((70, 162), 'Useful apps.', font=serif, fill='white')
        draw.text((70, 256), 'Playful games.', font=serif, fill='#9acbfc')
        draw.text((73, 398), 'An independent studio in Irving, Texas.', font=small, fill='white')
        for i, item in enumerate(SLUGS):
            icon = Image.open(OUT / (item + '-icon-20260926.webp')).resize((112, 112), Image.Resampling.LANCZOS)
            mask = Image.new('L', icon.size); ImageDraw.Draw(mask).rounded_rectangle((0, 0, 111, 111), radius=23, fill=255)
            canvas.paste(icon, (754 + (i % 3) * 132, 181 + (i // 3) * 142), mask)
        filename = 'portfolio-social-20260926.jpg'
    else:
        title = app['trackName'].split(':')[0]
        subtitle = app['trackName'].split(': ')[1] if ': ' in app['trackName'] else 'Keep the coffee in the cup'
        draw.text((70, 198), title, font=serif, fill='white')
        draw.text((73, 301), subtitle, font=sans, fill='#9acbfc')
        draw.text((73, 411), 'Discover the app at penguinfalls.com', font=small, fill='white')
        icon = Image.open(OUT / (slug + '-icon-20260926.webp')).resize((256, 256), Image.Resampling.LANCZOS)
        mask = Image.new('L', icon.size); ImageDraw.Draw(mask).rounded_rectangle((0, 0, 255, 255), radius=55, fill=255)
        canvas.paste(icon, (856, 183), mask)
        filename = slug + '-social-20260926.jpg'
    draw.line((70, 548, 1130, 548), fill='#385673', width=1)
    draw.text((73, 569), 'penguinfalls.com', font=small, fill='#9acbfc')
    canvas.save(OUT / filename, quality=90, optimize=True)
print(f'Prepared {len(assets)} verified app assets and 7 social images.')
