#!/usr/bin/env python3
"""從 resume-en.yaml / resume-zh.yaml 產生個人網頁（單一 index.html，中英切換）。

用法：python3 site/build.py [--out _site]
輸出：_site/index.html + static 資產；PDF 若存在於 rendercv_output/ 也會一起複製。
"""
import argparse
import datetime as dt
import pathlib
import re
import shutil
import subprocess

import jinja2
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def md_inline(s: str) -> str:
    s = LINK_RE.sub(r'<a href="\2">\1</a>', s)
    s = BOLD_RE.sub(r"<strong>\1</strong>", s)
    return s


def fmt_date(d, lang: str) -> str:
    if d is None:
        return ""
    s = str(d)
    if s == "present":
        return "至今" if lang == "zh" else "present"
    parts = s.split("-")
    y = parts[0]
    m = int(parts[1]) if len(parts) > 1 else None
    if lang == "zh":
        return f"{y} 年 {m} 月" if m else y
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[m-1]} {y}" if m else y


def date_range(item: dict, lang: str) -> str:
    if item.get("date"):
        return fmt_date(item["date"], lang)
    a, b = item.get("start_date"), item.get("end_date")
    if a and b:
        return f"{fmt_date(a, lang)} – {fmt_date(b, lang)}"
    return fmt_date(a or b, lang)


def year_of(item: dict) -> str:
    d = item.get("date") or item.get("start_date") or ""
    return str(d)[:4]


def classify(item):
    if isinstance(item, str):
        return "text"
    if "company" in item:
        return "experience"
    if "institution" in item:
        return "education"
    if "label" in item:
        return "oneline"
    if "name" in item:
        return "project"
    return "other"


def load(lang: str) -> dict:
    d = yaml.safe_load((ROOT / f"resume-{lang}.yaml").read_text(encoding="utf-8"))
    cv = d["cv"]
    sections = []
    for title, items in cv.get("sections", {}).items():
        entries = []
        for it in items:
            kind = classify(it)
            e = {"kind": kind}
            if kind == "text":
                e["html"] = md_inline(it)
            else:
                e.update(it)
                e["when"] = date_range(it, lang)
                e["year"] = year_of(it)
                e["highlights"] = [md_inline(h) for h in it.get("highlights", [])]
                if it.get("details"):
                    e["details_html"] = md_inline(str(it["details"]))
            entries.append(e)
        if lang == "en":
            title = title.replace("_", " ")
            title = title[:1].upper() + title[1:]
        sections.append({"title": title, "entries": entries})
    return {"cv": cv, "sections": sections}


def git_last_updated() -> str:
    try:
        out = subprocess.check_output(["git", "-C", str(ROOT), "log", "-1", "--format=%cs"], text=True).strip()
        return out or dt.date.today().isoformat()
    except Exception:
        return dt.date.today().isoformat()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(SITE)), autoescape=False)
    tpl = env.get_template("template.html")

    pdfs = {}
    for lang, pattern in (("en", "Kai-Chi_Huang_CV.pdf"), ("zh", "黃楷奇_CV.pdf")):
        for cand in ROOT.glob(f"rendercv_output/{pattern}"):
            target = out / ("cv-en.pdf" if lang == "en" else "cv-zh.pdf")
            shutil.copy(cand, target)
            pdfs[lang] = target.name

    html = tpl.render(en=load("en"), zh=load("zh"), pdfs=pdfs, updated=git_last_updated())
    (out / "index.html").write_text(html, encoding="utf-8")
    for f in (SITE / "static").iterdir():
        shutil.copy(f, out / f.name)
    print(f"built → {out/'index.html'}  (pdfs: {list(pdfs)})")


if __name__ == "__main__":
    main()
