import re

controller_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\app\Http\Controllers\FrontController.php"

with open(controller_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Service
text = text.replace("use App\\Services\\JasaSloSchemeService;", "use App\\Services\\JasaSlfSchemeService;")
text = text.replace("JasaSloSchemeService::", "JasaSlfSchemeService::")

# Update WhatsApp Text
text = text.replace(
    "Jasa SLO Indonesia, saya ingin konsultasi permohonan Sertifikat Laik Operasi (SLO) instalasi listrik (IPTL TR/TM, Genset, PLTS, Distribusi) untuk wilayah {region}. Mohon informasi persyaratan, jadwal inspeksi komisioning, dan estimasi biaya.",
    "Jasa SLF Indonesia, saya ingin konsultasi permohonan Sertifikat Laik Fungsi (SLF) bangunan gedung (Pabrik, Gudang, Mall, Hotel, Rumah Sakit, Gedung Bertingkat) untuk wilayah {region}. Mohon info persyaratan dokumen teknis, audit struktur/fire safety, dan estimasi biaya."
)
text = text.replace(
    "Jasa SLO & Sertifikasi Kelaikan Operasi Listrik",
    "Jasa SLF & Sertifikasi Laik Fungsi Bangunan Gedung"
)
text = text.replace(
    "Halo Admin Utama Jasa SLO Indonesia, saya ingin mengajukan permohonan Sertifikat Laik Operasi (SLO){$progText} di wilayah {$regionText}.",
    "Halo Admin Utama Jasa SLF Indonesia, saya ingin mengajukan permohonan Sertifikat Laik Fungsi (SLF){$progText} di wilayah {$regionText}."
)
text = text.replace(
    "Halo CS Jasa SLO Indonesia (Hotline 2), mohon info jadwal uji komisioning, inspeksi kelaikan listrik, dan kuota sertifikasi di {$regionText}.",
    "Halo CS Jasa SLF Indonesia (Hotline 2), mohon info jadwal audit keandalan struktur, inspeksi fire safety, dan kuota sertifikasi di {$regionText}."
)
text = text.replace(
    "Halo Tim Inspektur Teknik Ketenagalistrikan (Hotline 3), saya ingin konsultasi teknis pengujian trafo, genset, grounding, dan single line diagram di {$regionText}.",
    "Halo Tim Ahli Pengkaji Teknis Bangunan (Hotline 3), saya ingin konsultasi teknis NDT hammer test, proteksi kebakaran hydrant, dan as-built drawing di {$regionText}."
)
text = text.replace(
    "Halo Tim Sertifikasi SKTTK & Kerjasama Korporat (Hotline 4), kami ingin konsultasi sertifikasi kompetensi personel listrik dan paket uji SLO industri di {$regionText}.",
    "Halo Tim Sertifikasi & Perpanjangan SLF Korporat (Hotline 4), kami ingin konsultasi audit kelaikan fungsi gedung dan kontrak pemeliharaan berkala di {$regionText}."
)

# Update hotline descriptions
text = text.replace(
    "'Hotline Utama (Permohonan & Sertifikasi SLO)'",
    "'Hotline Utama (Permohonan & Sertifikasi SLF)'"
)
text = text.replace(
    "'Layanan resmi konsultasi permohonan Sertifikat Laik Operasi (SLO) TR/TM, Genset, dan PLTS.'",
    "'Layanan resmi konsultasi permohonan Sertifikat Laik Fungsi (SLF) pabrik, mall, hotel, rumah sakit, dan gedung bertingkat.'"
)
text = text.replace(
    "'Hotline 2 (Jadwal Inspeksi & Uji Komisioning)'",
    "'Hotline 2 (Jadwal Asesmen & Uji Lapangan)'"
)
text = text.replace(
    "'Penjadwalan inspeksi lapangan, pengujian alat ukur megger, grounding, dan verifikasi dokumen.'",
    "'Penjadwalan inspeksi keandalan struktur, uji NDT hammer test, audit hydrant sprinkler, dan verifikasi as-built drawing.'"
)
text = text.replace(
    "'Hotline 3 (Konsultasi Teknis Elektro & Proteksi)'",
    "'Hotline 3 (Konsultasi Ahli Struktur & Fire Safety)'"
)
text = text.replace(
    "'Konsultasi teknis PUIL, Single Line Diagram (SLD), relai proteksi, trafo, dan kualitas daya.'",
    "'Konsultasi teknis struktur beton/baja, uji pembebanan, sistem proteksi kebakaran pasif/aktif, dan utilitas MEP.'"
)
text = text.replace(
    "'Hotline 4 (Sertifikasi Tenaga Teknik SKTTK & Korporat)'",
    "'Hotline 4 (Perpanjangan SLF & Pemeliharaan Gedung)'"
)
text = text.replace(
    "'Sertifikasi kompetensi personel kelistrikan (SKTTK) dan kontrak inspeksi berkala korporasi.'",
    "'Pengurusan perpanjangan berkala Sertifikat Laik Fungsi (SLF), manual pemeliharaan gedung, dan kontrak audit korporasi.'"
)

# Update Partners
old_partners = """        $partners = [
            ['name' => 'PT PLN (Persero)', 'role' => 'Kemitraan Standardisasi Kelaikan Operasi & Penyaluran Tenaga Listrik Konsumen Tegangan Menengah'],
            ['name' => 'PT Indonesia Power', 'role' => 'Uji Komisioning & Sertifikasi Laik Operasi Unit Pembangkitan Thermal dan PLTU'],
            ['name' => 'PT PLN Nusantara Power', 'role' => 'Sertifikasi Kelaikan Operasi Pembangkit Energi Baru Terbarukan (EBT) & PLTS Grid'],
            ['name' => 'PT Pertamina Power Indonesia', 'role' => 'Inspeksi Kelaikan Sistem Kelistrikan Kilang, Captive Power & Gas Turbine'],
            ['name' => 'PT Cikarang Listrindo Tbk', 'role' => 'Uji Proteksi Relai, Trafo Daya & Jaringan Distribusi Kawasan Industri Terpadu'],
            ['name' => 'PT Medco Power Indonesia', 'role' => 'Sertifikasi SLO Pembangkit Panas Bumi (PLTP) & Gardu Induk Swasta'],
            ['name' => 'PT Pupuk Indonesia (Persero)', 'role' => 'Sertifikasi Laik Operasi Sistem Kelistrikan Pabrik Pupuk & Instalasi Ex-Proof'],
            ['name' => 'PT Semen Indonesia (Persero) Tbk', 'role' => 'Inspeksi Tegangan Menengah 20 kV, Motor Tegangan Tinggi & Sistem Pembumian'],
            ['name' => 'PT Telkom Data Ekosistem (NeutraDC)', 'role' => 'Uji Kelaikan Operasi Kelistrikan Data Center Tier 3/4 & Sistem Genset Dinamis'],
            ['name' => 'PT Astra Agro Lestari Tbk', 'role' => 'Sertifikasi Kelaikan Operasi Pembangkit Listrik Biogas & Distribusi Pabrik Sawit'],
        ];"""

new_partners = """        $partners = [
            ['name' => 'PT Wijaya Karya (Persero) Tbk', 'role' => 'Pengkajian Teknis Kelaikan Fungsi Struktur Gedung Bertingkat & Fasilitas Infrastruktur'],
            ['name' => 'PT PP (Persero) Tbk', 'role' => 'Audit Keandalan Struktur, Fire Safety & Sertifikasi Laik Fungsi (SLF) Proyek High-Rise'],
            ['name' => 'PT Adhi Karya (Persero) Tbk', 'role' => 'Pemeriksaan Komisioning Utilitas MEP & Kelaikan Bangunan Stasiun serta Komersial'],
            ['name' => 'PT Waskita Karya (Persero) Tbk', 'role' => 'Uji NDT Struktur Beton & Sertifikasi Kelaikan Operasi Gedung Perkantoran Strategis'],
            ['name' => 'PT Ciputra Development Tbk', 'role' => 'Audit Kelaikan Fungsi Kawasan Terpadu, Mall Komersial, Perhotelan & Residensial'],
            ['name' => 'PT Pakuwon Jati Tbk', 'role' => 'Pengurusan & Perpanjangan SLF Berkala Superblock, Pusat Perbelanjaan & Apartemen'],
            ['name' => 'PT Agung Podomoro Land Tbk', 'role' => 'Asesmen Keandalan Proteksi Kebakaran Gedung Publik & Aksesibilitas Universal'],
            ['name' => 'PT Summarecon Agung Tbk', 'role' => 'Sertifikasi Kelaikan Bangunan Pusat Komersial, Sekolah & Gedung Pertemuan'],
            ['name' => 'PT Lippo Karawaci Tbk', 'role' => 'Audit Kelaikan Fasilitas Rumah Sakit Siloam & Menara Gedung Bertingkat Terintegrasi'],
            ['name' => 'PT BSD Tbk (Sinar Mas Land)', 'role' => 'Sertifikasi Kelaikan Fungsi Gedung Industri Hijau, Pusat Data & Office Park'],
        ];"""

text = text.replace(old_partners, new_partners)

# Update contact message
text = text.replace(
    "Tim Ahli Inspeksi Jasa SLO Indonesia",
    "Tim Pengkaji Teknis Jasa SLF Indonesia"
)

with open(controller_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated FrontController.php successfully for Jasa SLF!")
