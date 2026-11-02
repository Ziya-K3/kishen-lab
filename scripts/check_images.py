import urllib.request

pages = ["/", "/people", "/about", "/research", "/media", "/publications"]
for path in pages:
    html = urllib.request.urlopen("http://127.0.0.1:5050" + path).read().decode("utf-8", "replace")
    srcs = []
    marker = 'src="/static/images/'
    start = 0
    while True:
        i = html.find(marker, start)
        if i < 0:
            break
        j = html.find('"', i + 5)
        srcs.append(html[i + 5:j])
        start = j
    print(path, len(srcs))
    for src in srcs:
        status = urllib.request.urlopen("http://127.0.0.1:5050" + src).status
        print(" ", status, src)
