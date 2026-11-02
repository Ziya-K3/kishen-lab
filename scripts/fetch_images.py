import urllib.request
from pathlib import Path

OUT = Path("static/images")
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "lab-group.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/08/Lab-picture-home-page-1-e1754040934339.jpeg",
    "anil-banner.jpg": "https://thekishenlab.org/wp-content/uploads/2025/08/WEB-BANNER-DENT-150-Kishen-Anil_2024-11-11_023.jpg",
    "anil-headshot.jpg": "https://www.utoronto.ca/sites/default/files/styles/scale_image_750_width_/public/2025-04/anil-Headshot-crop_0.jpg?itok=DoxA6i9D",
    "logo.png": "https://thekishenlab.org/wp-content/uploads/2025/06/ChatGPT-Image-Jul-28-2025-11_32_31-AM-e1753682688705.png",
    "prabha.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/10/WhatsApp-Image-2025-10-05-at-8.19.30-AM-e1761542817245.jpeg",
    "fangchi.png": "https://thekishenlab.org/wp-content/uploads/2025/07/alice.png",
    "fardad.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/08/IMG_1974-768x824.jpeg",
    "shivam.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/07/Shivam-Sharma-headshot-scaled.jpeg",
    "nandita.png": "https://thekishenlab.org/wp-content/uploads/2025/07/Screenshot-2025-07-30-124515-e1753859806201.png",
    "tanvi.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/07/Tanvi-Sharma-768x768.jpeg",
    "lauren.jpg": "https://thekishenlab.org/wp-content/uploads/2025/08/image001-768x829.jpg",
    "shahin.jpg": "https://thekishenlab.org/wp-content/uploads/2025/08/2023-09-21-21-06-28-644.jpg",
    "emma.jpeg": "https://thekishenlab.org/wp-content/uploads/2025/07/Emma-Afsa-768x768.jpeg",
    "fig-training.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/1-s2.0-S0020653925001509-gr1.jpg",
    "fig-glass.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/1-s2.0-S010956412500675X-gr3.jpg",
    "fig-wound.png": "https://thekishenlab.org/wp-content/uploads/2025/07/41598_2025_673_Fig1_HTML.png",
    "research-bench.jpg": "https://thekishenlab.org/wp-content/uploads/2025/08/FB_IMG_1754116196838-768x960.jpg",
    "focus.jpg": "https://thekishenlab.org/wp-content/uploads/2025/08/Screenshot-2025-08-02-171208.jpg",
    "news-dean.png": "https://thekishenlab.org/wp-content/uploads/2025/07/image.png",
    "news-grads.png": "https://thekishenlab.org/wp-content/uploads/2025/07/image-1.png",
    "fund-1.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/1.jpg",
    "fund-2.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/2.jpg",
    "fund-3.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/3.jpg",
    "fund-4.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/4.jpg",
    "fund-5.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/5.jpg",
    "fund-6.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/6.jpg",
    "media-1.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/1-3.jpg",
    "media-2.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/2-3.jpg",
    "media-3.jpg": "https://thekishenlab.org/wp-content/uploads/2025/07/3-3.jpg",
}

for name, url in FILES.items():
    dest = OUT / name
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        dest.write_bytes(data)
        print(f"ok {name} {len(data)}")
    except Exception as exc:
        print(f"FAIL {name} {exc}")
