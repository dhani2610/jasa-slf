import os
import re

views_dir = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\resources\views\front"

# 1. Update programs.blade.php
prog_file = os.path.join(views_dir, "programs.blade.php")
with open(prog_file, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Layanan Jasa SLF & Sertifikasi Keandalan Bangunan Gedung | Standar Teknis Nasional')",
    text
)
text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Katalog 8 layanan resmi Jasa SLF (Sertifikat Laik Fungsi): Bangunan Industri, Komersial, Rumah Sakit, Data Center, Audit Struktur NDT, Fire Safety, MEP, dan Perpanjangan SLF.')",
    text
)
text = text.replace("Jasa SLO & Sertifikasi Kelaikan Operasi Listrik", "Jasa SLF & Sertifikasi Laik Fungsi Bangunan Gedung")
text = text.replace("Jasa SLO Indonesia", "Jasa SLF Indonesia")
text = text.replace("Layanan Resmi SLO", "Layanan Resmi SLF")
text = text.replace("Konsultasi SLO", "Konsultasi SLF")
text = text.replace("Lembaga Inspeksi Teknik Terakreditasi & Standar Keselamatan Ketenagalistrikan", "Lembaga Pengkaji Teknis Terakreditasi & Standar Keandalan Bangunan Gedung")
text = text.replace(
    "Pastikan seluruh instalasi ketenagalistrikan fasilitas industri, komersial, dan pembangkit mandiri Anda lulus uji kelaikan operasi (SLO) berstandar PUIL nasional bersama tim inspektur teknik profesional dan instrumen uji terkalibrasi KAN.",
    "Pastikan seluruh fasilitas bangunan gedung pabrik industri, komersial, hotel, rumah sakit, dan perkantoran Anda lulus audit keandalan struktur dan sistem proteksi kebakaran demi terbitnya Sertifikat Laik Fungsi (SLF) resmi berbarcode sah."
)
text = text.replace("4 Hotline WhatsApp Layanan Resmi Jasa SLO Ketenagalistrikan", "4 Hotline WhatsApp Layanan Resmi Jasa SLF Bangunan Gedung")
text = text.replace("background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);", "background: linear-gradient(135deg, #ea580c 0%, #f97316 100%);")
text = text.replace("border: 1.5px solid #bfdbfe;", "border: 1.5px solid #fed7aa;")
text = text.replace("border: 2px solid rgba(56, 189, 248, 0.4);", "border: 2px solid rgba(249, 115, 22, 0.4);")

with open(prog_file, "w", encoding="utf-8") as f:
    f.write(text)
print("Updated programs.blade.php for SLF")

# 2. Update about.blade.php
about_file = os.path.join(views_dir, "about.blade.php")
with open(about_file, "r", encoding="utf-8") as f:
    abt_text = f.read()

abt_text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Tentang Kami | Profil Lembaga Pengkaji Teknis Jasa SLF & Keandalan Bangunan Gedung')",
    abt_text
)
abt_text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Profil lembaga pengkaji teknis bangunan gedung independen, sejarah, visi, misi, legalitas dan tim ahli structural & fire safety auditor di Indonesia.')",
    abt_text
)
abt_text = abt_text.replace("Jasa SLO Indonesia", "Jasa SLF Indonesia")
abt_text = abt_text.replace("Jasa SLO", "Jasa SLF")
abt_text = abt_text.replace("Sertifikat Laik Operasi (SLO)", "Sertifikat Laik Fungsi (SLF)")
abt_text = abt_text.replace("Sertifikat Laik Operasi", "Sertifikat Laik Fungsi")
abt_text = abt_text.replace("kelaikan operasi listrik", "kelaikan fungsi bangunan gedung")
abt_text = abt_text.replace("Standar Uji Kelaikan PUIL", "Standar Keandalan Bangunan Gedung")
abt_text = abt_text.replace("Pengujian Tahanan Isolasi Megger & Grounding", "Audit Keandalan Struktur NDT & Fire Safety")
abt_text = abt_text.replace("Sertifikasi Tenaga Teknik SKTTK", "Sertifikasi Tenaga Ahli Pengkaji Teknis")
abt_text = abt_text.replace("Zero Electrical Fire & Incident", "Zero Building Disaster & Zero Accident")

with open(about_file, "w", encoding="utf-8") as f:
    f.write(abt_text)
print("Updated about.blade.php for SLF")

# 3. Update contact.blade.php
contact_file = os.path.join(views_dir, "contact.blade.php")
with open(contact_file, "r", encoding="utf-8") as f:
    cnt_text = f.read()

