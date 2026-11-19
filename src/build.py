import re, html, importlib.util, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
def load(n):
    s = importlib.util.spec_from_file_location(n, pathlib.Path(__file__).parent / f"{n}.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.C
def ph(s): return re.sub(r"⟦(.*?)⟧", r'<span class="ph">[\1]</span>', s)
SOURCES = [("NAEMT TCCC","https://www.naemt.org/education/trauma-education/naemt-tccc"),
 ("JTS / CoTCCC Guidelines","https://jts.health.mil/index.cfm/committees/cotccc/guidelines"),
 ("JTS Prolonged Casualty Care","https://jts.health.mil/assets/docs/cpgs/Prolonged_Casualty_Care_Guidelines_21_Dec_2021_ID91v1.1.pdf"),
 ("AMedP-8.15 / STANAG 2122","https://www.coemed.org/files/stanags/03_AMEDP/AMedP-8.15_EDB_V1_E_2122.pdf"),
 ("AJP-4.10(A) — Role 1–3","https://shape.nato.int/resources/site6362/medica-secure/publications/ajp-4.10(a).pdf"),
 ("ATP 4-02.2 — 9-Line / MIST","https://armypubs.army.mil/epubs/DR_pubs/DR_a/pdf/web/ARN17834_ATP%204-02x2%20FINAL%20WEB.pdf"),
 ("BUMEDINST 1510.25B — Tier 4, Train-the-Trainer","https://www.med.navy.mil/Portals/62/Documents/BUMED/Directives/Instructions/1510.25B.pdf")]
SITE = "https://aleks-army.github.io/masazhyst/"
def page(C):
    b = C["base"]; uk = C["lang"]=="uk"
    nav = "".join(f'<a href="#{i}">{t}</a>' for i,t in C["nav"])
    lang = (f'<a href="index.html" aria-current="true" lang="uk">UA</a><a href="en/index.html" lang="en" hreflang="en">EN</a>' if uk
            else f'<a href="../index.html" lang="uk" hreflang="uk">UA</a><a href="index.html" aria-current="true" lang="en">EN</a>')
    card = "".join(f"<dt>{k}</dt><dd>{ph(v)}</dd>" for k,v in C["card"])
    facts = "".join(f"<li><b>{ph(a)}</b><span>{ph(t)}</span></li>" for a,t in C["facts"])
    about = "".join(f"<p>{ph(p)}</p>" for p in C["about_p"])
    pr = "".join(f"<li><i aria-hidden=\"true\">{n}</i><span>{t}</span></li>" for n,t in C["principles"])
    tl = "".join(f'<li class="{c}"><time>{ph(y)}</time><div><h3>{ph(h)}</h3><p>{ph(t)}</p></div></li>' for y,c,h,t in C["timeline"])
    phases = "".join(f'<article class="phase {c}"><span class="n">{n}</span><h3>{h}</h3><p class="en" lang="en">{e}</p><p>{t}</p></article>' for c,n,h,e,t in C["phases"])
    patches = "".join(f'<li class="patch {c}">{t}</li>' for c,t in C["patches"])
    march = "".join(f'<li class="ml{" paws" if i>4 else ""}"><b>{l}</b><span class="t" lang="en">{e}</span>{"" if not uk else f"<span class=u>{u}</span>"}</li>' for i,(l,e,u) in enumerate(C["march"]))
    tiers = "".join(f'<article class="tier {c}"><span class="lvl">{l}</span><h3>{h}</h3><p>{t}</p><span class="meta">{ph(m)}</span><span class="std">{ph(s)}</span></article>' for l,h,t,m,s,c in C["tiers"])
    topics = "".join(f"<li>{t}</li>" for t in C["topics"])
    fmts = "".join(f'<div class="fmt"><h3>{h}</h3><p>{t}</p></div>' for h,t in C["formats"])
    th = "".join(f'<th scope="col">{t}</th>' for t in C["th"])
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{ph(u)}</td><td>{ph(n)}</td><td>{ph(l)}</td><td><span class="st {s[0]}">{s[1]}</span></td></tr>' for a,u,n,l,s in C["rows"])
    src = " · ".join(f'<a href="{u}" rel="noopener" target="_blank">{t}</a>' for t,u in SOURCES)
    les = "".join(f'<article class="lesson"><span class="k">{k}</span><h3>{h}</h3><p>{t}</p></article>' for k,h,t in C["lessons"])
    aud = "".join(f"<li>{t}</li>" for t in C["aud"])
    cl = "".join(f"<li><span>{k}</span><b>{ph(v)}</b></li>" for k,v in C["clist"])
    opts = "".join(f"<option>{o}</option>" for o in C["f_opts"])
    alt_uk = "index.html" if uk else "../index.html"; alt_en = "en/index.html" if uk else "index.html"
    return f'''<!doctype html>
<html lang="{C["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{C["title"]}</title>
<meta name="description" content="{html.escape(C["desc"])}">
<meta name="robots" content="index,follow">
<meta name="theme-color" content="#0A1420">
<link rel="canonical" href="{SITE}{"" if uk else "en/"}">
<link rel="alternate" hreflang="uk" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{b}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{b}apple-touch-icon.png">
<link rel="preload" href="{b}assets/fonts/unbounded.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{b}assets/style.css">
<meta property="og:url" content="{SITE}{"" if uk else "en/"}">
<meta property="og:type" content="website">
<meta property="og:title" content="{C["title"]}">
<meta property="og:description" content="{html.escape(C["desc"])}">
</head>
<body id="top">
<a class="skip" href="#main">{C["skip"]}</a>
<div class="draft" role="note">{ph(C["draft"])}</div>
<header class="hdr">
 <div class="wrap">
  <a class="brand" href="#top"><img src="{b}assets/mark.svg" alt="" width="34" height="34"><span>{C["h1"]}<small>{C["brand_sub"]}</small></span></a>
  <button class="burger" aria-expanded="false" aria-controls="nav" aria-label="{C["menu"]}"><span></span><span></span><span></span></button>
  <nav class="nav" id="nav" aria-label="{C["menu"]}">{nav}<span class="lang" role="group" aria-label="Language">{lang}</span></nav>
 </div>
</header>
<main id="main">
<section class="hero dark" aria-labelledby="h1">
 <div class="wrap">
  <div>
   <p class="callsign">{C["callsign"]}</p>
   <h1 id="h1">{C["h1"]}<span class="tq" aria-hidden="true"></span></h1>
   <p class="role">{C["role"]}</p>
   <p class="lead">{C["lead"]}</p>
   <figure class="quote"><blockquote><p>{C["quote"]}</p></blockquote><figcaption><cite>— <a href="https://www.sefaria.org/Mishnah_Sanhedrin.4.5" rel="noopener" target="_blank">{C["quote_cite"]}</a></cite></figcaption></figure>
   <div class="ctas"><a class="btn btn-primary" href="#contact">{C["cta1"]} →</a><a class="btn btn-ghost" href="#standards">{C["cta2"]}</a></div>
  </div>
  <aside class="fcard" aria-label="{C["card_title"]}">
   <div class="fcard-top"><img src="{b}assets/mark.svg" alt="{C["alt_mark"]}" width="44" height="44"><div><b>{C["card_title"]}</b><span>{C["card_sub"]}</span></div></div>
   <div class="fcard-band" aria-hidden="true"></div>
   <dl>{card}</dl>
   <div class="march" aria-label="MARCH"><span>M</span><span>A</span><span>R</span><span>C</span><span>H</span></div>
  </aside>
 </div>
 <div class="ecg" aria-hidden="true"><svg viewBox="0 0 1200 70" preserveAspectRatio="none"><path d="M0 40H300l14-22 18 44 16-58 16 50 10-14H640l10-10 12 22 14-30 14 18H900l14-22 18 44 16-58 16 50 10-14H1200" fill="none" stroke="currentColor" stroke-width="2.2"/></svg></div>
</section>
<div class="facts"><div class="wrap"><ul>{facts}</ul></div></div>
<div class="orn" aria-hidden="true"></div>

<section id="about" class="about" aria-labelledby="about-h">
 <div class="wrap grid">
  <div><p class="eyebrow">{C["about_eye"]}</p><h2 id="about-h">{C["about_h"]}</h2>{about}<ul class="principles">{pr}</ul></div>
  <div class="photo" role="img" aria-label="{html.escape(re.sub(r"[⟦⟧]","",C["photo"]))}"><div><svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="20" r="11" fill="none" stroke="#4D5A69" stroke-width="2.5"/><path d="M10 58c2-14 11-22 22-22s20 8 22 22" fill="none" stroke="#4D5A69" stroke-width="2.5"/></svg>{ph(C["photo"])}</div></div>
 </div>
</section>

<section id="path" aria-labelledby="path-h" style="background:var(--paper-2)">
 <div class="wrap">
  <div class="section-head"><div><p class="eyebrow">{C["path_eye"]}</p><h2 id="path-h">{C["path_h"]}</h2></div><p class="mono" style="font-size:.8rem;color:var(--muted)">{C["path_note"]}</p></div>
  <ol class="tl">{tl}</ol>
 </div>
</section>

<section id="line" class="dark" aria-labelledby="line-h">
 <div class="wrap">
  <p class="eyebrow">{C["line_eye"]}</p><h2 id="line-h">{C["line_h"]}</h2><p class="lead">{C["line_lead"]}</p>
  <div class="phases">{phases}</div>
  <div class="split">
   <div class="panel"><h3>{C["pcc_h"]}</h3><p>{C["pcc_p"]}</p></div>
   <div class="panel red"><h3>{C["rif_h"]}</h3><p>{C["rif_p"]}</p></div>
  </div>
  <ul class="patches" style="list-style:none;padding:0">{patches}</ul>
  <p class="opsec">{C["opsec"]}</p>
 </div>
</section>
<div class="orn" aria-hidden="true"></div>

<section id="teach" aria-labelledby="teach-h">
 <div class="wrap">
  <p class="eyebrow">{C["teach_eye"]}</p><h2 id="teach-h">{C["teach_h"]}</h2><p class="lead">{C["teach_lead"]}</p>
  <h3 style="margin-top:40px">{C["march_h"]}</h3>
  <ol class="march-row" style="list-style:none;padding:0">{march}</ol>
  <p class="march-legend">{C["march_legend"]}</p>
  <div class="tiers">{tiers}</div>
  <h3 style="margin-top:40px">{C["topics_h"]}</h3>
  <ul class="chips">{topics}</ul>
  <h3 style="margin-top:44px">{C["formats_h"]}</h3>
  <div class="formats" style="margin-top:16px">{fmts}</div>
 </div>
</section>

<section id="standards" aria-labelledby="std-h" style="background:var(--paper-2)">
 <div class="wrap">
  <p class="eyebrow">{C["std_eye"]}</p><h2 id="std-h">{C["std_h"]}</h2><p class="lead">{C["std_lead"]}</p>
  <div class="tbl-wrap" tabindex="0" role="region" aria-labelledby="std-h"><table><caption>{C["caption"]}</caption><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>
  <div class="disclaimer" role="note"><span aria-hidden="true">⚠</span><p style="margin:0"><b>{C["disc_b"]}</b> {C["disc"]}</p></div>
  <p class="sources">{C["sources_t"]} {src}</p>
 </div>
</section>


<section id="partners" class="dark" aria-labelledby="part-h">
 <div class="wrap">
  <p class="eyebrow">{C["part_eye"]}</p><h2 id="part-h">{C["part_h"]}</h2><p class="lead">{C["part_lead"]}</p>
  <div class="lessons">{les}</div>
  <p style="margin:28px 0 24px;color:#B9C6D4">{" · ".join(C["aud"])}</p>
  <a class="btn btn-primary" href="#contact">{C["part_cta"]} →</a>
 </div>
</section>

<div class="orn" aria-hidden="true"></div>

<section id="contact" class="dark contact" aria-labelledby="con-h">
 <div class="wrap grid">
  <div><p class="eyebrow">{C["con_eye"]}</p><h2 id="con-h">{C["con_h"]}</h2><p class="lead">{C["con_lead"]}</p><ul class="clist">{cl}</ul></div>
  <form id="invite" novalidate>
   <label>{C["f_name"]}<input name="name" autocomplete="name" required></label>
   <label>{C["f_org"]}<input name="org" autocomplete="organization"></label>
   <label>{C["f_country"]}<input name="country" autocomplete="country-name"></label>
   <label>{C["f_fmt"]}<select name="format">{opts}</select></label>
   <label class="full">{C["f_msg"]}<textarea name="msg"></textarea></label>
   <div class="full"><button class="btn btn-red" type="submit">{C["f_send"]}</button></div>
   <p class="form-note full">{C["f_note"]}</p>
   <p class="form-ok full" tabindex="-1" role="status">{C["f_ok"]}</p>
  </form>
 </div>
</section>
</main>
<footer>
 <div class="wrap">
  <div><a class="brand" href="#top"><img src="{b}assets/mark.svg" alt="" width="34" height="34"><span>{C["h1"]}<small>{C["brand_sub"]}</small></span></a></div>
  <div><p>{ph(C["foot1"])}</p><p>{C["foot2"]}</p><p class="note">{C["foot_note"]}</p></div>
 </div>
</footer>
<script src="{b}assets/app.js" defer></script>
</body>
</html>'''
(ROOT/"index.html").write_text(page(load("content_uk")), encoding="utf-8")
(ROOT/"en").mkdir(exist_ok=True)
(ROOT/"en"/"index.html").write_text(page(load("content_en")), encoding="utf-8")
print("built")
