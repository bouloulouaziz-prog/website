"""Controleert alle lokale links, plaatjes en css in de HTML-bestanden.
Gebruik: python3 controle_links.py <pad naar de sitemap>"""
import sys, os, re
from html.parser import HTMLParser
root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "..")
class P(HTMLParser):
    def __init__(s): super().__init__(); s.refs=[]; s.imgs=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=="a" and a.get("href"): s.refs.append(a["href"])
        if t=="link" and a.get("href"): s.refs.append(a["href"])
        if t=="img": s.imgs.append(a); s.refs.append(a.get("src",""))
fout=0; n=0
for dp,_,fs in os.walk(root):
    for f in fs:
        if not f.endswith(".html"): continue
        p=os.path.join(dp,f); h=P(); h.feed(open(p,encoding="utf-8").read())
        for r in h.refs:
            if re.match(r"(https?:|mailto:|#)",r): continue
            n+=1
            t=os.path.normpath(os.path.join(dp,r.split("#")[0]))
            if r.startswith("/") or ":" in r[:3] or not os.path.exists(t):
                print("FOUT:",os.path.relpath(p,root),"->",r); fout+=1
        for i in h.imgs:
            if not i.get("alt"): print("FOUT: alt-tekst mist in",os.path.relpath(p,root)); fout+=1
print(f"{n} lokale verwijzingen gecontroleerd, {fout} fouten")
sys.exit(1 if fout else 0)
