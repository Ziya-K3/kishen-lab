import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def html_of(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", "replace")


home = html_of("https://thekishenlab.org/")
print("lab picture mentions", home.lower().count("lab-picture"), home.lower().count("background-image"))
bgs = re.findall(r"url\(([^)]+)\)", home)
print("url() count", len(bgs))
for bg in bgs:
    if "upload" in bg or "jpg" in bg or "png" in bg or "jpeg" in bg or "webp" in bg:
        print(bg[:180])

css = html_of("https://thekishenlab.org/wp-content/uploads/elementor/css/post-18.css")
print("\nPOST 18 css len", len(css))
for bg in re.findall(r"url\(([^)]+)\)", css):
    print("18", bg[:200])

css105 = html_of("https://thekishenlab.org/wp-content/uploads/elementor/css/post-105.css")
print("\nPOST 105")
for bg in re.findall(r"url\(([^)]+)\)", css105):
    if any(ext in bg for ext in ("jpg", "png", "jpeg", "webp")):
        print("105", bg[:200])
