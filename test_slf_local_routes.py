import urllib.request
import re

base_url = "http://127.0.0.1:8018"

routes = [
    "/",
    "/tentang-kami",
    "/program",
    "/program/jasa-slf-bangunan-gedung-industri-pabrik",
    "/program/jasa-slf-bangunan-komersial-mall-hotel",
    "/program/training-audit-keandalan-struktur-bangunan-gedung",
    "/artikel",
    "/artikel/training-jasa-slf-panduan-lengkap-sertifikat-laik-fungsi-slf-bangunan-gedung-standar-teknis-nasional-di-indonesia",
    "/wilayah/dki-jakarta",
    "/wilayah/dki-jakarta/kota-jakarta-selatan",
    "/wilayah/dki-jakarta/kota-jakarta-selatan/kebayoran-baru",
    "/artikel/training-jasa-slf-panduan-lengkap-sertifikat-laik-fungsi-slf-bangunan-gedung-standar-teknis-nasional-di-kebayoran-baru-kota-jakarta-selatan-dki-jakarta",
    "/hubungi-kami",
    "/admin/login"
]

print("=== TESTING LOCAL JASA SLF ROUTES (PORT 8018) ===")
for r in routes:
    url = base_url + r
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>([^<]+)</title>', body)
            title = title_m.group(1).strip() if title_m else 'No title'
            print(f"[OK 200] {r} -> {title[:65]}")
    except Exception as e:
        print(f"[ERROR] {r} -> {e}")
