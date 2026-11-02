import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def html_of(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", "replace")


home = html_of("https://thekishenlab.org/")
srcs = re.findall(r"https://thekishenlab.org/wp-content/uploads/[^\"'\s)]+", home)
print("HOME unique")
seen = []
for src in srcs:
    src = src.split("?")[0]
    if src not in seen:
        seen.append(src)
        print(src)

print("\nPEOPLE context")
people = html_of("https://thekishenlab.org/people/")
# pull nearby text for each upload
for match in re.finditer(r"https://thekishenlab.org/wp-content/uploads/[^\"'\s)]+", people):
    src = match.group(0).split("?")[0]
    start = max(0, match.start() - 180)
    snippet = re.sub(r"<[^>]+>", " ", people[start:match.end() + 80])
    snippet = re.sub(r"\s+", " ", snippet)[:160]
    if "-150x" in src or "-300x" in src or "-280x" in src or "-278x" in src:
        continue
    print(src)
    print(" ", snippet)
    print()
