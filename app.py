"""Kishen Lab research site."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from flask import Flask, jsonify, render_template, request
from jinja2 import ChoiceLoader, DictLoader, FileSystemLoader

from data.embedded_templates import TEMPLATES

from data.content import (
    ABOUT,
    ALUMNI,
    AWARDS,
    BASIC,
    COVERS,
    CURRENT,
    DIRECTOR,
    FUNDS,
    IMPACT,
    LAB,
    MEDIA,
    NEWS,
    PAGES,
    PAPERS,
    PARTNERS,
    PATENTS,
    PILLARS,
    STATS,
    TESTIMONIALS,
    THEMES,
    TRANSLATIONS,
)

ROOT = Path(__file__).resolve().parent
INSTANCE = ROOT / "instance"
INBOX = INSTANCE / "messages.json"

app = Flask(__name__)
app.secret_key = "kishen-lab-local-key"
app.jinja_loader = ChoiceLoader(
    [
        FileSystemLoader(str(ROOT / "templates")),
        DictLoader(TEMPLATES),
    ]
)

NAV = [
    ("Home", "home"),
    ("About", "about"),
    ("Research", "research"),
    ("People", "people"),
    ("Publications", "publications"),
    ("Awards", "awards"),
    ("Media", "media"),
    ("Contact", "contact"),
]


def _blob(*parts: str) -> str:
    return " ".join(p for p in parts if p).lower()


def search_index():
    items = []
    for page in PAGES:
        items.append(
            {
                "kind": page["kind"],
                "title": page["title"],
                "href": page["href"],
                "meta": "On this site",
                "text": _blob(page["title"], page["text"]),
            }
        )
    for paper in PAPERS:
        items.append(
            {
                "kind": "Paper",
                "title": paper["title"],
                "href": "/publications?q=" + quote(paper["title"][:48]),
                "meta": f"{paper['year']} · {paper['journal']}",
                "text": _blob(paper["title"], paper["authors"], paper["journal"], paper["summary"], paper["theme"]),
            }
        )
    for person in CURRENT:
        items.append(
            {
                "kind": "People",
                "title": person["name"],
                "href": "/people#current",
                "meta": person["role"],
                "text": _blob(person["name"], person["role"], person["project"]),
            }
        )
    items.append(
        {
            "kind": "People",
            "title": DIRECTOR["name"],
            "href": "/people",
            "meta": "Principal investigator",
            "text": _blob(DIRECTOR["name"], " ".join(DIRECTOR["titles"]), " ".join(DIRECTOR["bio"])),
        }
    )
    for award in AWARDS:
        items.append(
            {
                "kind": "Award",
                "title": award["title"],
                "href": f"/awards?scope={award['scope']}#{award['year']}",
                "meta": str(award["year"]),
                "text": _blob(award["title"], award["detail"], str(award["year"]), award["scope"]),
            }
        )
    for story in NEWS + [
        {"title": item["title"], "summary": item["outlet"], "outlet": item["outlet"], "date": item["year"]}
        for item in MEDIA
    ]:
        items.append(
            {
                "kind": "Media",
                "title": story["title"],
                "href": story.get("href") or "/media",
                "meta": story.get("outlet") or story.get("date", ""),
                "text": _blob(story["title"], story.get("summary", ""), story.get("outlet", "")),
            }
        )
    for patent in PATENTS:
        items.append(
            {
                "kind": "Patent",
                "title": patent["title"],
                "href": "/research#patents",
                "meta": patent["number"],
                "text": _blob(patent["title"], patent["summary"], patent["inventors"], patent["number"]),
            }
        )
    return items


INDEX = search_index()


def filter_papers(q: str, year: str, theme: str):
    q = q.strip().lower()
    found = []
    for paper in PAPERS:
        if year and str(paper["year"]) != year:
            continue
        if theme and paper["theme"] != theme:
            continue
        hay = _blob(paper["title"], paper["authors"], paper["journal"], paper["summary"], paper["theme"])
        if q and q not in hay:
            continue
        found.append(paper)
    return found


@app.context_processor
def inject():
    return {
        "lab": LAB,
        "nav": NAV,
        "now_year": datetime.now().year,
    }


@app.route("/")
def home():
    return render_template(
        "index.html",
        page="home",
        stats=STATS,
        pillars=PILLARS,
        papers=[p for p in PAPERS if p["featured"]],
        news=[n for n in NEWS if n["featured"]],
        testimonials=TESTIMONIALS,
        partners=PARTNERS,
        funds=FUNDS,
        translations=TRANSLATIONS,
    )


@app.route("/about")
def about():
    return render_template("about.html", page="about", about=ABOUT, director=DIRECTOR, stats=STATS)


@app.route("/research")
def research():
    return render_template(
        "research.html",
        page="research",
        pillars=PILLARS,
        basic=BASIC,
        impact=IMPACT,
        translations=TRANSLATIONS,
        patents=PATENTS,
    )


@app.route("/people")
def people():
    return render_template(
        "people.html",
        page="people",
        director=DIRECTOR,
        current=CURRENT,
        alumni=ALUMNI,
    )


@app.route("/publications")
def publications():
    q = request.args.get("q", "")
    year = request.args.get("year", "")
    theme = request.args.get("theme", "")
    papers = filter_papers(q, year, theme)
    years = sorted({p["year"] for p in PAPERS}, reverse=True)
    return render_template(
        "publications.html",
        page="publications",
        papers=papers,
        total=len(PAPERS),
        years=years,
        themes=THEMES,
        q=q,
        year=year,
        theme=theme,
    )


@app.route("/api/publications")
def api_publications():
    q = request.args.get("q", "")
    year = request.args.get("year", "")
    theme = request.args.get("theme", "")
    papers = filter_papers(q, year, theme)
    return jsonify({"count": len(papers), "papers": papers})


@app.route("/api/search")
def api_search():
    q = request.args.get("q", "").strip().lower()
    if len(q) < 2:
        return jsonify({"results": []})
    hits = []
    for item in INDEX:
        if q in item["text"]:
            hits.append({k: item[k] for k in ("kind", "title", "href", "meta")})
        if len(hits) == 10:
            break
    return jsonify({"results": hits})


@app.route("/awards")
def awards():
    scope = request.args.get("scope", "all")
    if scope not in {"all", "personal", "team"}:
        scope = "all"
    rows = [a for a in AWARDS if scope == "all" or a["scope"] == scope]
    return render_template("awards.html", page="awards", awards=rows, scope=scope)


@app.route("/media")
def media():
    return render_template("media.html", page="media", news=NEWS, media=MEDIA, covers=COVERS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    stored = False
    error = ""
    if request.method == "POST":
        if request.form.get("company"):
            sent = True
        else:
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            role = request.form.get("role", "").strip()
            message = request.form.get("message", "").strip()
            if len(name) < 2 or "@" not in email or "." not in email.split("@")[-1] or len(message) < 12:
                error = "Add your name, a real email, and a note of at least a sentence."
            else:
                entry = {
                    "name": name,
                    "email": email,
                    "role": role or "General",
                    "message": message,
                    "at": datetime.now(timezone.utc).isoformat(),
                }
                existing = []
                if INBOX.exists():
                    try:
                        existing = json.loads(INBOX.read_text(encoding="utf-8"))
                    except json.JSONDecodeError:
                        existing = []
                existing.append(entry)
                try:
                    INSTANCE.mkdir(exist_ok=True)
                    INBOX.write_text(json.dumps(existing, indent=2), encoding="utf-8")
                    stored = True
                except OSError:
                    stored = False
                sent = True
    return render_template("contact.html", page="contact", sent=sent, error=error, stored=stored)


@app.route("/sitemap.xml")
def sitemap():
    paths = ["/", "/about", "/research", "/people", "/publications", "/awards", "/media", "/contact"]
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    base = request.host_url.rstrip("/")
    for path in paths:
        body.append(f"<url><loc>{base}{path}</loc></url>")
    body.append("</urlset>")
    return app.response_class("\n".join(body), mimetype="application/xml")


@app.errorhandler(404)
def missing(_err):
    return render_template("404.html", page=""), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
