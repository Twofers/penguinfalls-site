
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.refs=[]; self.h1=0; self.images=[]; self.labels=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a:self.ids.append(a["id"])
        if tag=="h1":self.h1+=1
        if tag=="img":self.images.append(a)
        for key in ("href","src"):
            if key in a:self.refs.append(a[key])
        if "aria-labelledby" in a:self.labels.extend(a["aria-labelledby"].split())
pages={}
for file in root.rglob("*.html"):
    if ".git" in file.parts:continue
    p=Page();p.feed(file.read_text(encoding="utf-8"));pages[file.resolve()]=p
errors=[];refs=0
for file,p in pages.items():
    if p.h1!=1:errors.append(f"{file.name}: {p.h1} H1s")
    if len(p.ids)!=len(set(p.ids)):errors.append(f"{file.name}: duplicate IDs")
    for label in p.labels:
        if label not in p.ids:errors.append(f"{file.name}: missing ARIA label {label}")
    for a in p.images:
        if "alt" not in a:errors.append(f"{file.name}: missing alt")
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        path=unquote(u.path)
        target=(root/path.lstrip("/") if path.startswith("/") else file.parent/path) if path else file
        if not target.suffix and target.with_suffix(".html").is_file():target=target.with_suffix(".html")
        elif target.is_dir():target=target/"index.html"
        if not target.is_file():errors.append(f"{file.name}: missing {ref}");continue
        refs+=1
        if u.fragment and target.resolve() in pages and u.fragment not in pages[target.resolve()].ids:errors.append(f"{file.name}: missing fragment {ref}")
print(json.dumps({"pages":len(pages),"localReferences":refs,"errors":errors},indent=2))
raise SystemExit(bool(errors))
