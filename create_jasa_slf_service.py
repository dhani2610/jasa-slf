import os

service_dir = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\app\Services"
os.makedirs(service_dir, exist_ok=True)
service_file = os.path.join(service_dir, "JasaSlfSchemeService.php")

programs = [
    {
        "id": 1,
        "title": "Jasa SLF Bangunan Gedung Industri & Pabrik Manufaktur (Audit Struktur, Utilitas & Kelaikan Operasional)",
        "slug": "jasa-slf-bangunan-gedung-industri-pabrik",
        "level_code": "SLF-IND",
        "level_name": "Bangunan Gedung Industri / Industrial Facility",
        "badge": "Layanan Utama",
        "duration": "Kajian Cepat (7 - 14 Hari Kerja)",
        "method": "Inspeksi Visual, Uji NDT Hammer Test Struktur, Audit Hydrant & Uji Kelaikan Utilitas",
        "certification": "Sertifikat Laik Fungsi (SLF) Resmi Bangunan Industri Berbarcode Sah",
        "price_note": "Hubungi Tim Pengkaji Teknis SLF",
        "icon": "bi-buildings-fill",
        "short_description": "Layanan pengkajian teknis dan penerbitan Sertifikat Laik Fungsi (SLF) resmi untuk fasilitas pabrik manufaktur, gudang logistik, dan kawasan industri.",
        "overview": "Setiap bangunan gedung pabrik dan fasilitas industri wajib mengantongi Sertifikat Laik Fungsi (SLF) sebagai bukti bahwa bangunan telah memenuhi standar keandalan struktur, keselamatan kebakaran, kesehatan kerja, dan kenyamanan operasional. Layanan ini mencakup audit ketahanan struktur bentang lebar (portal baja/beton), uji NDT hammer test dan ketebalan baja ultrasonik, pengujian performa sistem pompa hydrant dan sprinkler, kelaikan ventilasi industri (HVAC), sistem pengolahan limbah (STP/WWTP), hingga jalur evakuasi darurat bagi ribuan tenaga kerja.",
        "target_audience": "Plant Manager, Industrial Engineering Manager, Project Director Kawasan Industri, Facility Management, dan Tim HSE Korporat",
        "curriculum": [
            "Modul 1: Kerangka Standar Teknis Keandalan Bangunan Gedung Industri Nasional",
            "Modul 2: Verifikasi Dokumen As-Built Drawing Struktur Portal, Denah Pabrik & Beban Mesin",
            "Modul 3: Uji Non-Destructive Testing (NDT) Hammer Test & Ultrasonic Thickness Gauge pada Rangka Baja",
            "Modul 4: Pengujian Tekanan & Debit Pompa Hydrant Utama, Jockey Pump, dan Jaringan Sprinkler",
            "Modul 5: Audit Kelistrikan Pabrik: Panel Hubung Bagi, Genset Cadangan & Sistem Pembumian Grounding",
            "Modul 6: Evaluasi Sistem Ventilasi Udara Mekanikal, Exhaust Fan & Pencahayaan Ruang Produksi",
            "Modul 7: Pemeriksaan Kelaikan Instalasi Pengolahan Air Limbah (STP) & Drainase Kawasan",
            "Modul 8: Penyusunan Dokumen Laporan Kajian Teknis & Pengurusan Penerbitan Sertifikat SLF Industri"
        ],
        "requirements": [
            "Salinan gambar As-Built Drawing Arsitektur, Struktur, dan MEP lengkap",
            "Dokumen legalitas kepemilikan bangunan / izin mendirikan bangunan awal",
            "Laporan pemeliharaan berkala struktur dan proteksi kebakaran tahunan",
            "Akses penuh tim pengkaji teknis ke seluruh area lantai produksi, atap, dan ruang mesin"
        ],
        "facilities": [
            "Sertifikat Laik Fungsi (SLF) Resmi dengan Validasi Barcode & Nomor Registrasi Sah",
            "Buku Laporan Kajian Teknis Keandalan Bangunan Gedung Komprehensif Ditandatangani Ahli",
            "Peta Temuan Anomali Struktur / Utilitas & Rekomendasi Mitigasi Prioritas",
            "Plat Logam Kelaikan Fungsi Gedung untuk Dipasang di Lobi / Gerbang Utama Fasilitas"
        ],
        "meta_title": "Jasa SLF Bangunan Gedung Industri & Pabrik Manufaktur | Sertifikat Laik Fungsi",
        "meta_description": "Layanan pengkajian teknis dan penerbitan Sertifikat Laik Fungsi (SLF) resmi untuk pabrik, gudang logistik, dan fasilitas industri. Audit struktur dan proteksi kebakaran terakreditasi."
    },
    {
        "id": 2,
        "title": "Jasa SLF Bangunan Gedung Komersial, Mall, Pusat Perbelanjaan & Perhotelan Bertingkat",
        "slug": "jasa-slf-bangunan-komersial-mall-hotel",
        "level_code": "SLF-KOM",
        "level_name": "Bangunan Komersial & Publik / Commercial High-Rise",
        "badge": "Prioritas Komersial",
        "duration": "Audit Terjadwal & Uji Komisioning",
        "method": "Audit Keselamatan Jiwa, Uji Smoke Management, Uji Lift & Eskalator, Audit Aksesibilitas",
        "certification": "Sertifikat Laik Fungsi (SLO/SLF) Resmi Gedung Komersial Berizin Sah",
        "price_note": "Hubungi Tim Pengkaji Teknis SLF",
        "icon": "bi-shop-window",
        "short_description": "Kajian teknis keandalan bangunan mall, pusat perbelanjaan, perhotelan, dan gedung komersial bertingkat tinggi guna memastikan keselamatan pengunjung dan kelaikan operasional.",
        "overview": "Gedung komersial dengan intensitas pengunjung tinggi menuntut standar keselamatan yang sangat ketat. Layanan Jasa SLF Komersial berfokus pada audit integritas kompartemenisasi api, waktu evakuasi tangga darurat bertekanan (pressurized stairwell), kelaikan sistem deteksi asap dan sprinkler otomatis, sertifikasi keselamatan lift penumpang dan eskalator, kelaikan kualitas udara dalam ruang (IAQ), ketersediaan fasilitas aksesibilitas ramah disabilitas, serta ketahanan struktur terhadap beban dinamis pengunjung.",
        "target_audience": "Building Manager Mall, General Manager Hotel, Direktur Operasional Pusat Perbelanjaan, Pengelola Gedung Bertingkat, dan Konsultan MEP",
        "curriculum": [
            "Modul 1: Standar Keandalan Gedung Komersial & Tata Bangunan Publik Terpadu",
            "Modul 2: Audit Sistem Keselamatan Jiwa: Tangga Darurat, Pintu Tahan Api & Smoke Damper",
            "Modul 3: Uji Aliran & Tekanan Air Sprinkler, Flow Switch, dan Integrasi Alarm Kebakaran Otomatis",
            "Modul 4: Inspeksi Mekanikal Transportasi Vertikal: Uji Safety Gear Lift Penumpang & Eskalator",
            "Modul 5: Pengukuran Tingkat Pencahayaan Alami / Buatan, Kebisingan & Kualitas Udara (IAQ)",
            "Modul 6: Evaluasi Fasilitas Aksesibilitas: Ramp Disabilitas, Lift Difabel & Toilet Khusus",
            "Modul 7: Pemeriksaan Sistem Penyalur Petir Sangkar Faraday & Pembumian Proteksi Gedung",
            "Modul 8: Sidang Evaluasi Teknis Bersama Tim Ahli Pengkaji & Rekomendasi Terbit SLF Komersial"
        ],
        "requirements": [
            "Gambar teknis arsitektur, denah rute evakuasi, dan skematik sistem tata udara HVAC",
            "Izin kelaikan operasi lift penumpang, gondola pembersih kaca, dan trafo kelistrikan",
            "Jadwal operasional gedung untuk penentuan waktu uji alarm dan sprinkler tanpa mengganggu pengunjung",
            "Penunjukan pendamping dari tim engineering building management"
        ],
        "facilities": [
            "Sertifikat Laik Fungsi (SLF) Resmi Gedung Komersial Berlaku 5 Tahun",
            "Dokumen Audit Keandalan Tata Bangunan, Struktur, dan Utilitas Lengkap",
            "Sertifikat Uji Komisioning Pemadam Kebakaran & Transportasi Vertikal",
            "Konsultasi Manajemen Perawatan Gedung (*Building Maintenance System*)"
        ],
        "meta_title": "Jasa SLF Gedung Komersial, Mall & Hotel Bertingkat | Pengkaji Teknis",
        "meta_description": "Jasa pengurusan dan perpanjangan Sertifikat Laik Fungsi (SLF) mall, hotel, dan gedung komersial bertingkat. Pemeriksaan struktur, lift, hydrant, dan proteksi kebakaran sah."
    },
    {
        "id": 3,
        "title": "Jasa SLF Fasilitas Rumah Sakit, Fasilitas Pelayanan Kesehatan & Gedung Khusus Laboratorium",
        "slug": "jasa-slf-fasilitas-rumah-sakit-kesehatan",
        "level_code": "SLF-RS",
        "level_name": "Fasilitas Kesehatan Khusus / Healthcare Facility",
        "badge": "Standar Medis",
        "duration": "Inspeksi Steril & Khusus",
        "method": "Audit Tata Udara Ruang Isolasi/Operasi (HEPA Filter), Uninterruptible Power, Uji Struktur",
        "certification": "Sertifikat Laik Fungsi (SLF) Resmi Fasilitas Rumah Sakit & Kesehatan",
        "price_note": "Hubungi Tim Pengkaji Teknis SLF",
        "icon": "bi-hospital-fill",
        "short_description": "Pengkajian kelaikan teknis komprehensif bagi bangunan rumah sakit, klinik utama, dan laboratorium medis sesuai standar keselamatan kesehatan dan keandalan sarana prasarana.",
        "overview": "Bangunan rumah sakit memiliki kompleksitas utilitas tertinggi dengan tuntutan keandalan suplai oksigen medis, tekanan udara terkontrol (ruang isolasi tekanan negatif & ruang bedah tekanan positif), catu daya cadangan tanpa jeda (UPS & genset darurat tersinkronisasi), proteksi radiasi ruang radiologi, serta pengelolaan limbah bahan berbahaya dan beracun (B3) medis. Jasa SLF Rumah Sakit memastikan seluruh sarana memenuhi kelaikan fungsi prima demi keselamatan pasien dan tenaga medis.",
        "target_audience": "Direktur Rumah Sakit, Kepala Instalasi Sarana Prasarana Rumah Sakit (IPSRS), Komite K3RS, Manajer Fasilitas Kesehatan, dan Pengembang Laboratorium",
        "curriculum": [
            "Modul 1: Standar Khusus Keandalan Bangunan Gedung Fasilitas Pelayanan Kesehatan",
            "Modul 2: Evaluasi Tata Ruang Fungsional: Zona Steril, Semi-Steril, Ruang Rawat Inap & Jalur Bed",
            "Modul 3: Audit Tata Udara Medis (HVAC AHU): Uji Differential Pressure, HEPA Filter & Penggantian Udara",
            "Modul 4: Uji Keandalan Kelistrikan Khusus Medis: Sistem IT Terisolasi, UPS Sentral & Genset Siaga",
            "Modul 5: Pemeriksaan Instalasi Gas Medik: Sentral Oksigen, Vacuum, Nitrous Oxide & Alarm Tekanan",
            "Modul 6: Kelaikan Instalasi Pengolahan Air Limbah Medis (IPAL B3 Cair) & Incinerator/TPS B3",
            "Modul 7: Keselamatan Proteksi Radiasi: Ketebalan Timbal (Pb) Ruang X-Ray, CT-Scan & MRI",
            "Modul 8: Penyusunan Laporan Kelayakan Fungsi Bangunan Rumah Sakit Menuju Sertifikat SLF Sah"
        ],
        "requirements": [
            "Master Plan Rumah Sakit dan gambar As-Built Drawing blok gedung pelayanan medis",
            "Hasil uji berkala emisi IPAL cair medis dan kalibrasi instalasi gas medik",
            "Log book pengujian rutin genset transfer switch otomatis (AMF/ATS)",
            "Izin operasional rumah sakit dan data kapasitas tempat tidur (*bed capacity*)"
        ],
        "facilities": [
            "Sertifikat Laik Fungsi (SLF) Rumah Sakit Resmi dengan Nomor Registrasi Sah",
            "Buku Laporan Audit Keandalan Sarana Prasarana Rumah Sakit (IPSRS Compliant)",
            "Matriks Rekomendasi Pengendalian Infeksi Lingkungan Bangunan (ICRA Terpadu)",
            "Dukungan Penuh dalam Pemenuhan Persyaratan Akreditasi Rumah Sakit Paripurna"
        ],
        "meta_title": "Jasa SLF Bangunan Rumah Sakit & Fasilitas Kesehatan | Sertifikat Laik Fungsi",
        "meta_description": "Layanan uji kelaikan teknis dan pengurusan Sertifikat Laik Fungsi (SLF) Rumah Sakit, klinik, dan laboratorium medis. Keandalan ruang bedah, isolasi, gas medis, dan IPAL teruji."
    },
    {
        "id": 4,
        "title": "Jasa SLF Bangunan Gedung Pusat Data (Data Center), Gedung Perkantoran & Menara Komunikasi",
        "slug": "jasa-slf-data-center-gedung-perkantoran",
        "level_code": "SLF-OFFICE",
        "level_name": "Pusat Data & Menara Komersial / Mission Critical",
        "badge": "Teknologi Tinggi",
        "duration": "Inspeksi Presisi & Non-Intrusif",
        "method": "Audit Kapasitas Beban Lantai Server, Uji Clean Agent Fire Suppression, Redundansi Daya",
        "certification": "Sertifikat Laik Fungsi (SLF) Resmi Gedung Pusat Data & Perkantoran",
        "price_note": "Hubungi Tim Pengkaji Teknis SLF",
        "icon": "bi-hdd-rack-fill",
        "short_description": "Sertifikasi kelaikan fungsi bangunan perkantoran modern, menara telekomunikasi, dan gedung data center Tier 3/4 dengan keandalan operasional 99.99%.",
        "overview": "Gedung pusat data (Data Center) dan gedung perkantoran cerdas modern membutuhkan kajian keandalan struktur khusus untuk menahan beban rak server berkepadatan tinggi (*raised floor loading*), sistem pemadam kebakaran gas bersih ramah lingkungan (*Clean Agent Fire Suppression - FM200/Novec 1230*), sistem pendingin presisi (PAC / Chiller Plant) redundan N+1/2N, sistem catu daya baterai UPS raksasa, serta proteksi ketat kebocoran air (*Water Leak Detection*). Jasa SLF menjamin gedung beroperasi andal tanpa risiko downtime.",
        "target_audience": "Data Center Infrastructure Manager, CTO/CIO Perusahaan Teknologi, Building Manager Gedung Perkantoran, dan Pengembang Smart Building",
        "curriculum": [
            "Modul 1: Standar Keandalan Bangunan Gedung Kategori Mission Critical & Data Center",
            "Modul 2: Verifikasi Beban Titik (Point Load) & Beban Terbagi Rata Lantai Ruang Server",
            "Modul 3: Uji Kinerja Sistem Pemadam Kebakaran Gas Bersih (Inergen / FM-200) & Room Integrity Test",
            "Modul 4: Audit Redundansi Sistem Pendingin Presisi (Precision Air Conditioning - PAC)",
            "Modul 5: Kelaikan Ruang Baterai UPS: Ventilasi Pembuangan Gas Hidrogen & Deteksi Kebakaran Termal",
            "Modul 6: Pemeriksaan Sistem Penyalur Petir Dinamis & Ekipotensial Grounding Sinyal Data (< 1 Ohm)",
            "Modul 7: Evaluasi Sistem Otomasi Gedung (Building Management System - BMS) & Keamanan Fisik",
            "Modul 8: Penerbitan Rekomendasi Teknis & Pengesahan Sertifikat SLF Gedung Data Center Resmi"
        ],
        "requirements": [
            "Gambar detail struktur pembebanan lantai ruang server dan layout rack data hall",
            "Spesifikasi sistem pemadam gas otomatis dan sertifikat uji tekanan tabung gas",
            "Data Single Line Diagram kelistrikan redundan dan skematik sistem pendingin",
            "Akses berizin khusus (security clearance) bagi tim auditor teknis bersertifikat"
        ],
        "facilities": [
            "Sertifikat Laik Fungsi (SLF) Gedung Data Center & Perkantoran Resmi Terakreditasi",
            "Laporan Uji Integritas Ruangan (Enclosure Integrity Test Certificate)",
            "Audit Peta Jalur Kabel Data, Proteksi Surja dan Pembumian Komputasi Presisi",
            "Jaminan Kerahasiaan Data Klien melalui Non-Disclosure Agreement (NDA) Ketat"
        ],
        "meta_title": "Jasa SLF Bangunan Data Center & Gedung Perkantoran Bertingkat",
        "meta_description": "Layanan uji kelaikan dan penerbitan Sertifikat Laik Fungsi (SLF) Data Center dan gedung perkantoran. Audit kekuatan lantai beban rak, clean agent fire suppression, dan MEP."
    },
    {
        "id": 5,
        "title": "Training & Audit Keandalan Struktur Bangunan Gedung (NDT Hammer Test, Core Drill & Analisis Gempa)",
        "slug": "training-audit-keandalan-struktur-bangunan-gedung",
        "level_code": "TRAIN-STRUKTUR",
        "level_name": "Audit Struktur / Certified Structural Auditor",
        "badge": "Keahlian Teknik",
        "duration": "4 Hari (32 Jam Pelajaran)",
        "method": "Teori Standar Beton/Baja, Praktik Alat NDT Schmidt Hammer, UPV, dan Pemodelan ETABS",
        "certification": "Sertifikat Ahli Audit Keandalan Struktur Bangunan Gedung Terakreditasi",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-cone-striped",
        "short_description": "Pelatihan dan sertifikasi praktis pengujian non-destruktif struktur beton/baja, pengukuran retak, uji kekerasan, pemindaian tulangan rebar scan, dan analisis ketahanan gempa gedung.",
        "overview": "Struktur adalah pilar terpenting dalam kelaikan fungsi bangunan. Program pelatihan ini melatih para insinyur sipil dan praktisi konstruksi menguasai metodologi asesmen kondisi eksisting gedung, teknik pengoperasian alat uji non-destruktif (Rebound Hammer, Ultrasonic Pulse Velocity, Rebar Locator), uji destruktif terbatas (Core Drill & Uji Kuat Tekan Laboratorium), pengujian lendutan balok, serta simulasi ulang kapasitas struktur terhadap beban gempa menggunakan software analisis teknik modern.",
        "target_audience": "Insinyur Sipil, Manajer Proyek Konstruksi, Konsultan Struktur, Structural Inspector, Auditor Bangunan, dan Pengawas Lapangan",
        "curriculum": [
            "Modul 1: Prinsip Evaluasi Keandalan Struktur Bangunan Gedung Eksisting & Standar SNI Gempa",
            "Modul 2: Metodologi Pengujian Non-Destruktif (NDT): Schmidt Rebound Hammer Test Sesuai Standar",
            "Modul 3: Ultrasonic Pulse Velocity (UPV) Test untuk Menentukan Homogenitas & Retak Internal Beton",
            "Modul 4: Penggunaan Rebar Scanner / Ferroscan untuk Memetakan Jumlah, Diameter & Selimut Tulangan",
            "Modul 5: Prosedur Pengambilan Sampel Core Drill, Penambalan Grouting & Uji Kuat Tekan Lab",
            "Modul 6: Identifikasi Pola Retak (Struktural vs Non-Struktural), Karbonasi & Korosi Tulangan Baja",
            "Modul 7: Pemodelan Komputasi Beban Gempa & Analisis Rasio Kapasitas Elemen (Demand-to-Capacity Ratio)",
            "Modul 8: Penyusunan Dokumen Kajian Teknis Keandalan Struktur sebagai Syarat Mutlak Penerbitan SLF"
        ],
        "requirements": [
            "Pendidikan minimal D3/S1 Teknik Sipil atau memiliki pengalaman kerja di bidang pengawasan struktur",
            "Memahami dasar-dasar mekanika teknik, perancangan beton bertulang, dan struktur baja",
            "Membawa laptop untuk sesi pengolahan data uji NDT dan pemodelan evaluasi struktur"
        ],
        "facilities": [
            "Sertifikat Kompetensi Auditor Keandalan Struktur Bangunan Gedung Resmi",
            "Modul Teknis Lengkap Metode Uji NDT & Formula Koreksi Nilai Hammer Test",
            "Spreadsheet Otomatis Kalkulasi Karbonasi, Homogenitas UPV & Rekapitulasi Tulangan",
            "Sesi Praktik Lapangan Menggunakan Instrumen Uji NDT Digital Terkalibrasi"
        ],
        "meta_title": "Training & Audit Keandalan Struktur Bangunan Gedung (NDT & Gempa)",
        "meta_description": "Pelatihan audit keandalan struktur bangunan gedung, uji NDT hammer test, UPV, rebar scan tulangan, dan analisis beban gempa untuk syarat penerbitan Sertifikat Laik Fungsi (SLF)."
    },
    {
        "id": 6,
        "title": "Training & Asesmen Proteksi Kebakaran Gedung (Fire Safety Audit, Hydrant, Sprinkler & Smoke Control)",
        "slug": "training-asesmen-proteksi-kebakaran-gedung",
        "level_code": "TRAIN-FIRE",
        "level_name": "Proteksi Kebakaran / Certified Fire Protection Specialist",
        "badge": "Keselamatan Jiwa",
        "duration": "3 Hari (24 Jam Pelajaran)",
        "method": "Teori Standar NFPA/SNI, Uji Aliran Pompa Kebakaran (Flow Test), & Simulasi Smoke Damper",
        "certification": "Sertifikat Asesor Sistem Proteksi Kebakaran Bangunan Gedung",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-fire",
        "short_description": "Pembinaan intensif audit sistem keselamatan kebakaran gedung, pengujian debit/tekanan pompa hydrant, keandalan sprinkler otomatis, pintu darurat, dan manajemen asap.",
        "overview": "Kebakaran merupakan ancaman paling mematikan pada bangunan gedung bertingkat. Pelatihan ini membekali peserta dengan keterampilan melakukan audit menyeluruh terhadap sistem proteksi kebakaran pasif (ketahanan api dinding, pintu darurat, sealing penetrasi kabel) dan proteksi kebakaran aktif (Fire Hydrant System, Automatic Fire Sprinkler, Fire Alarm & Detection, Clean Agent Gas). Peserta dilatih menguji kurva performa pompa kebakaran (Fire Pump Performance Curve) dan memastikan gedung aman bagi evakuasi penghuni.",
        "target_audience": "Fire Safety Officer, Safety Manager Gedung, Kepala Engineering Hotel/Mall, Konsultan Proteksi Kebakaran, dan Tim Tanggap Darurat Perusahaan",
        "curriculum": [
            "Modul 1: Filosofi Keselamatan Jiwa (Life Safety) & Standar Proteksi Kebakaran Bangunan Gedung",
            "Modul 2: Inspeksi Sarana Penyelamatan Jiwa: Tangga Darurat, Lebar Koridor & Lampu Emergency/Exit",
            "Modul 3: Evaluasi Kompartemenisasi Bangunan & Uji Pintu Kebakaran (Fire Rated Door)",
            "Modul 4: Pengujian Pompa Kebakaran (Electric, Diesel, Jockey): Uji Tanpa Beban, 100% Flow & 150% Peak",
            "Modul 5: Pemeriksaan Jaringan Pipa Hydrant, Pillar Hydrant, Box Hydrant & Uji Tekanan Nozzle",
            "Modul 6: Uji Kinerja Sistem Sprinkler Otomatis: Alarm Check Valve, Water Motor Gong & Inspector Test Connection",
            "Modul 7: Pengujian Integrasi Fire Alarm (Smoke/Heat Detector, Manual Call Point) dengan Sistem Lift & HVAC",
            "Modul 8: Penyusunan Laporan Audit Fire Safety Sesuai Checklist Resmi Standar Kelaikan Fungsi (SLF)"
        ],
        "requirements": [
            "Pendidikan minimal SMK Teknik / D3 / S1 atau staf HSE / pengelola fasilitas gedung",
            "Memahami prinsip dasar sistem pemadam kebakaran dan keselamatan kerja umum",
            "Membawa perlengkapan safety (sepatu kerja, helm pelindung) untuk sesi praktik pompa kebakaran"
        ],
        "facilities": [
            "Sertifikat Asesor Sistem Proteksi Kebakaran Bangunan Gedung Terakreditasi",
            "Template Standar Formulir Inspeksi Pompa Kebakaran (Hydrant Flow Test Sheet Excel)",
            "Buku Pedoman Standar Jarak Penempatan Sprinkler & Detektor Kebakaran SNI/NFPA",
            "Simulasi Pengujian Langsung pada Instalasi Pompa Pemadam Kebakaran Gedung Nyata"
        ],
        "meta_title": "Training & Asesmen Proteksi Kebakaran Gedung | Fire Safety SLF",
        "meta_description": "Pelatihan audit sistem proteksi kebakaran gedung bertingkat, uji debit pompa hydrant, keandalan sprinkler, tangga darurat, dan alarm kebakaran untuk pemenuhan syarat SLF."
    },
    {
        "id": 7,
        "title": "Training Mekanikal, Elektrikal & Plumbing (MEP) Kelaikan Fungsi Bangunan Gedung Bertingkat",
        "slug": "training-mep-kelaikan-fungsi-bangunan-gedung",
        "level_code": "TRAIN-MEP",
        "level_name": "Audit Utilitas / Certified MEP Inspector",
        "badge": "Utilitas Gedung",
        "duration": "3 Hari (24 Jam Pelajaran)",
        "method": "Inspeksi Sistem Distribusi Daya, Pengukuran Kualitas Air Bersih/Limbah, & Kinerja HVAC",
        "certification": "Sertifikat Auditor Mekanikal, Elektrikal & Plumbing Gedung Bertingkat",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-wrench-adjustable-circle-fill",
        "short_description": "Pelatihan komprehensif inspeksi dan pengujian kelaikan sistem utilitas mekanikal, elektrikal, tata udara, penyediaan air bersih, pengolahan air limbah, dan penyalur petir gedung.",
        "overview": "Keandalan fungsi utilitas MEP menentukan kenyamanan, kesehatan, dan kelangsungan operasional gedung setiap hari. Program ini melatih peserta mengevaluasi kapasitas trafo, panel distribusi utama, kontinuitas sistem genset darurat, sistem pembumian dan penyalur petir, kelaikan lift dan gondola, efisiensi sistem tata udara (Chiller/VRV), sistem pemipaan air bersih, serta instalasi pengolahan air limbah (STP) agar memenuhi baku mutu lingkungan hidup.",
        "target_audience": "MEP Engineer, Maintenance Supervisor, Facility Engineer Gedung Bertingkat, Kontraktor Instalatur Mekanikal-Elektrikal, dan Quality Inspector",
        "curriculum": [
            "Modul 1: Kriteria Keandalan Sistem Utilitas Bangunan Gedung dalam Penilaian Kelaikan Fungsi",
            "Modul 2: Inspeksi Sistem Elektrikal: Panel LVMDP, Distribusi Daya, Keseimbangan Beban & Drop Tegangan",
            "Modul 3: Uji Pembumian (Grounding System) dan Kelaikan Instalasi Penyalur Petir Eksternal/Internal",
            "Modul 4: Kelaikan Genset Darurat: Uji Transfer Otomatis AMF/ATS, Kesiapan Bahan Bakar & Peredam Bising",
            "Modul 5: Audit Sistem Tata Udara (HVAC): Efisiensi Chiller, Aliran Udara Duktus & Distribusi Suhu Ruang",
            "Modul 6: Pemeriksaan Sistem Transportasi Vertikal: Sertifikasi Kelaikan Lift Penumpang, Barang & Eskalator",
            "Modul 7: Sistem Plumbing: Uji Tekanan Pipa Air Bersih, Kualitas Air Minum & Kinerja Aerasi Bak IPAL/STP",
            "Modul 8: Penyusunan Lembar Checklist MEP & Laporan Komisioning untuk Permohonan Sertifikat SLF"
        ],
        "requirements": [
            "Pendidikan minimal SMK Listrik/Mesin, D3/S1 Teknik Elektro / Mesin / Fisika Teknik",
            "Pengalaman kerja di bidang operasi dan pemeliharaan utilitas gedung bertingkat",
            "Membawa alat tulis dan kalkulator teknik untuk sesi perhitungan beban utilitas"
        ],
        "facilities": [
            "Sertifikat Auditor Mekanikal, Elektrikal & Plumbing (MEP) Bangunan Gedung Resmi",
            "Buku Pedoman Teknis Pemeriksaan Berkala Utilitas Gedung Berstandar Nasional",
            "Paket Template Checklist Uji Komisioning MEP Siap Cetak & Pakai",
            "Bimbingan Studi Kasus Penanganan Kegagalan Utilitas Gedung Bertingkat Tinggi"
        ],
        "meta_title": "Training MEP Kelaikan Fungsi Bangunan Gedung Bertingkat | Audit Utilitas",
        "meta_description": "Pelatihan inspeksi dan komisioning sistem Mekanikal, Elektrikal & Plumbing (MEP) gedung bertingkat. Pemeriksaan genset, lift, tata udara HVAC, sanitasi, dan penyalur petir SLF."
    },
    {
        "id": 8,
        "title": "Training Tata Kelola Pemeliharaan, Perawatan Bangunan (Building Maintenance) & Perpanjangan SLF",
        "slug": "training-tata-kelola-pemeliharaan-bangunan-slf",
        "level_code": "TRAIN-MAINT",
        "level_name": "Manajemen Fasilitas / Building Maintenance & SLF Management",
        "badge": "Tata Kelola Gedung",
        "duration": "2 Hari (16 Jam Pelajaran)",
        "method": "Studi Kebijakan Pemeliharaan, Penyusunan Manual Perawatan Gedung, & Prosedur Resertifikasi SLF",
        "certification": "Sertifikat Manajer Pemeliharaan & Kelaikan Bangunan Gedung Terakreditasi",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-clipboard2-check-fill",
        "short_description": "Pembekalan strategis penyusunan rencana pemeliharaan preventif, log book berkala, audit kelaikan arsitektur/struktur, serta tata cara perpanjangan berkala Sertifikat Laik Fungsi (SLF).",
        "overview": "Masa berlaku Sertifikat Laik Fungsi (SLF) dibatasi secara periodik (5 tahun untuk bangunan umum dan 20 tahun untuk rumah tinggal tunggal) dan wajib diperpanjang sebelum masa berlakunya berakhir. Pelatihan ini memandu pimpinan pengelola gedung menyusun Rencana Kerja Pemeliharaan dan Perawatan Bangunan Gedung (RKPPBG), mengorganisir log book pencatatan kerusakan, mengelola tim teknisi in-house, dan menyiapkan dokumen administrasi serta teknis resertifikasi SLF tepat waktu tanpa kendala birokrasi.",
        "target_audience": "Property Manager, Head of Facility Management, Building Maintenance Superintendent, Legal Officer Properti, dan Pemilik Aset Gedung",
        "curriculum": [
            "Modul 1: Kerangka Hukum & Kebijakan Tata Kelola Pemeliharaan Bangunan Gedung Berkelanjutan",
            "Modul 2: Penyusunan Dokumen Manual Operasi, Pemeliharaan, dan Perawatan Bangunan Gedung",
            "Modul 3: Manajemen Pemeliharaan Arsitektur: Fasad Kaca, Dinding Luar, Waterproofing Atap & Kusen",
            "Modul 4: Pemantauan Rutin Deformasi Struktur, Perambatan Retak, dan Korosi Elemen Eksterior",
            "Modul 5: Manajemen Jadwal Kalibrasi Alat Ukur Utilitas & Perpanjangan Izin Operasi Peralatan K3",
            "Modul 6: Sistem Pelaporan Digital Riwayat Pemeliharaan Gedung (*Computerized Maintenance Management*)",
            "Modul 7: Prosedur Lengkap Pengajuan Perpanjangan Sertifikat Laik Fungsi (SLF) Gedung Eksisting",
            "Modul 8: Strategi Lolos Sidang Evaluasi Teknis Pengkaji Bangunan Tanpa Catatan Perbaikan Berat"
        ],
        "requirements": [
            "Pengelola gedung, manajer properti, staf legal korporasi, atau penanggung jawab fasilitas",
            "Membawa dokumen contoh jadwal perawatan fasilitas gedung yang sedang dikelola",
            "Komitmen mengikuti seluruh sesi diskusi studi kasus tata kelola gedung"
        ],
        "facilities": [
            "Sertifikat Manajer Pemeliharaan & Kelaikan Bangunan Gedung Terakreditasi",
            "Buku Panduan Standar Penyusunan Manual Pemeliharaan Bangunan Gedung Siap Adaptasi",
            "Template Formulir Log Book Pemeliharaan Berkala Struktur, Arsitektur, dan Utilitas",
            "Konsultasi Pra-Audit Resertifikasi SLF bersama Tim Ahli Pengkaji Teknis Bangunan"
        ],
        "meta_title": "Training Pemeliharaan Bangunan Gedung & Perpanjangan SLF Berkala",
        "meta_description": "Pelatihan tata kelola pemeliharaan gedung (building maintenance), manual perawatan arsitektur/struktur, dan panduan lengkap pengurusan perpanjangan Sertifikat Laik Fungsi (SLF)."
    }
]

