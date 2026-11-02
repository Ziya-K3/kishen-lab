"""Bake the HTML templates into a Python module for Cloudflare Workers."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
templates = ROOT / "templates"
out = ROOT / "data" / "embedded_templates.py"
lines = ["TEMPLATES = {"]
for path in sorted(templates.glob("*.html")):
    lines.append(f"    {path.name!r}: {path.read_text(encoding='utf-8')!r},")
lines.append("}")
lines.append("")
out.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {out}")
