import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def html_of(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", "replace")


people = html_of("https://thekishenlab.org/people/")
# content area roughly
start = people.find("Dr. Anil Kishen")
chunk = people[start:start + 80000]
chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk)
# mark images
chunk = re.sub(
    r'<img[^>]+src="([^"]+)"[^>]*>',
    lambda m: "\n[IMG " + m.group(1).split("/")[-1][:70] + "]\n",
    chunk,
)
text = re.sub(r"<[^>]+>", "\n", chunk)
text = re.sub(r"\n+", "\n", text)
print(text[:6000])

print("\n\n==== CSS BACKGROUNDS ====")
for css_url in [
    "https://thekishenlab.org/wp-content/uploads/elementor/css/post-8.css",
    "https://thekishenlab.org/wp-content/uploads/elementor/css/post-47.css",
    "https://thekishenlab.org/wp-content/uploads/elementor/css/post-157.css",
    "https://thekishenlab.org/wp-content/uploads/elementor/css/post-18.css",
]:
    css = html_of(css_url)
    print(css_url.split("/")[-1])
    for bg in re.findall(r'url\(([^)]+)\)', css):
        if any(ext in bg for ext in ("jpg", "png", "jpeg", "webp")):
            print(" ", bg[:180])
