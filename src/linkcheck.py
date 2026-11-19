import re, pathlib, urllib.parse
from html.parser import HTMLParser
R = pathlib.Path(__file__).resolve().parent.parent
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=set(); s.imgs_noalt=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if "id" in a: s.ids.add(a["id"])
        for k in ("href","src"):
            if k in a: s.links.append(a[k])
        if t=="img" and "alt" not in a: s.imgs_noalt+=1
pages={}
for f in R.rglob("*.html"):
    p=P(); p.feed(f.read_text()); pages[f]=p
total=bad=ext=0
for f,p in pages.items():
    for l in p.links:
        if l.startswith(("http://","https://","mailto:")): ext+=1; continue
        total+=1
        u=urllib.parse.urlparse(l); target=(f.parent/u.path).resolve() if u.path else f
        if not target.exists() or not str(target).startswith(str(R)): print("BROKEN",f.relative_to(R),l); bad+=1; continue
        if u.fragment:
            tp=pages.get(target)
            if tp is None or u.fragment not in tp.ids: print("BROKEN ANCHOR",f.relative_to(R),l); bad+=1
    print(f.relative_to(R),"imgs without alt:",p.imgs_noalt)
# css url()
for c in R.rglob("*.css"):
    for u in re.findall(r"url\(([^)\"']+)\)",c.read_text()):
        total+=1
        if not (c.parent/u).exists(): print("BROKEN CSS",u); bad+=1
print(f"internal checked={total} broken={bad} external(not checked)={ext}")
