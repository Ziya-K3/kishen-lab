import html
import json
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return json.load(resp)


def imgs_from(content):
    found = []
    for tag in re.findall(r"<img[^>]+>", content):
        src = re.search(r'src="([^"]+)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        if src:
            found.append((html.unescape(alt.group(1) if alt else ""), src.group(1)))
    return found


pages = get("https://thekishenlab.org/wp-json/wp/v2/pages?per_page=20")
for page in pages:
    found = imgs_from(page["content"]["rendered"])
    print("=== PAGE", page["slug"], len(found))
    for alt, src in found:
        print(f"  {alt[:70]} | {src}")

posts = get("https://thekishenlab.org/wp-json/wp/v2/posts?per_page=20&_embed=1")
print("=== POSTS")
for post in posts:
    title = html.unescape(post["title"]["rendered"])[:80]
    media = (post.get("_embedded") or {}).get("wp:featuredmedia") or [{}]
    feat = media[0].get("source_url", "") if media and media[0] else ""
    found = imgs_from(post["content"]["rendered"])
    print("-", title)
    print("  feat", feat)
    for alt, src in found[:6]:
        print(f"  {alt[:50]} | {src}")
