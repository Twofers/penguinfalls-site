"""Render the framework-free portfolio from one app catalog."""
import html
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
APPS = json.loads((ROOT / 'data/apps.json').read_text(encoding='utf-8'))
ASSETS = json.loads((ROOT / 'data/asset-sources.json').read_text())['assets']
DIMENSIONS = {a['file']: (a['width'], a['height']) for a in ASSETS}
ORIGIN = 'https://www.penguinfalls.com'
VERSION = '20260926'
e = html.escape

def image(app, kind='icon', alt='', eager=False, cls=''):
    path = f'/assets/apps/{app["slug"]}-{kind}-{VERSION}.webp'
    w, h = DIMENSIONS[path]
    priority = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{cls}" src="{path}" width="{w}" height="{h}" alt="{e(alt)}" {priority} decoding="async">'

def nav():
    return '''<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header"><div class="container header-inner">
<a class="wordmark" href="/" aria-label="Penguin Falls home"><img src="/brand/penguin-falls-logo-reverse.svg" width="190" height="48" alt="Penguin Falls"></a>
<button class="menu-toggle" type="button" aria-controls="site-menu" aria-expanded="false" hidden><span class="menu-label">Menu</span><span class="menu-icon" aria-hidden="true"></span></button>
<nav class="site-menu" id="site-menu" aria-label="Primary navigation"><a href="/#apps">Apps &amp; Games</a><a href="/#about">About</a><a href="/support">Support</a><a href="/#contact">Contact <span aria-hidden="true">↗</span></a></nav>
</div></header>'''

def footer():
    return '''<footer class="site-footer"><div class="container footer-top"><div><a class="wordmark" href="/" aria-label="Penguin Falls home"><img src="/brand/penguin-falls-logo-reverse.svg" width="190" height="48" alt="Penguin Falls"></a><p>Independent apps and games.<br>Made in Irving, Texas.</p></div><nav aria-label="Footer navigation"><a href="/#apps">Apps &amp; Games</a><a href="/#about">About the studio</a><a href="/support">App support</a><a href="mailto:contact@penguinfalls.com">Contact</a></nav></div><div class="container footer-bottom"><p>© 2026 Penguin Falls LLC</p><p>Twofer, Sightlines, and the Penguin games are products of Penguin Falls LLC.</p><nav aria-label="Website policies"><a href="/privacy">Website privacy</a><a href="/terms">Website terms</a></nav></div></footer>'''