slf_topics = [
    "Panduan Lengkap Sertifikat Laik Fungsi (SLF) Bangunan Gedung & Standar Teknis Nasional",
    "Uji Keandalan Struktur Beton & Rangka Baja Bangunan Pabrik Industri",
    "Uji Keandalan Struktur Bangunan Gedung Bertingkat Menggunakan NDT Hammer Test",
    "Tata Cara Pengurusan, Pemeriksaan & Penerbitan Sertifikat Laik Fungsi (SLF) Sah",
    "Audit Sistem Proteksi Kebakaran Aktif Hydrant, Sprinkler & Pompa Pemadam Gedung",
    "Evaluasi Kompartemenisasi Kebakaran, Pintu Tahan Api & Tangga Darurat Bertekanan",
    "Audit Keselamatan Sistem Mekanikal Transportasi Vertikal Lift Penumpang & Eskalator",
    "Pemeriksaan Kelaikan Sistem Kelistrikan Gedung, Panel LVMDP & Genset Darurat",
    "Pengujian Kualitas Udara Dalam Ruang (IAQ), Sistem Ventilasi & Tata Udara HVAC",
    "Audit Keandalan Sistem Sanitasi, Distribusi Air Bersih & Pengolahan Air Limbah STP",
    "Pemeriksaan Kelaikan Sistem Penyalur Petir & Pembumian Proteksi Bangunan Gedung",
    "Evaluasi Kemudahan Aksesibilitas Universal bagi Penyandang Disabilitas di Gedung Publik",
    "Uji Karakteristik Getaran Mesin, Pondasi Dinamis & Beban Gempa Bangunan Gedung",
    "Manajemen Pemeliharaan Fasad Gedung Tinggi, Waterproofing & Uji Kebocoran Kaca",
    "Sertifikasi Laik Fungsi (SLF) Rumah Sakit, Ruang Operasi Steril & Pengelolaan Limbah Medis",
    "Sertifikasi Laik Fungsi (SLF) Bangunan Pusat Data (Data Center) & Gedung Perkantoran",
    "Sertifikasi Laik Fungsi (SLF) Mall, Pusat Perbelanjaan & Hotel Bertingkat Modern",
    "Inspeksi Geoteknik, Penurunan Pondasi (Settlement) & Daya Dukung Tanah Gedung",
    "Penyusunan Gambar As-Built Drawing Arsitektur, Struktur & MEP untuk Syarat SLF",
    "Uji Integritas Ruangan (Enclosure Integrity Test) Sistem Pemadam Gas Clean Agent",
    "Mitigasi Bahaya Keruntuhan Bangunan, Deteksi Retak Struktur & Injeksi Grouting Epoxy",
    "Standar Tata Ruang Luar Gedung, Koefisien Dasar Bangunan (KDB) & Ruang Terbuka Hijau",
    "Evaluasi Kenyamanan Termal, Tingkat Pencahayaan Alami (Lux) & Efisiensi Energi Gedung",
    "Inspeksi Kelaikan Gondola Pembersih Kaca Fasad & Jalur Keselamatan Kerja Atap",
    "Uji Komisioning Terpadu (Integrated Commissioning Test) Sarana Keselamatan Gedung",
    "Prosedur Perpanjangan Berkala Sertifikat Laik Fungsi (SLF) Bangunan Gedung Eksisting",
    "Pemeriksaan Ketahanan Api Material Pelapis Dinding, Plafon & Karpet Koridor Evakuasi",
    "Audit Kelaikan Instalasi Gas Medis & Sistem Pembuangan Gas Anestesi Ruang Rawat",
    "Kelaikan Struktur Bentang Lebar Gudang Logistik & Kapasitas Beban Lantai Racking",
    "Standardisasi Jalur Pemandu Tunanetra (Guiding Blocks) & Fasilitas Ramah Lansia",
    "Kajian Forensik Kegagalan Bangunan Gedung, Analisis Korosi Rebar & Penyelamatan Aset",
    "Audit Kelaikan Bangunan Heritage, Cagar Budaya & Konservasi Arsitektur Bersejarah",
    "Uji Kinerja Smoke Extraction Fan & Damper Pengendali Asap Kebakaran Gedung",
    "Pemeriksaan Sistem Drainase Halaman, Sumur Resapan & Kolam Retensi Pengendali Banjir",
    "Sertifikasi Laik Fungsi (SLF) Gedung Sekolah, Kampus Universitas & Fasilitas Edukasi",
    "Kelaikan Fungsi Bangunan Apartemen, Rumah Susun & Tata Kelola Hunian Vertikal",
    "Pemeriksaan Ruang Penyimpanan Bahan Berbahaya (B3), Tanggul Pengaman & Spill Kit",
    "Penyusunan Rencana Kerja Pemeliharaan dan Perawatan Bangunan Gedung (RKPPBG)",
    "Penyusunan Dokumen Laporan Kajian Teknis Komprehensif Tenaga Ahli Pengkaji SLF",
    "Peta Jalan Keandalan Bangunan Gedung Menuju Zero Building Disaster & Zero Accident"
]