cnt_text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Kontak Kami | Layanan Cepat Permohonan Sertifikat Laik Fungsi (Jasa SLF)')",
    cnt_text
)
cnt_text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Hubungi tim tenaga ahli pengkaji teknis resmi Jasa SLF untuk permohonan audit struktur, proteksi kebakaran, dan sertifikasi kelaikan fungsi gedung di seluruh Indonesia.')",
    cnt_text
)
cnt_text = cnt_text.replace("Jasa SLO Indonesia", "Jasa SLF Indonesia")
cnt_text = cnt_text.replace("Jasa SLO", "Jasa SLF")
cnt_text = cnt_text.replace("Sertifikat Laik Operasi", "Sertifikat Laik Fungsi")
cnt_text = cnt_text.replace("Inspektur Teknik Ketenagalistrikan", "Tenaga Ahli Pengkaji Teknis Bangunan")
cnt_text = cnt_text.replace("Permohonan Sertifikasi SLO", "Permohonan Sertifikat SLF")

with open(contact_file, "w", encoding="utf-8") as f:
    f.write(cnt_text)
print("Updated contact.blade.php for SLF")

# 4. Update articles.blade.php & article-detail.blade.php
for a_fname in ["articles.blade.php", "article-detail.blade.php"]:
    a_path = os.path.join(views_dir, a_fname)
    with open(a_path, "r", encoding="utf-8") as f:
        art_t = f.read()
    art_t = art_t.replace("Jasa SLO Indonesia", "Jasa SLF Indonesia")
    art_t = art_t.replace("Jasa SLO Ketenagalistrikan", "Jasa SLF Bangunan Gedung")
    art_t = art_t.replace("Jasa SLO", "Jasa SLF")
    art_t = art_t.replace("Sertifikat Laik Operasi", "Sertifikat Laik Fungsi")
    art_t = art_t.replace("Lead Electrical Inspector & Tim Ahli Ketenagalistrikan", "Lead Structural Auditor & Tim Pengkaji Teknis SLF")
    art_t = art_t.replace("Uji Kelaikan Operasi PUIL", "Audit Keandalan Bangunan Gedung")
    art_t = art_t.replace("border: 1px solid #bfdbfe;", "border: 1px solid #fed7aa;")
    art_t = art_t.replace("background: #1d4ed8;", "background: #ea580c;")
    art_t = art_t.replace("color: #1d4ed8;", "color: #ea580c;")
    art_t = art_t.replace("background: #eff6ff;", "background: #fff7ed;")
    art_t = art_t.replace("border: 1px solid #bae6fd;", "border: 1px solid #fed7aa;")
    art_t = art_t.replace("color: #0284c7;", "color: #ea580c;")
    with open(a_path, "w", encoding="utf-8") as f:
        f.write(art_t)
    print(f"Updated {a_fname} for SLF")

# 5. Update regional views: wilayah-provinsi, wilayah-kabkot, wilayah-kecamatan, program-region-detail, program-detail
for w_fname in ["wilayah-provinsi.blade.php", "wilayah-kabkot.blade.php", "wilayah-kecamatan.blade.php", "program-region-detail.blade.php", "program-detail.blade.php"]:
    w_path = os.path.join(views_dir, w_fname)
    with open(w_path, "r", encoding="utf-8") as f:
        w_t = f.read()
    w_t = w_t.replace("Jasa SLO Ketenagalistrikan", "Jasa SLF Bangunan Gedung")
    w_t = w_t.replace("Jasa SLO", "Jasa SLF")
    w_t = w_t.replace("Sertifikat Laik Operasi (SLO)", "Sertifikat Laik Fungsi (SLF)")
    w_t = w_t.replace("Sertifikat Laik Operasi", "Sertifikat Laik Fungsi")
    w_t = w_t.replace("Lead Electrical Inspector & Tim Ahli Ketenagalistrikan", "Lead Structural Auditor & Tim Pengkaji Teknis SLF")
    w_t = w_t.replace("Uji Komisioning & Kelaikan Listrik PUIL", "Audit Keandalan Struktur & Fire Safety")
    w_t = w_t.replace("border: 1px solid #bfdbfe;", "border: 1px solid #fed7aa;")
    w_t = w_t.replace("background: #1d4ed8;", "background: #ea580c;")
    w_t = w_t.replace("color: #1d4ed8;", "color: #ea580c;")
    w_t = w_t.replace("background: #eff6ff;", "background: #fff7ed;")
    w_t = w_t.replace("color: #0284c7;", "color: #ea580c;")
    w_t = w_t.replace("border: 1px solid #bae6fd;", "border: 1px solid #fed7aa;")
    with open(w_path, "w", encoding="utf-8") as f:
        f.write(w_t)
    print(f"Updated {w_fname} for SLF")

print("All front views successfully updated for Jasa SLF!")