def page(title, description, path, body, app=None, noindex=False):
    social = f'{app["slug"]}-social-{VERSION}.jpg' if app else f'portfolio-social-{VERSION}.jpg'
    structured = {'@context': 'https://schema.org', '@type': 'Organization', '@id': ORIGIN + '/#organization', 'name': 'Penguin Falls LLC', 'url': ORIGIN, 'logo': ORIGIN + '/brand/penguin-falls-symbol.png', 'email': 'contact@penguinfalls.com', 'address': {'@type': 'PostalAddress', 'addressLocality': 'Irving', 'addressRegion': 'Texas', 'addressCountry': 'US'}, 'brand': [{'@type': 'Brand', 'name': a['name'], 'url': ORIGIN + '/' + a['slug']} for a in APPS]}
    if app:
        structured = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': app['fullName'], 'url': ORIGIN + path, 'image': ORIGIN + f'/assets/apps/{app["slug"]}-icon-{VERSION}.webp', 'description': app['summary'], 'applicationCategory': 'GameApplication' if app['kind'] == 'game' else ('LifestyleApplication' if app['slug'] == 'twofer' else 'UtilitiesApplication'), 'operatingSystem': 'iOS, Android' if app.get('google') else 'iOS', 'downloadUrl': app['apple'], 'publisher': {'@type': 'Organization', '@id': ORIGIN + '/#organization', 'name': 'Penguin Falls LLC'}}
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}">
<link rel="canonical" href="{ORIGIN}{path}">{robots}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN}{path}">
<meta property="og:image" content="{ORIGIN}/assets/apps/{social}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{e(app['fullName'] if app else 'Penguin Falls — Useful apps. Playful games.')}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><meta name="twitter:image" content="{ORIGIN}/assets/apps/{social}">
<meta name="theme-color" content="#0b2949"><link rel="icon" href="/brand/favicon.ico" sizes="any"><link rel="icon" href="/brand/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/brand/apple-touch-icon.png">
<link rel="stylesheet" href="/portfolio.css?v={VERSION}"><script src="/portfolio.js?v={VERSION}" defer></script>
<script type="application/ld+json">{json.dumps(structured, ensure_ascii=False).replace('<', '&lt;')}</script>
</head><body id="top">{nav()}<main id="main-content" tabindex="-1">{body}</main>{footer()}</body></html>'''

def badges(app):
    result = f'<a class="store-badge" href="{e(app["apple"])}" aria-label="Download {e(app["name"])} on the App Store"><img src="/assets/badge-appstore-en.svg" width="120" height="40" alt="Download on the App Store" loading="lazy"></a>'
    if app.get('google'):
        result += f'<a class="store-badge google-badge" href="{e(app["google"])}" aria-label="Get {e(app["name"])} on Google Play"><img src="/assets/badge-googleplay-en.png" width="135" height="40" alt="Get it on Google Play" loading="lazy"></a>'
    return '<div class="store-links">' + result + '</div>'

def resources(app):
    return f'<nav class="resource-links" aria-label="{e(app["name"])} resources"><a href="{e(app["support"])}">Support</a><a href="{e(app["privacy"])}">Privacy</a><a href="{e(app["terms"])}">{e(app["termsLabel"])}</a></nav>'

def app_card(a):
    return f'''<article class="featured-card {a['slug']}" id="{a['slug']}"><div class="featured-copy">{image(a, alt='', cls='app-icon')}<p class="eyebrow">{e(a['category'])}</p><h3><a href="/{a['slug']}">{e(a['name'])}</a></h3><p>{e(a['summary'])}</p><a class="text-link" href="/{a['slug']}">Explore {e(a['name'])} <span aria-hidden="true">↗</span></a>{badges(a)}<p class="availability">{e(a['platform'])}</p></div><a class="featured-screen" href="/{a['slug']}" aria-label="Explore {e(a['name'])}">{image(a, 'screen-1', a['screenAlts'][0])}</a></article>'''

def game_card(a):
    return f'''<article class="game-card {a['slug']}"><a class="game-art" href="/{a['slug']}" aria-label="Explore {e(a['name'])}">{image(a, 'screen-1', a['screenAlts'][0])}<span class="game-icon">{image(a, alt='')}</span></a><div class="game-copy"><p class="eyebrow">{e(a['category'])}</p><h3><a href="/{a['slug']}">{e(a['name'])}</a></h3><p>{e(a['summary'])}</p><a class="text-link" href="/{a['slug']}">Explore the game <span aria-hidden="true">↗</span></a>{badges(a)}<p class="availability">{e(a['platform'])}{' · Ages 13+' if a['slug'] == 'penguin-crash' else ''}</p></div></article>'''

def home():
    icons = ''.join(f'<a class="hero-app" href="/{a["slug"]}" aria-label="Explore {e(a["name"])}">{image(a, alt="", eager=True)}<span>{e(a["name"])}</span></a>' for a in APPS)
    body = f'''<section class="hero"><div class="container hero-grid"><div class="hero-copy"><p class="eyebrow">Independent studio · Irving, Texas</p><h1>Useful apps.<br><span>Playful games.</span></h1><p>Practical tools and playful games—from discovering local deals and exploring your surroundings to taking a well-earned penguin break.</p><a class="button" href="#apps">Explore our apps <span aria-hidden="true">↗</span></a></div><div class="hero-collection" aria-label="Our six apps"><div class="hero-icons">{icons}</div><p>Six apps. One independent studio.</p></div></div></section>
<section class="apps-section section" id="apps" aria-labelledby="apps-title"><div class="container"><div class="section-heading"><div><p class="eyebrow">A little discovery, every day</p><h2 id="apps-title">Meet your next useful app.</h2></div><p>Made to help you find a good thing<br class="desktop-break"> right around the corner—or farther afield.</p></div><div class="featured-grid">{''.join(app_card(a) for a in APPS if a['kind']=='app')}</div></div></section>
<section class="games-section section" id="games" aria-labelledby="games-title"><div class="container"><div class="section-heading"><div><p class="eyebrow">The Penguin games</p><h2 id="games-title">Make time for a little play.</h2></div><p>A rescue, a perfect glide, a coffee delivery, a daring heist.<br class="desktop-break"> Four ways to take a penguin break.</p></div><div class="games-grid">{''.join(game_card(a) for a in APPS if a['kind']=='game')}</div><p class="games-note">Made by Penguin Falls. Presented by <a href="/twofer">Twofer</a>. Each game stands on its own—exploring Twofer is always optional.</p></div></section>
<span class="anchor-alias" id="company"></span><section class="about-section section" id="about" aria-labelledby="about-title"><div class="container about-grid"><div class="about-mark"><img src="/brand/penguin-falls-symbol-reverse.svg" width="220" height="220" alt="" loading="lazy"><p>Curiosity. Care.<br>A little character.</p></div><div class="about-copy"><p class="eyebrow">About Penguin Falls</p><h2 id="about-title">Small studio.<br>Thoughtful products.</h2><p>Penguin Falls is an independent app studio based in Irving, Texas. We build and operate our own products, bringing the same care to a useful everyday tool and a game that makes you smile.</p><p>Founded by a Coast Guard veteran and SMU Cox MBA graduate, the studio pairs practical problem solving with a willingness to explore. Twofer, Sightlines, and our growing family of penguin games all call Penguin Falls home.</p><a class="text-link light" href="mailto:contact@penguinfalls.com">Say hello <span aria-hidden="true">↗</span></a></div></div></section>
<section class="contact-section section" id="contact" aria-labelledby="contact-title"><div class="container contact-grid"><div><p class="eyebrow">Let's talk</p><h2 id="contact-title">A question, an idea,<br>or a little help?</h2><p>For company and partnership inquiries:</p><a class="contact-email" href="mailto:contact@penguinfalls.com">contact@penguinfalls.com <span aria-hidden="true">↗</span></a></div><div class="help-panel"><span class="help-symbol" aria-hidden="true">↗</span><h3>Here for your app questions.</h3><p>Choose your app to find the right help, privacy information, and contact details.</p><a class="button navy" href="/support">Find app support <span aria-hidden="true">↗</span></a></div></div></section>'''
    return page('Penguin Falls | Useful Apps & Playful Games', 'Discover Twofer, Sightlines, Penguin Bounce, Penguin Slide, Penguin Express, and Penguin Crash. Independent apps and games from Penguin Falls in Irving, Texas.', '/', body)

