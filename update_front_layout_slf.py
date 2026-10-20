import re

layout_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\resources\views\layouts\front.blade.php"

with open(layout_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Title and Meta
text = re.sub(
    r"<title>@yield\('title', '[^']+'\)</title>",
    "<title>@yield('title', 'Jasa SLF - Sertifikat Laik Fungsi Bangunan Gedung | Layanan Pengkaji Teknis Resmi')</title>",
    text
)
text = re.sub(
    r"<meta name=\"description\" content=\"@yield\('meta_description', '[^']+'\)\">",
    "<meta name=\"description\" content=\"@yield('meta_description', 'Layanan resmi Jasa SLF (Sertifikat Laik Fungsi), audit keandalan struktur beton/baja, proteksi kebakaran hydrant sprinkler, utilitas MEP, dan penerbitan SLF di 38 provinsi di Indonesia.')\">",
    text
)

# 2. Update Favicon (Building Shield Emblem in Orange & Dark Navy)
old_fav_pattern = r"<link rel=\"icon\"[^\n]+\n"
new_fav = """    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 2L4 7v9c0 8.84 5.16 13.8 12 15 6.84-1.2 12-6.16 12-15V7L16 2z' fill='%23ea580c'/%3E%3Cpath d='M16 4.5L6.5 8.5v7.2c0 7 4 10.9 9.5 11.9 5.5-1 9.5-4.9 9.5-11.9V8.5L16 4.5z' fill='%230f172a'/%3E%3Cpath d='M11 20V12h3v8h-3zm4 0V9h3v11h-3zm4 0v-6h3v6h-3z' fill='%23f97316'/%3E%3C/svg%3E">
"""
if re.search(old_fav_pattern, text):
    text = re.sub(old_fav_pattern, new_fav, text)
else:
    text = text.replace("<head>", "<head>\n" + new_fav)

# 3. Update CSS Root Palette to Orange & Dark Slate with Mint Highlights
new_palette = """:root {
            /* TEMA UTAMA: SAFETY ORANGE & SLATE NAVY (WARNA WEB: ORANGE DENGAN AKSEN HIJAU MUDA & BIRU MUDA) */
            --primary-orange: #ea580c; /* Deep Corporate Safety Orange */
            --primary-orange-dark: #c2410c; /* Burnished Rust */
            --primary-orange-deep: #9a3412; /* Dark Amber */
            --primary-orange-light: #fff7ed; /* Light Orange Tint */
            --primary-orange-subtle: #fed7aa; /* Soft Orange Border */
            --primary-orange-accent: #f97316; /* Energetic Safety Orange */

            --primary-blue: #ea580c; /* Main button/accent mapping */
            --primary-blue-dark: #c2410c;
            --primary-blue-deep: #0f172a; /* Deep Slate Navy */
            --primary-blue-light: #fff7ed;
            --primary-blue-subtle: #fed7aa;
            --primary-blue-accent: #f97316;

            --primary-green: #10b981; /* Fresh Mint / Green Safe Indicator */
            --primary-green-dark: #059669;
            --primary-green-light: #ecfdf5;
            --primary-green-subtle: #a7f3d0;

            --bg-dark: #0f172a; /* Midnight High-Tech Slate Navy */
            --bg-dark-card: #1e293b; /* Slate Card Background */
            --bg-dark-hover: #334155;
            --bg-light: #f8fafc; /* Crisp Clean Off-White */
            --bg-white: #ffffff;

            --text-dark: #0f172a;
            --text-muted: #64748b;
            --text-light: #cbd5e1;
            --accent-mint: #10b981;
            --accent-amber: #ea580c;

            --gold-gradient: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            --navy-gradient: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            --blue-gradient: linear-gradient(135deg, #ea580c 0%, #f97316 50%, #fb923c 100%);
            --yellow-gradient: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            --yellow-blue-gradient: linear-gradient(135deg, #ea580c 0%, #f97316 100%);

            --wa-green: #25d366;
            --wa-green-hover: #20ba5a;
            --border-dark: rgba(249, 115, 22, 0.25);
            --border-light: #fed7aa;
            --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.08);
            --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.1), 0 2px 4px -2px rgba(15, 23, 42, 0.06);
            --shadow-lg: 0 12px 28px -6px rgba(15, 23, 42, 0.28);
            --shadow-gold: 0 10px 25px -5px rgba(234, 88, 12, 0.45);
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-xl: 18px;
        }"""

text = re.sub(r":root\s*\{[^}]+\}", new_palette, text)

# 4. Update Nav-link Active Border Bottom Color to Safety Orange
text = re.sub(
    r"\.nav-link::after\s*\{[^}]*background:\s*[^;]+;",
    """.nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%) scaleX(0);
            width: 85%;
            height: 3px;
            background: #ea580c;
            border-radius: 4px 4px 0 0;
            box-shadow: 0 0 10px rgba(234, 88, 12, 0.85);""",
    text
)

text = re.sub(
    r"\.nav-link:hover\s*\{[^}]*\}",
    """.nav-link:hover {
            color: #ea580c;
            background: #fff7ed;
        }""",
    text
)

text = re.sub(
    r"\.nav-link\.active\s*\{[^}]*\}",
    """.nav-link.active {
            color: #ea580c;
            background: #fff7ed;
            font-weight: 800;
        }""",
    text
)

# 5. Update Header Button "Hubungi" (Compact, Orange Gradient + Soft Border)
old_btn_header_pattern = r"\.btn-wa-header\s*\{[^}]+\}\s*\.btn-wa-header:hover\s*\{[^}]+\}"
new_btn_header = """.btn-wa-header {
            background: linear-gradient(135deg, #ea580c 0%, #f97316 100%);
            color: #ffffff !important;
            border: 1px solid #fed7aa;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 7px 16px;
            border-radius: 50px;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 3px 10px rgba(234, 88, 12, 0.3);
            transition: all 0.25s ease;
            text-decoration: none;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .btn-wa-header:hover {
            background: linear-gradient(135deg, #f97316 0%, #c2410c 100%);
            color: #ffffff !important;
            transform: translateY(-1px);
            box-shadow: 0 5px 15px rgba(234, 88, 12, 0.45);
        }"""
text = re.sub(old_btn_header_pattern, new_btn_header, text)

# 6. Update Brand Logo in Navbar
brand_navbar_pattern = r"<a href=\"\{\{ route\('home'\) \}\}\" class=\"brand-logo\">[\s\S]*?<\/a>"
new_brand_navbar = """<a href="{{ route('home') }}" class="brand-logo">
                    <div class="brand-icon" style="background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%); border: 1.5px solid #fed7aa; color: #ffffff; box-shadow: 0 0 12px rgba(234, 88, 12, 0.4);">
                        <i class="bi bi-buildings-fill"></i>
                    </div>
                    <div class="brand-text">
                        <h1 style="font-size: 1.15rem; font-weight: 800; letter-spacing: -0.5px; color: #0f172a; margin: 0;">JASA <span style="color: #ea580c;">SLF</span></h1>
                        <span style="font-size: 0.65rem; font-weight: 700; color: #64748b; letter-spacing: 0.5px; text-transform: uppercase; display: block; margin-top: -2px;">Sertifikat Laik Fungsi</span>
                    </div>
                </a>"""
text = re.sub(brand_navbar_pattern, new_brand_navbar, text, count=1)

# 7. Update Footer Brand & Text
footer_brand_pattern = r"<div class=\"brand-logo\" style=\"margin-bottom: 14px;\">[\s\S]*?<\/p>"
new_footer_brand = """<div class="brand-logo" style="margin-bottom: 14px;">
                        <div class="brand-icon" style="background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%); border: 1.5px solid #fed7aa; color: #ffffff;">
                            <i class="bi bi-buildings-fill"></i>
                        </div>
                        <div class="brand-text">
                            <h3 style="font-size: 1.05rem; font-weight: 800; color: #fff;">JASA <span style="color: #f97316;">SLF</span></h3>
                            <span style="font-size: 0.68rem; color: #fed7aa; letter-spacing: 0.5px; text-transform: uppercase; display: block;">Sertifikat Laik Fungsi Bangunan Gedung</span>
                        </div>
                    </div>
                    <p class="footer-desc">
                        Lembaga pengkaji teknis dan sertifikasi keandalan bangunan gedung terakreditasi: Audit Keandalan Struktur Beton & Rangka Baja (NDT Hammer Test/UPV), Sistem Proteksi Kebakaran Hydrant & Sprinkler, Utilitas Mekanikal Elektrikal Plumbing (MEP), Aksesibilitas Disabilitas, serta Penerbitan & Perpanjangan Sertifikat Laik Fungsi (SLF) di 38 provinsi di Indonesia.
                    </p>"""
text = re.sub(footer_brand_pattern, new_footer_brand, text, count=1)

# 8. Update Footer Links to Jasa SLF Programs
footer_links_pattern = r"<ul class=\"footer-links\">[\s\S]*?<\/ul>"
# Let's replace the first footer-links (Program Resmi)
m_links = list(re.finditer(footer_links_pattern, text))
if m_links:
    first_link = m_links[0]
    new_footer_prog_links = """<ul class="footer-links">
                        <li><a href="{{ route('program.detail', 'jasa-slf-bangunan-gedung-industri-pabrik') }}">SLF Gedung Industri & Pabrik</a></li>
                        <li><a href="{{ route('program.detail', 'jasa-slf-bangunan-komersial-mall-hotel') }}">SLF Mall, Komersial & Hotel</a></li>
                        <li><a href="{{ route('program.detail', 'jasa-slf-fasilitas-rumah-sakit-kesehatan') }}">SLF Fasilitas Rumah Sakit & Medis</a></li>
                        <li><a href="{{ route('program.detail', 'training-audit-keandalan-struktur-bangunan-gedung') }}">Audit Keandalan Struktur NDT</a></li>
                        <li><a href="{{ route('programs') }}">Lihat Seluruh 8 Layanan Jasa SLF</a></li>
                    </ul>"""
    text = text[:first_link.start()] + new_footer_prog_links + text[first_link.end():]

# 9. Update Floating WA Modal Text
text = text.replace(
    "Hotline Resmi Layanan Jasa SLO & Uji Komisioning Ketenagalistrikan",
    "Hotline Resmi Layanan Jasa SLF & Audit Keandalan Bangunan Gedung"
)
text = text.replace(
    "Pilih kontak WhatsApp inspektur teknik dan konsultan kelaikan operasi listrik untuk respon cepat 24 jam:",
    "Pilih kontak WhatsApp tenaga ahli pengkaji teknis dan auditor keandalan struktur bangunan untuk respon cepat 24 jam:"
)
text = text.replace("0813-9981-0272", "0813-9981-0272")

with open(layout_path, "w", encoding="utf-8") as f:
    f.write(text)

print("layouts/front.blade.php updated successfully for Jasa SLF!")