prefixes = [
    "Training Jasa SLF: ",
    "Jasa SLF Training: ",
    "Jasa SLF: ",
    "Training Sertifikat Laik Fungsi (SLF): ",
    "Jasa Pengurusan SLF: "
]

titles_200 = []
for i in range(200):
    topic = slf_topics[i % len(slf_topics)]
    pfx = prefixes[i % len(prefixes)]
    cycle = i // len(slf_topics)
    if cycle == 0:
        t = f"{pfx}{topic} di {{region}}"
    elif cycle == 1:
        t = f"{pfx}{topic} (Fokus Bangunan Industri & Komersial) di {{region}}"
    elif cycle == 2:
        t = f"{pfx}{topic} (Standar Audit Struktur & Proteksi Jiwa) di {{region}}"
    elif cycle == 3:
        t = f"{pfx}{topic} (Panduan Kajian Teknis & Resertifikasi) di {{region}}"
    else:
        t = f"{pfx}{topic} (Implementasi Keandalan Utilitas Bangunan) di {{region}}"
    titles_200.append(t)

service_code = """<?php

namespace App\\Services;

use Illuminate\\Support\\Str;

class JasaSlfSchemeService
{
    public static function getMasterPrograms(): array
    {
        return [
"""

for p in programs:
    curriculum_php = ",\n".join([f"                    '{c}'" for c in p["curriculum"]])
    requirements_php = ",\n".join([f"                    '{r}'" for r in p["requirements"]])
    facilities_php = ",\n".join([f"                    '{f}'" for f in p["facilities"]])
    
    service_code += f"""            [
                'id' => {p["id"]},
                'title' => '{p["title"]}',
                'slug' => '{p["slug"]}',
                'level_code' => '{p["level_code"]}',
                'level_name' => '{p["level_name"]}',
                'badge' => '{p["badge"]}',
                'duration' => '{p["duration"]}',
                'method' => '{p["method"]}',
                'certification' => '{p["certification"]}',
                'price_note' => '{p["price_note"]}',
                'icon' => '{p["icon"]}',
                'short_description' => '{p["short_description"]}',
                'overview' => '{p["overview"]}',
                'target_audience' => '{p["target_audience"]}',
                'curriculum' => [
{curriculum_php}
                ],
                'requirements' => [
{requirements_php}
                ],
                'facilities' => [
{facilities_php}
                ],
                'meta_title' => '{p["meta_title"]}',
                'meta_description' => '{p["meta_description"]}'
            ],
"""