def product(a):
    gallery = ''.join(f'<figure>{image(a, f"screen-{i+1}", alt)}<figcaption>{e(alt)}</figcaption></figure>' for i, alt in enumerate(a['screenAlts']))
    features = ''.join(f'<div><span class="feature-index">0{i+1}</span><h3>{e(title)}</h3><p>{e(text)}</p></div>' for i, (title, text) in enumerate(a['features']))
    crosslink = '<a class="text-link" href="https://www.twoferapp.com/">Visit Twofer for customers &amp; merchants <span aria-hidden="true">↗</span></a>' if a.get('website') else ''
    related = [b for b in APPS if b['slug'] != a['slug'] and b['kind'] == a['kind']]
    related_links = ''.join(f'<a href="/{b["slug"]}">{image(b, alt="")}<span>{e(b["name"])} <span aria-hidden="true">↗</span></span></a>' for b in related)
    body = f'''<section class="product-hero {a['slug']}"><div class="container"><a class="back-link" href="/#apps">← All apps &amp; games</a><div class="product-grid"><div class="product-copy"><div class="product-identity">{image(a, alt='', eager=True)}<div><p class="eyebrow">{e(a['category'])}</p><p>{e(a['fullName'])}</p></div></div><h1>{e(a['headline'])}</h1><p class="product-intro">{e(a['description'])}</p>{badges(a)}<p class="availability">{e(a['platform'])} · {e(a['pricing'])}</p>{crosslink}</div><div class="product-visual">{image(a, 'screen-1', a['screenAlts'][0], eager=True)}</div></div></div></section>
<section class="section product-features"><div class="container"><h2 class="visually-hidden">What you can do with {e(a['name'])}</h2><div class="feature-grid">{features}</div></div></section>
<section class="section screenshot-section {a['slug']}"><div class="container"><div class="section-heading"><div><p class="eyebrow">Take a closer look</p><h2>Inside {e(a['name'])}.</h2></div><p>Actual screens from the app.</p></div><div class="screenshots {'landscape' if a['slug']=='penguin-crash' else ''}" role="region" aria-label="{e(a['name'])} screenshots" tabindex="0">{gallery}</div></div></section>
<section class="section"><div class="container product-info"><div><h2>{'Free to explore. Plus when you need it.' if a['slug']=='sightlines' else 'Good to know'}</h2><p>{e(a['note'])}</p><p class="ownership">{e(a['name'])} is made and operated by Penguin Falls LLC.</p></div><aside class="product-help"><h3>Need a hand?</h3><p>{e(a['supportSummary'])}</p>{resources(a)}<a class="text-link" href="mailto:{a['email']}?subject={quote(a['name']+' support')}">Email {e(a['name'])} support <span aria-hidden="true">↗</span></a></aside></div></section>
<section class="related-section"><div class="container"><h2>More from Penguin Falls</h2><div class="related-apps">{related_links}</div></div></section>'''
    return page(a['fullName'] + ' | Penguin Falls', a['summary'] + ' Discover screenshots, downloads, and support from Penguin Falls LLC.', '/' + a['slug'], body, a)

