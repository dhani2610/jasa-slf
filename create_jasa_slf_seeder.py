import os

seeder_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\database\seeders\DatabaseSeeder.php"

seeder_code = """<?php

namespace Database\\Seeders;

use App\\Models\\User;
use App\\Models\\Setting;
use App\\Models\\Statistic;
use App\\Models\\Program;
use App\\Models\\Article;
use App\\Models\\Faq;
use App\\Services\\JasaSlfSchemeService;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\Hash;
use Illuminate\\Support\\Facades\\Schema;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        Schema::disableForeignKeyConstraints();

        // 1. Super Admin User
        User::updateOrCreate(
            ['email' => 'admin@jasaslf.my.id'],
            [
                'name' => 'Administrator Jasa SLF Indonesia',
                'password' => Hash::make('admin123'),
                'email_verified_at' => now(),
            ]
        );

        // 2. Settings
        $settings = [
            'site_name' => 'Jasa SLF - Sertifikat Laik Fungsi Bangunan Gedung',
            'site_tagline' => 'Layanan Resmi Pengkaji Teknis, Audit Struktur & Penerbitan Sertifikat Laik Fungsi (SLF) Nasional',
            'company_name' => 'Lembaga Pengkaji Teknis & Sertifikasi Keandalan Bangunan Gedung Indonesia',
            'license_info' => 'Lembaga Pengkaji Teknis Terakreditasi Standar Keandalan Bangunan Gedung Nasional',
            'whatsapp' => '081399810272', // Main WA Utama (Highlighted)
            'whatsapp_detail_1' => '08118500177',
            'whatsapp_detail_2' => '081399810272',
            'whatsapp_detail_3' => '087894580806',
            'whatsapp_detail_4' => '087894580649',
            'email' => 'kontak@jasaslf.my.id',
            'email_secondary' => 'info@jasaslf.my.id',
            'phone' => '081399810272',
            'address' => 'Gedung Pusat Pengkajian Teknis & Layanan Sertifikat Laik Fungsi Bangunan Gedung, Jakarta',
            'maps_embed' => 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126920.28298835848!2d106.759478!3d-6.2297465!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f3e498c0a531%3A0x7d87f7b2c0e86b0a!2sJakarta%2C%20Indonesia!5e0!3m2!1sen!2sid!4v1700000000000!5m2!1sen!2sid',
            'office_hours' => 'Senin - Jumat: 08.00 - 17.00 WIB | Hotline Konsultasi Cepat SLF & Audit Struktur WA: 24 Jam',
            'hero_title' => 'Layanan Resmi Jasa SLF (Sertifikat Laik Fungsi) Bangunan Gedung & Audit Struktur',
            'hero_description' => 'Mitra pengkaji teknis independen terakreditasi untuk audit keandalan struktur beton/baja, sistem proteksi kebakaran hydrant sprinkler, utilitas MEP, dan kelaikan fungsi bangunan di 38 provinsi di Indonesia.',
            'about_history' => 'Lembaga Jasa SLF didirikan oleh konsorsium insinyur sipil senior, ahli arsitektur bangunan gedung, lead structural auditor, dan spesialis proteksi kebakaran dengan pengalaman lebih dari dua puluh tahun. Kami berdedikasi mendampingi sektor industri manufaktur, pergudangan, pusat perbelanjaan, perhotelan, rumah sakit, data center, dan gedung perkantoran dalam menjamin bahwa bangunan gedung yang didirikan dan ditempati memenuhi standar keandalan struktur, keselamatan jiwa dari kebakaran, kesehatan lingkungan, dan kemudahan aksesibilitas sesuai regulasi teknis nasional.',
            'about_vision' => 'Menjadi lembaga pengkaji teknis bangunan gedung terdepan, terpercaya, dan tercepat di Indonesia dalam mewujudkan gedung yang kokoh, aman terhadap bencana gempa dan kebakaran, ramah lingkungan, serta memiliki kepatuhan hukum penuh.',
            'about_mission' => "1. Menyelenggarakan audit keandalan struktur, proteksi kebakaran, dan utilitas MEP secara independen dengan instrumen uji presisi terkalibrasi.\\n2. Memberikan layanan pengurusan dan penerbitan Sertifikat Laik Fungsi (SLF) resmi dengan tata kelola transparan, akuntabel, dan tepat waktu.\\n3. Membimbing pengelola fasilitas dalam menyusun manual pemeliharaan preventif bangunan gedung (building maintenance plan) dan perpanjangan SLF berkala.\\n4. Mendukung terciptanya Zero Building Disaster and Zero Fire Accident pada seluruh fasilitas industri dan komersial di Indonesia.",
            'floating_wa_text' => 'Halo Admin Jasa SLF Indonesia, saya ingin konsultasi permohonan Sertifikat Laik Fungsi (SLF) dan audit keandalan bangunan gedung perusahaan.'
        ];

        foreach ($settings as $key => $value) {
            Setting::updateOrCreate(['key' => $key], ['value' => $value]);
        }

        // 3. Statistics
        $statistics = [
            [
                'key' => 'slf_terbit',
                'label' => 'Sertifikat SLF Terbit',
                'value' => '12.800+',
                'icon' => 'bi-patch-check-fill',
                'description' => 'Pabrik, Gudang, Mall, Hotel, RS & Menara Perkantoran',
                'sort_order' => 1
            ],
            [
                'key' => 'kepatuhan_keandalan',
                'label' => 'Kepatuhan Uji Keandalan',
                'value' => '100%',
                'icon' => 'bi-shield-check',
                'description' => 'Uji Struktur NDT, Fire Safety & MEP Terverifikasi Sah',
                'sort_order' => 2
            ],
            [
                'key' => 'jangkauan_provinsi',
                'label' => 'Jangkauan Wilayah Asesmen',
                'value' => '38',
                'icon' => 'bi-geo-alt-fill',
                'description' => 'Provinsi di Seluruh Wilayah Republik Indonesia',
                'sort_order' => 3
            ],
            [
                'key' => 'kepuasan_klien',
                'label' => 'Tingkat Kepuasan Klien',
                'value' => '99.8%',
                'icon' => 'bi-trophy-fill',
                'description' => 'Didukung Lebih dari 1.200 Perusahaan Properti & BUMN',
                'sort_order' => 4
            ]
        ];

        foreach ($statistics as $stat) {
            Statistic::updateOrCreate(['key' => $stat['key']], $stat);
        }

        // 4. Programs Seeding from JasaSlfSchemeService
        $programs = JasaSlfSchemeService::getMasterPrograms();
        foreach ($programs as $index => $prog) {
            Program::updateOrCreate(
                ['slug' => $prog['slug']],
                [
                    'title' => $prog['title'],
                    'level_name' => $prog['level_name'] ?? 'Layanan Sertifikasi SLF Resmi',
                    'level_code' => $prog['level_code'] ?? 'SLF',
                    'badge' => $prog['badge'] ?? 'Layanan Terakreditasi',
                    'duration' => $prog['duration'] ?? 'Proses Cepat & Akurat',
                    'method' => $prog['method'] ?? 'Inspeksi Visual, Uji NDT Struktur & Komisioning MEP',
                    'certification' => $prog['certification'] ?? 'Sertifikat Laik Fungsi (SLF) Resmi',
                    'price_note' => $prog['price_note'] ?? 'Hubungi Tim Pengkaji Teknis SLF',
                    'target_audience' => $prog['target_audience'] ?? '',
                    'requirements' => json_encode($prog['requirements'] ?? []),
                    'curriculum' => json_encode($prog['curriculum'] ?? []),
                    'facilities' => json_encode($prog['facilities'] ?? []),
                    'short_description' => $prog['short_description'] ?? '',
                    'full_description' => $prog['overview'] ?? ($prog['short_description'] ?? ''),
                    'image' => 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
                    'is_active' => true,
                    'sort_order' => $index + 1
                ]
            );
        }

        // 5. Featured Articles (Homepage 3 cards)
        $articles = [
            [
                'title' => 'Training Jasa SLF: Panduan Lengkap Sertifikat Laik Fungsi (SLF) Bangunan Gedung & Standar Teknis Nasional di Indonesia',
                'slug' => 'training-jasa-slf-panduan-lengkap-sertifikat-laik-fungsi-slf-bangunan-gedung-standar-teknis-nasional-di-indonesia',
                'category' => 'Panduan Sertifikasi SLF',
                'author' => 'Lead Structural Auditor & Tim Pengkaji Teknis SLF',
                'read_time' => 26,
                'views_count' => 5820,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Panduan komprehensif alur pengurusan Sertifikat Laik Fungsi (SLF), dokumen as-built drawing arsitektur struktur MEP, tata cara pemeriksaan fisik lapangan, dan pemenuhan regulasi keandalan bangunan gedung nasional.',
                'content' => JasaSlfSchemeService::generateDeepArticle('Training Jasa SLF: Panduan Lengkap Sertifikat Laik Fungsi (SLF) Bangunan Gedung & Standar Teknis Nasional di Indonesia', 'Indonesia')['content']
            ],
            [
                'title' => 'Jasa SLF: Uji Keandalan Struktur Beton & Rangka Baja Bangunan Pabrik Industri di Indonesia',
                'slug' => 'jasa-slf-uji-keandalan-struktur-beton-rangka-baja-bangunan-pabrik-industri-di-indonesia',
                'category' => 'Audit Struktur & NDT',
                'author' => 'Lead Structural Auditor & Tim Pengkaji Teknis SLF',
                'read_time' => 28,
                'views_count' => 5140,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1541888946425-d0fbb18615f3?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Prosedur teknis asesmen kekuatan portal baja, non-destructive test (NDT) Schmidt hammer test beton, ketebalan korosi elemen baja struktural, serta analisis ketahanan beban gempa fasilitas pabrik manufaktur.',
                'content' => JasaSlfSchemeService::generateDeepArticle('Jasa SLF: Uji Keandalan Struktur Beton & Rangka Baja Bangunan Pabrik Industri di Indonesia', 'Indonesia')['content']
            ],
            [
                'title' => 'Training Jasa SLF: Audit Sistem Proteksi Kebakaran Hydrant, Sprinkler & Pompa Pemadam di Indonesia',
                'slug' => 'training-jasa-slf-audit-sistem-proteksi-kebakaran-hydrant-sprinkler-pompa-pemadam-di-indonesia',
                'category' => 'Proteksi Kebakaran Gedung',
                'author' => 'Lead Structural Auditor & Tim Pengkaji Teknis SLF',
                'read_time' => 25,
                'views_count' => 4760,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Metodologi pengujian debit dan tekanan pompa kebakaran hydrant, kurva performa flow test sprinkler otomatis, kompartemenisasi pintu darurat tahan api, dan manajemen asap untuk keselamatan jiwa penghuni gedung.',
                'content' => JasaSlfSchemeService::generateDeepArticle('Training Jasa SLF: Audit Sistem Proteksi Kebakaran Hydrant, Sprinkler & Pompa Pemadam di Indonesia', 'Indonesia')['content']
            ]
        ];

        foreach ($articles as $art) {
            Article::updateOrCreate(['slug' => $art['slug']], $art);
        }

        // 6. FAQs
        $faqs = [
            [
                'question' => 'Apa itu Sertifikat Laik Fungsi (SLF) dan mengapa setiap bangunan gedung wajib memilikinya?',
                'answer' => 'Sertifikat Laik Fungsi (SLF) adalah sertifikat resmi berkekuatan hukum yang menyatakan bahwa bangunan gedung telah selesai dibangun dan memenuhi seluruh kriteria teknis kelaikan fungsi sebelum dapat dimanfaatkan. Memiliki SLF adalah kewajiban hukum untuk menjamin keselamatan jiwa penghuni dari bahaya keruntuhan struktur dan kebakaran, menjamin kesehatan lingkungan, melindungi investasi properti, serta menjadi syarat mutlak penerbitan izin operasional bisnis dan polis asuransi gedung.',
                'sort_order' => 1
            ],
            [
                'question' => 'Jenis bangunan gedung apa saja yang dilayani pengujian dan pengurusan SLF-nya oleh lembaga kami?',
                'answer' => 'Kami melayani 8 lingkup pengkajian teknis kelaikan fungsi: 1) Bangunan Industri, Pabrik Manufaktur & Gudang Logistik; 2) Bangunan Komersial, Mall, Pusat Perbelanjaan & Hotel Bertingkat; 3) Fasilitas Rumah Sakit, Klinik & Laboratorium Medis; 4) Pusat Data (Data Center), Gedung Perkantoran & Menara Komunikasi; 5) Pelatihan & Audit Struktur NDT (Hammer Test/UPV); 6) Asesmen Proteksi Kebakaran Hydrant & Sprinkler; 7) Uji Kelaikan Utilitas MEP (Genset, Lift, Plumbing & HVAC); serta 8) Manajemen Pemeliharaan Bangunan & Perpanjangan SLF Berkala.',
                'sort_order' => 2
            ],
            [
                'question' => 'Berapa lama masa berlaku Sertifikat Laik Fungsi (SLF) dan bagaimana prosedur perpanjangannya?',
                'answer' => 'Sesuai standar regulasi tata bangunan nasional, masa berlaku Sertifikat Laik Fungsi untuk bangunan gedung umum (industri, komersial, perkantoran, rumah sakit, hotel) adalah 5 (lima) tahun, sedangkan untuk bangunan rumah tinggal tunggal berlaku selama 20 (dua puluh) tahun. Perpanjangan SLF wajib diajukan sebelum masa berlakunya habis melalui pengkajian teknis berkala guna memastikan gedung tetap dirawat dan laik digunakan.',
                'sort_order' => 3
            ],
            [
                'question' => 'Apa saja parameter teknis yang diperiksa oleh tim pengkaji teknis selama audit lapangan?',
                'answer' => 'Pemeriksaan teknis mencakup 4 pilar keandalan: 1) Keselamatan Struktur (Uji NDT Schmidt hammer test, pemindaian tulangan rebar scan, ketahanan gempa & fondasi); 2) Proteksi Kebakaran (Uji debit/tekanan pompa hydrant, sprinkler, alarm deteksi, pintu darurat tahan api & smoke exhaust); 3) Kesehatan Lingkungan (Ventilasi udara HVAC, pencahayaan alami/buatan, instalasi air bersih & pengolahan limbah STP); serta 4) Kemudahan & Kenyamanan (Uji kelaikan lift penumpang, kemiringan ramp disabilitas, toilet difabel, tingkat kebisingan & getaran).',
                'sort_order' => 4
            ],
            [
                'question' => 'Bagaimana prosedur dan estimasi waktu penerbitan Sertifikat Laik Fungsi (SLF) melalui lembaga kami?',
                'answer' => 'Proses sangat sistematis dan terukur: 1) Verifikasi berkas administrasi dan gambar As-Built Drawing Arsitektur, Struktur & MEP; 2) Penjadwalan inspeksi visual dan pengujian instrumen di lokasi gedung; 3) Analisis data uji dan penyusunan Laporan Kajian Teknis Keandalan Bangunan; 4) Pelaksanaan sidang evaluasi teknis bersama Dewan Ahli Pengkaji; 5) Penerbitan rekomendasi teknis; dan 6) Pengesahan serta penyerahan Sertifikat Laik Fungsi (SLF) berbarcode resmi yang sah secara nasional dalam waktu 7 hingga 14 hari kerja pasca-uji dinyatakan memenuhi syarat.',
                'sort_order' => 5
            ]
        ];

        foreach ($faqs as $faq) {
            Faq::updateOrCreate(['question' => $faq['question']], $faq);
        }

        Schema::enableForeignKeyConstraints();
    }
}
"""

with open(seeder_path, "w", encoding="utf-8") as f:
    f.write(seeder_code)

print("DatabaseSeeder.php for Jasa SLF created successfully!")