service_code += """        ];
    }

    public static function getAllPrograms(): array
    {
        return self::getMasterPrograms();
    }

    public static function getProgramBySlug(string $slug): ?array
    {
        foreach (self::getMasterPrograms() as $prog) {
            if ($prog['slug'] === $slug) {
                return $prog;
            }
        }
        return null;
    }

    public static function get200ArticleTitles(): array
    {
        return [
"""

for t in titles_200:
    clean_t = t.replace('"', '\\"')
    service_code += f'            "{clean_t}",\n'

service_code += """        ];
    }

    public static function generateDeepArticle(string $rawTitle, string $regionName = 'Indonesia'): array
    {
        $formattedTitle = str_replace('{region}', $regionName, $rawTitle);
        $slug = Str::slug($formattedTitle);

        $chapters = [
            [
                'title' => 'Landasan Regulasi Keselamatan, Keandalan & Standar Kelaikan Fungsi Bangunan Gedung',
                'desc' => 'Kerangka acuan hukum dan persyaratan teknis kelaikan fungsi bangunan gedung nasional, prinsip keselamatan struktur, proteksi kebakaran, kesehatan lingkungan, serta kenyamanan dan kemudahan aksesibilitas publik.'
            ],
            [
                'title' => 'Verifikasi Dokumen As-Built Drawing Arsitektur, Struktur & Skematik Utilitas Gedung',
                'desc' => 'Pemeriksaan kesesuaian gambar terlaksana (as-built drawing) dengan kondisi fisik lapangan mencakup denah tata ruang, dimensi elemen struktur balok-kolom, kapasitas lantai beban, dan skematik sistem MEP.'
            ],
            [
                'title' => 'Pemeriksaan Keandalan Struktur Beton & Baja: Non-Destructive Testing (NDT) Hammer Test & UPV',
                'desc' => 'Metodologi pengujian non-destruktif menggunakan Schmidt Rebound Hammer dan Ultrasonic Pulse Velocity untuk memetakan kekuatan tekan beton, mendeteksi keropos internal, dan uji ketebalan baja.'
            ],
            [
                'title' => 'Uji Kekuatan Bahan Karbonasi, Uji Coring Beton & Analisis Ketahanan Beban Gempa',
                'desc' => 'Uji kedalaman penetrasi karbonasi dengan larutan fenolftalein, pengambilan sampel inti beton terbatas, serta evaluasi rasio kapasitas elemen struktur terhadap bahaya gempa bumi.'
            ],
            [
                'title' => 'Pemeriksaan Geoteknik, Pondasi Dangkal / Tiang Pancang & Pemantauan Penurunan (Settlement)',
                'desc' => 'Inspeksi stabilitas tanah dasar, evaluasi penurunan diferensial antar kolom pendukung, kondisi dinding penahan tanah (retaining wall), dan integritas pile cap pondasi gedung.'
            ],
            [
                'title' => 'Audit Sistem Keselamatan & Proteksi Kebakaran Aktif: Hydrant, Sprinkler & Pompa Kebakaran',
                'desc' => 'Pengujian performa debit dan tekanan pompa pemadam kebakaran (electric, diesel, jockey pump), uji pancaran hidran gedung, serta keandalan jaringan sprinkler otomatis sesuai standar proteksi api.'
            ],
            [
                'title' => 'Evaluasi Sistem Proteksi Kebakaran Pasif: Kompartemenisasi, Smoke Barrier & Tangga Darurat',
                'desc' => 'Pemeriksaan ketahanan api dinding pemisah, pintu darurat tahan api (fire door) dengan panic bar, kekedapan smoke damper, serta tekanan udara positif pada tangga evakuasi darurat.'
            ],
            [
                'title' => 'Pengujian Sistem Deteksi, Alarm Kebakaran Otomatis & Sistem Pengendalian Asap (Smoke Exhaust)',
                'desc' => 'Uji sensitivitas smoke/heat detector, verifikasi panel kontrol alarm kebakaran utama (MCFA), keterhubungan alarm dengan pelepasan kunci pintu otomatis, serta kinerja kipas ekstraksi asap.'
            ],
            [
                'title' => 'Pemeriksaan Sistem Kelistrikan Gedung, Panel Distribusi LVMDP, Genset Emergency & Grounding',
                'desc' => 'Pengujian kelaikan panel hubung bagi, kontinuitas sistem catu daya darurat otomatis saat pemadaman listrik PLN, uji isolasi kabel daya, dan pengukuran tahanan pembumian kelistrikan.'
            ],
            [
                'title' => 'Uji Kelaikan Sistem Mekanikal Transportasi Vertikal: Lift Penumpang, Lift Barang & Eskalator',
                'desc' => 'Inspeksi perangkat keselamatan rem darurat (safety gear), sensor pintu, sistem interkom darurat car lift, uji beban overspeed governor, dan sertifikasi kelaikan operasi lift penumpang.'
            ],
            [
                'title' => 'Evaluasi Kualitas Penghawaan (HVAC), Ventilasi Ruang & Standar Pertukaran Udara Bersih (ACH)',
                'desc' => 'Pengukuran debit aliran udara masuk dan keluar, filterisasi udara AHU, kecukupan ventilasi alami/mekanikal, dan penghitungan laju pertukaran udara per jam demi kesehatan penghuni.'
            ],
            [
                'title' => 'Audit Sistem Sanitasi, Distribusi Air Bersih, Pengolahan Air Limbah (STP) & Drainase Tapak',
                'desc' => 'Pemeriksaan mutu air bersih, uji tekanan pipa distribusi air, kapasitas dan efisiensi aerasi Sewage Treatment Plant (STP), serta kelaikan sumur resapan pencegah genangan banjir kawasan.'
            ],
            [
                'title' => 'Uji Kelaikan Proteksi Petir Gedung (Lightning Protection) & Pengukuran Pembumian Khusus',
                'desc' => 'Verifikasi radius sangkar proteksi sambaran petir eksternal, ketahanan klem hantaran penurunan (down conductor), dan pengukuran nilai tahanan pembumian khusus petir di bawah 1 Ohm.'
            ],
            [
                'title' => 'Evaluasi Kemudahan & Aksesibilitas Universal: Ramp Disabilitas, Toilet Aksesibel & Jalur Pemandu',
                'desc' => 'Inspeksi kemiringan ramp akses disabilitas (< 1:12), lebar pintu ramah kursi roda, pegangan rambat (handrail), toilet khusus difabel, serta kelengkapan guiding blocks bagi tunanetra.'
            ],
            [
                'title' => 'Uji Kinerja Akustik, Insulasi Suara & Tingkat Pencahayaan Alami / Buatan (Lux Meter)',
                'desc' => 'Pengukuran intensitas cahaya pada area kerja dan koridor sesuai peruntukan ruang, serta pengujian isolasi suara dari kebisingan luar gedung untuk menjamin kenyamanan penghuni.'
            ],
            [
                'title' => 'Analisis Hasil Uji Komisioning, Penyusunan Laporan Kajian Teknis & Matriks Rekomendasi Perbaikan',
                'desc' => 'Pengolahan seluruh data ukur lapangan oleh tim ahli pengkaji teknis berlisensi, identifikasi derajat kerusakan atau deviasi standar, serta penyusunan corrective action plan prioritas.'
            ],
            [
                'title' => 'Proses Penerbitan Sertifikat Laik Fungsi (SLF) Resmi, Validasi Barcode & Pengesahan Sah',
                'desc' => 'Tahapan pengesahan dokumen kajian teknis, pencatatan nomor register resmi keandalan bangunan gedung, dan penerbitan plakat / sertifikat fisik SLF berkekuatan hukum penuh.'
            ],
            [
                'title' => 'Panduan Tata Kelola Pemeliharaan Preventif Bangunan Gedung & Prosedur Perpanjangan SLF Berkala',
                'desc' => 'Penyusunan Rencana Kerja Pemeliharaan dan Perawatan Bangunan Gedung (RKPPBG), jadwal inspeksi rutin mandiri, pencatatan log book gedung, dan tata cara resertifikasi SLF sebelum kedaluwarsa.'
            ]
        ];

        $content = "<h2>Panduan Komprehensif: {$formattedTitle}</h2>\\n\\n";
        $content .= "<p>Dalam lanskap pembangunan dan pengelolaan fasilitas modern di wilayah {$regionName}, keberadaan bangunan gedung industri, kawasan pergudangan, gedung komersial, perhotelan, hingga fasilitas pelayanan publik menuntut jaminan keandalan fisik yang mutlak. Pelaksanaan <strong>{$formattedTitle}</strong> di area {$regionName} merupakan langkah fundamental bagi para pemilik gedung, pengelola properti, dan jajaran manajemen korporat dalam membuktikan bahwa aset fisik yang ditempati telah teruji secara teknis memenuhi empat pilar keandalan bangunan gedung: keselamatan struktur, proteksi kebakaran, kesehatan sanitasi, serta kemudahan aksesibilitas publik.</p>\\n\\n";
        $content .= "<p>Sertifikat Laik Fungsi (SLF) adalah sertifikat resmi berkekuatan hukum yang menyatakan bahwa suatu bangunan gedung telah selesai dibangun dan memenuhi seluruh persyaratan teknis kelaikan fungsi sebelum dapat dimanfaatkan secara legal dan aman. Dokumen kajian panduan ini menyajikan delapan belas bab analisis teknis komprehensif yang dirancang sebagai rujukan utama tim pengkaji teknis, structural engineer, fire protection specialist, building maintenance manager, dan auditor keselamatan fasilitas di {$regionName}.</p>\\n\\n";

        foreach ($chapters as $index => $chap) {
            $num = $index + 1;
            $content .= "<h3>Bab {$num}: {$chap['title']}</h3>\\n";
            $content .= "<p><strong>Fokus Bahasan Teknis:</strong> {$chap['desc']}</p>\\n";

            $content .= "<p>Penerapan audit keandalan teknis pada bab ini di area operasional {$regionName} berfokus pada pengujian presisi di lapangan guna mendeteksi potensi anomali tersembunyi yang dapat mengancam keselamatan penghuni gedung. Setiap kegagalan fungsi struktur maupun sarana proteksi kebakaran yang tidak teridentifikasi dapat berakibat fatal, menimbulkan keruntuhan elemen konstruksi, menjebak penghuni saat kebakaran, hingga menyebabkan pembatalan polis asuransi dan penghentian izin operasional fasilitas.</p>\\n";

            $content .= "<h4>Metodologi Pemeriksaan & Langkah Kerja Standar Lapangan:</h4>\\n";
            $content .= "<ul>\\n";
            $content .= "<li><strong>Verifikasi Dokumen As-Built & Audit Visual Menyeluruh:</strong> Membandingkan kesesuaian gambar skematik arsitektur, struktur, dan MEP dengan realitas instalasi terpasang di gedung {$regionName}.</li>\\n";
            $content .= "<li><strong>Pengujian Instrumen Akurasi Tinggi:</strong> Melakukan pengukuran langsung dengan instrumen uji terkalibrasi laboratorium (Digital Rebound Hammer, Ultrasonic Pulse Velocity, Pitot Gauge Pompa Hydrant, Lux Meter, Sound Level Meter, Earth Tester).</li>\\n";
            $content .= "<li><strong>Analisis Deviasi terhadap Ambang Batas Standar:</strong> Menilai data ukur terhadap kriteria mutu teknis nasional, seperti batas lendutan balok maksimum L/360, kuat tekan karakteristik beton, debit aliran pompa pemadam, dan waktu evakuasi darurat.</li>\\n";
            $content .= "<li><strong>Penyusunan Tindakan Korektif & Rencana Perbaikan:</strong> Merumuskan solusi rekayasa teknik terhadap setiap temuan ketidaksesuaian, memprioritaskan perbaikan risiko tinggi, dan melakukan re-inspeksi pasca-perbaikan.</li>\\n";
            $content .= "</ul>\\n";

            $content .= "<p>Keterlibatan tim tenaga ahli pengkaji teknis independen berlisensi resmi di {$regionName} memberikan jaminan objektivitas hasil audit. Langkah ini memastikan bahwa proses sertifikasi kelaikan fungsi yang ditempuh benar-benar merefleksikan kondisi keandalan gedung secara faktual dan melindungi nilai investasi properti dalam jangka panjang.</p>\\n";

            $content .= "<blockquote>\\n";
            $content .= "<p><strong>Prinsip Keandalan Bangunan:</strong> \\\"Bangunan gedung yang laik fungsi bukan semata-mata memenuhi keindahan estetika arsitektur, melainkan perwujudan tanggung jawab moral dan hukum dalam menjamin keselamatan jiwa penghuni, kesiapsiagaan menghadapi bencana gempa dan kebakaran, serta kesinambungan pemanfaatan ruang yang aman dan produktif.\\\"</p>\\n";
            $content .= "</blockquote>\\n";

            $content .= "<p>Melalui implementasi sistematis tahapan pengujian di atas, aset properti dan gedung industri Anda di {$regionName} akan selalu berada pada status kelaikan fungsi prima, memenuhi seluruh regulasi keselamatan nasional, serta meningkatkan kepercayaan penyewa, mitra bisnis, dan pengunjung.</p>\\n\\n";
        }

        $content .= "<h3>Kesimpulan & Langkah Pengurusan Sertifikat Laik Fungsi di {$regionName}</h3>\\n";
        $content .= "<p>Pelaksanaan komprehensif audit teknis dalam <strong>{$formattedTitle}</strong> menegaskan bahwa kepatuhan terhadap kelaikan fungsi bangunan gedung adalah instrumen mitigasi risiko operasional yang paling efektif. Gedung-gedung di {$regionName} yang telah mengantongi Sertifikat Laik Fungsi (SLF) resmi berbarcode sah akan terbebas dari sanksi hukum pembekuan izin, mempermudah perolehan izin operasional bisnis lanjutan, memperoleh premi asuransi properti yang lebih kompetitif, serta memiliki nilai jual dan sewa yang jauh lebih tinggi.</p>\\n";
        $content .= "<p>Untuk konsultasi teknis, audit keandalan struktur bangunan, uji pemadam kebakaran, asesmen MEP, maupun pengurusan resmi Sertifikat Laik Fungsi (SLF) bangunan baru dan perpanjangan gedung eksisting di {$regionName}, hubungi tim pengkaji teknis dan inspektur ahli kami melalui saluran kontak resmi terpadu.</p>\\n";

        return [
            'title' => $formattedTitle,
            'slug' => $slug,
            'region' => $regionName,
            'excerpt' => "Panduan otoritatif {$formattedTitle} mengupas standar audit keandalan struktur bangunan gedung, uji NDT hammer test, proteksi kebakaran hydrant sprinkler, utilitas MEP, dan tata cara penerbitan Sertifikat Laik Fungsi (SLF) resmi di {$regionName}.",
            'content' => $content
        ];
    }

    public static function getRegionalArticleList($region, int $limit = 200): array
    {
        if (is_array($region)) {
            $parts = [];
            if (!empty($region['district'])) $parts[] = $region['district'];
            if (!empty($region['city'])) $parts[] = $region['city'];
            if (!empty($region['province'])) $parts[] = $region['province'];
            $regionName = !empty($parts) ? implode(', ', $parts) : 'Indonesia';
        } else {
            $regionName = (string) $region;
        }

        $titles = self::get200ArticleTitles();
        $articles = [];

        foreach (array_slice($titles, 0, $limit) as $index => $tTemplate) {
            $fullTitle = str_replace('{region}', $regionName, $tTemplate);
            $slug = Str::slug($fullTitle);
            $articles[] = [
                'id' => $index + 1,
                'title' => $fullTitle,
                'slug' => $slug,
                'category' => 'Jasa SLF Bangunan Gedung',
                'region' => $regionName,
                'excerpt' => "Panduan komprehensif mengenai {$fullTitle} untuk memastikan keandalan struktur, sistem proteksi kebakaran, utilitas gedung, dan penerbitan Sertifikat Laik Fungsi (SLF) resmi di {$regionName}.",
                'author' => 'Lead Structural Auditor & Tim Pengkaji Teknis SLF',
                'read_time' => 24,
                'views_count' => 195 + ($index * 11) % 450,
                'published_at' => now()->subDays($index % 60)->format('d/m/Y')
            ];
        }

        return $articles;
    }

    public static function getArticleBySlug(string $slug, $region = 'Indonesia'): ?array
    {
        if (is_array($region)) {
            $parts = [];
            if (!empty($region['district'])) $parts[] = $region['district'];
            if (!empty($region['city'])) $parts[] = $region['city'];
            if (!empty($region['province'])) $parts[] = $region['province'];
            $regionName = !empty($parts) ? implode(', ', $parts) : 'Indonesia';
        } else {
            $regionName = (string) $region;
        }

        $titles = self::get200ArticleTitles();
        $foundTitle = null;

        foreach ($titles as $tTemplate) {
            $testTitle = str_replace('{region}', $regionName, $tTemplate);
            if (Str::slug($testTitle) === $slug) {
                $foundTitle = $testTitle;
                break;
            }
        }

        if (!$foundTitle) {
            $cleanTitle = ucwords(str_replace('-', ' ', $slug));
            $foundTitle = $cleanTitle;
        }

        $articleData = self::generateDeepArticle($foundTitle, $regionName);

        return [
            'title' => $articleData['title'],
            'slug' => $slug,
            'category' => 'Jasa SLF Bangunan Gedung',
            'region' => $regionName,
            'author' => 'Lead Structural Auditor & Tim Pengkaji Teknis SLF',
            'read_time' => 24,
            'views_count' => 480,
            'created_at' => now()->subDays(2),
            'excerpt' => $articleData['excerpt'],
            'content' => $articleData['content']
        ];
    }

    public static function getArticleTopics(): array
    {
        return [
            ['name' => 'Semua Topik', 'slug' => 'semua'],
            ['name' => 'SLF Pabrik & Industri', 'slug' => 'slf-pabrik-industri'],
            ['name' => 'SLF Mall & Hotel', 'slug' => 'slf-mall-hotel'],
            ['name' => 'Audit Struktur & NDT', 'slug' => 'audit-struktur-ndt'],
            ['name' => 'Proteksi Kebakaran Hydrant', 'slug' => 'proteksi-kebakaran-hydrant'],
            ['name' => 'Utilitas MEP Gedung', 'slug' => 'utilitas-mep-gedung'],
            ['name' => 'Aksesibilitas Disabilitas', 'slug' => 'aksesibilitas-disabilitas'],
            ['name' => 'Perpanjangan SLF Berkala', 'slug' => 'perpanjangan-slf-berkala'],
        ];
    }

    public static function getOrSynthesizeArticle(string $slug, $region = 'Indonesia'): ?array
    {
        $dbArticle = \\App\\Models\\Article::where('slug', $slug)->first();
        if ($dbArticle) {
            return $dbArticle->toArray();
        }
        return self::getArticleBySlug($slug, $region);
    }
}
"""

with open(service_file, "w", encoding="utf-8") as f:
    f.write(service_code)

print(f"JasaSlfSchemeService.php written successfully to {service_file}")