def support():
    cards = ''.join(f'''<article class="support-card" id="{a['slug']}"><div class="support-identity">{image(a, alt='')}<div><h2>{e(a['name'])}</h2><a href="/{a['slug']}">About the app <span aria-hidden="true">↗</span></a></div></div><p>{e(a['supportSummary'])}</p>{resources(a)}<a class="text-link" href="mailto:{a['email']}?subject={quote(a['name']+' support')}">Email support <span aria-hidden="true">↗</span></a></article>''' for a in APPS)
    jump = ''.join(f'<a href="#{a["slug"]}">{e(a["name"])}</a>' for a in APPS)
    body = f'''<section class="page-intro"><div class="container"><p class="eyebrow">Penguin Falls support</p><h1>A little help,<br>right this way.</h1><p>Choose your app for help, privacy information, and the right person to contact.</p><nav class="support-jumps" aria-label="Choose an app">{jump}</nav></div></section><section class="section support-section"><div class="container"><div class="support-grid">{cards}</div><div class="support-tip"><h2>Help us help you.</h2><p>When you email, include the app name, your device model, app version, and what happened. Leave out passwords, payment details, and private information.</p><p>For company or partnership inquiries, email <a href="mailto:contact@penguinfalls.com">contact@penguinfalls.com</a>.</p></div></div></section>'''
    return page('App Support | Penguin Falls', 'Find help, privacy policies, terms, and contact details for Twofer, Sightlines, Penguin Bounce, Penguin Slide, Penguin Express, and Penguin Crash.', '/support', body)

def legal(filename, kind):
    source = (ROOT / filename).read_text(encoding='utf-8')
    article = re.search(r'<article\b[^>]*>(.*?)</article>', source, re.S).group(1)
    article = article.replace('Last Updated: June 18, 2026', 'Last Updated: September 26, 2026')
    if kind == 'privacy':
        replacement = '''<section class="legal-section" aria-labelledby="privacy-products"><h2 id="privacy-products">Our Apps and Games</h2><p>This policy covers the Penguin Falls informational website. Twofer, Sightlines, Penguin Bounce, Penguin Slide, Penguin Express, and Penguin Crash have their own product-specific privacy information and support resources.</p><p>Visit our <a href="/support">app support directory</a> to find the privacy policy, terms or iOS license, and support contact for each app.</p></section>'''
        article = re.sub(r'<section[^>]*aria-labelledby="privacy-(?:twofer|products)".*?</section>', replacement, article, flags=re.S)
    else:
        replacement = '''<section class="legal-section" aria-labelledby="terms-products"><h2 id="terms-products">Our Apps and Games</h2><p>Twofer, Sightlines, and the Penguin games are products operated by Penguin Falls LLC. Each product may be governed by separate terms, privacy practices, and support resources. Find the relevant terms or iOS license in our <a href="/support">app support directory</a>.</p></section>'''
        article = re.sub(r'<section[^>]*aria-labelledby="terms-(?:twofer|products)".*?</section>', replacement, article, flags=re.S)
    title = 'Website Privacy Policy' if kind == 'privacy' else 'Website Terms of Use'
    article = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', article, count=1)
    return page(title + ' | Penguin Falls', f'{title} for the Penguin Falls company website, with links to separate app and game policies.', '/' + kind, f'<div class="container legal-main"><a class="back-link" href="/">← Back to Penguin Falls</a><article class="legal-article">{article}</article></div>')

(ROOT / 'index.html').write_text(home(), encoding='utf-8')
for a in APPS:
    (ROOT / (a['slug'] + '.html')).write_text(product(a), encoding='utf-8')
(ROOT / 'support.html').write_text(support(), encoding='utf-8')
for kind in ('privacy', 'terms'):
    (ROOT / (kind + '.html')).write_text(legal(kind + '.html', kind), encoding='utf-8')
not_found = '<section class="page-intro"><div class="container"><p class="eyebrow">404 · Page not found</p><h1>A little off course?</h1><p>Let’s get you back to the apps and games.</p><a class="button navy" href="/">Back to Penguin Falls ↗</a><a class="text-link" href="/support">Find app support ↗</a></div></section>'
(ROOT / '404.html').write_text(page('Page Not Found | Penguin Falls', 'Find Penguin Falls apps, games, and support.', '/404', not_found, noindex=True), encoding='utf-8')
paths = ['/', '/support', '/privacy', '/terms'] + ['/' + a['slug'] for a in APPS] + ['/sightlines/support', '/sightlines/privacy', '/sightlines/terms']
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path in paths:
    date = '2026-09-20' if path.startswith('/sightlines/') else '2026-09-26'
    sitemap += f'  <url><loc>{ORIGIN}{path}</loc><lastmod>{date}</lastmod></url>\n'
(ROOT / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
print('Rendered homepage, six product pages, support directory, website policies, 404, and sitemap.')
