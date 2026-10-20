import os

index_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slf\resources\views\front\index.blade.php"

content = """@extends('layouts.front')

@section('title', 'Jasa SLF - Sertifikat Laik Fungsi Bangunan Gedung | Layanan Pengkaji Teknis Resmi')
@section('meta_description', 'Layanan resmi Jasa SLF (Sertifikat Laik Fungsi), audit keandalan struktur beton/baja, proteksi kebakaran hydrant sprinkler, utilitas MEP, dan penerbitan SLF di 38 provinsi di Indonesia.')

@section('content')
    <style>
        /* CSS KHUSUS DIREKTORI WILAYAH SEPERTI TRAINING PUBT (TEMA ORANGE & HIJAU MUDA) */
        .wilayah-section-wrap {
            background: #ffffff;
            border-bottom: 1px solid #e2e8f0;
        }
        .island-tab-btn {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            color: #475569;
            padding: 8px 16px;
            border-radius: 50px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .island-tab-btn:hover {
            border-color: #ea580c;
            color: #ea580c;
            background: #fff7ed;
        }
        .island-tab-btn.active {
            background: linear-gradient(135deg, #ea580c 0%, #f97316 100%);
            border-color: #ea580c;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(234, 88, 12, 0.35);
        }
        .home-province-card {
            background: #ffffff;
            border: 1px solid #fed7aa;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.25s ease;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
            margin-bottom: 16px;
        }
        .home-province-card:hover {
            border-color: #f97316;
            box-shadow: 0 6px 18px rgba(234, 88, 12, 0.08);
        }
        .prov-header-toggle {
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            background: #fff7ed;
            border-bottom: 1px solid transparent;
            flex-wrap: wrap;
            gap: 10px;
            transition: background 0.2s ease;
        }
        .prov-header-toggle.is-open {
            background: #ffedd5;
            border-bottom-color: #fdba74;
        }
        .prov-preview-bar {
            padding: 8px 18px;
            background: #ffffff;
            border-bottom: 1px solid #f1f5f9;
            font-size: 0.77rem;
            color: #64748b;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 6px;
        }
        .prov-preview-tag {
            background: #f1f5f9;
            color: #334155;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.73rem;
            font-weight: 600;
        }
        .prov-drawer-body {
            padding: 18px;
            background: #ffffff;
            border-top: 1px solid #fed7aa;
        }
        .kabkot-card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 12px;
        }
        .home-kabkot-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }
        .home-kabkot-box:hover {
            background: #ffffff;
            border-color: #f97316;
            box-shadow: 0 4px 12px rgba(234, 88, 12, 0.08);
        }
        .home-kec-pill {
            font-size: 0.72rem;
            color: #334155;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 2px 7px;
            border-radius: 4px;
            text-decoration: none;
            transition: all 0.15s ease;
            display: inline-block;
        }
        .home-kec-pill:hover {
            border-color: #ea580c;
            color: #ea580c;
            background: #fff7ed;
        }
    </style>

    <!-- HERO SLIDER SECTION (TANPA FOTO - HIGH-TECH STRUCTURAL HEALTH MONITORING & SLF CERTIFICATION HUD) -->
    <section class="gas-hero-wrapper" style="background: radial-gradient(circle at 80% 20%, rgba(234, 88, 12, 0.28) 0%, transparent 45%), radial-gradient(circle at 10% 80%, rgba(249, 115, 22, 0.18) 0%, transparent 50%), #0f172a; color: #ffffff; padding: 60px 0 70px; position: relative; overflow: hidden;">
        <!-- Background Grid Pattern -->
        <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 36px 36px; pointer-events: none;"></div>

        <div class="container" style="position: relative; z-index: 2;">
            <div class="hero-slider-container" id="heroSlider" style="position: relative; min-height: 480px;">
                <div class="hero-slide active" data-slide="1" style="display: block; transition: all 0.5s ease;">
                    <div class="hero-slide-grid" style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center;">
                        <div>
                            <div class="hero-badge" style="background: rgba(234, 88, 12, 0.2); border: 1px solid rgba(249, 115, 22, 0.5); color: #fb923c; font-size: 0.78rem; font-weight: 800; padding: 6px 16px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;">
                                <i class="bi bi-patch-check-fill" style="color: #f97316;"></i> Lembaga Pengkaji Teknis SLF Terakreditasi Resmi
                            </div>

                            <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 18px; color: #ffffff; letter-spacing: -0.5px;">
                                Layanan Resmi <span style="background: linear-gradient(135deg, #fb923c 0%, #ea580c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Jasa SLF & Sertifikat Laik Fungsi</span> Bangunan Gedung
                            </h1>

                            <p style="font-size: 1.02rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 28px; max-width: 620px;">
                                Melayani audit keandalan struktur beton/baja (NDT Hammer Test & UPV), pengujian proteksi kebakaran hydrant sprinkler, uji komisioning utilitas MEP, dan penerbitan Sertifikat Laik Fungsi (SLF) resmi untuk pabrik, gudang, mall, hotel, rumah sakit, dan gedung perkantoran di 38 provinsi di Indonesia.
                            </p>

                            <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 32px;">
                                <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Admin Utama Jasa SLF Indonesia, saya ingin konsultasi permohonan Sertifikat Laik Fungsi (SLF) resmi.') }}" target="_blank" class="btn-primary-green" style="background: linear-gradient(135deg, #ea580c 0%, #f97316 100%); border: 1px solid #fed7aa; box-shadow: 0 4px 18px rgba(234, 88, 12, 0.45); color: #ffffff; font-weight: 700; padding: 12px 24px; border-radius: 50px; display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
                                    <i class="bi bi-whatsapp" style="color: #25d366;"></i> Hotline Utama: 0813-9981-0272
                                </a>
                                <a href="#wilayah" class="btn-outline-white" style="border: 1px solid rgba(255,255,255,0.25); background: rgba(255,255,255,0.06); color: #ffffff; font-weight: 700; padding: 12px 22px; border-radius: 50px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                                    <i class="bi bi-geo-alt-fill" style="color: #fb923c;"></i> Direktori 38 Provinsi
                                </a>
                            </div>

                            <div style="display: flex; align-items: center; gap: 24px; color: #94a3b8; font-size: 0.85rem; flex-wrap: wrap;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> Sertifikat SLF Berbarcode Sah
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> Tenaga Ahli Pengkaji Berlisensi
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> Instrumen Uji NDT Terkalibrasi KAN
                                </div>
                            </div>
                        </div>

                        <!-- SIMULATED STRUCTURAL HEALTH MONITORING & SLF TELEMETRY HUD -->
                        <div>
                            <div style="background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%); border: 2px solid rgba(249, 115, 22, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.1); position: relative;">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 12px; margin-bottom: 18px;">
                                    <div style="display: flex; align-items: center; gap: 8px;">
                                        <span style="display: inline-block; width: 10px; height: 10px; background: #f97316; border-radius: 50%; box-shadow: 0 0 10px #f97316; animation: pulse 2s infinite;"></span>
                                        <span style="font-size: 0.78rem; font-weight: 800; color: #fed7aa; text-transform: uppercase; letter-spacing: 0.8px;">STRUCTURAL & UTILITY HEALTH TELEMETRY</span>
                                    </div>
                                    <span style="font-size: 0.72rem; background: rgba(34, 197, 94, 0.2); color: #86efac; padding: 3px 10px; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.4); font-weight: 700;">100% LAIK FUNGSI &bull; STRUKTUR TERUJI</span>
                                </div>

                                <div class="hud-metrics-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
                                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Lendutan Balok Struktur</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #fb923c;">0.00 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">mm</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Normal &bull; Bebas Retak L/360</div>
                                    </div>

                                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Kuat Tekan Beton Karakteristik</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #f97316;">38.5 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">MPa</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Schmidt Hammer Test Lulus</div>
                                    </div>

                                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Pompa Kebakaran Hydrant</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #fb923c;">1.000 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">GPM</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Tekanan 10 Bar &bull; NFPA 20</div>
                                    </div>

                                    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Transportasi Vertikal (Lift)</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #f97316;">100 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">%</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Governor & Safety Brake Aktif</div>
                                    </div>
                                </div>

                                <div style="background: rgba(10, 15, 26, 0.85); border-radius: 10px; padding: 12px; font-family: monospace; font-size: 0.75rem; color: #cbd5e1; border: 1px solid rgba(255,255,255,0.08);">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <span style="color: #fb923c;">[AUDIT-SLF]</span>
                                        <span style="color: #facc15;">12.800+ SERTIFIKAT TERBIT</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <span>Status Tangga Darurat:</span>
                                        <span style="color: #86efac;">PRESSURIZED (SMOKE-FREE)</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;">
                                        <span>Hasil Asesmen Arsitektur:</span>
                                        <span style="color: #86efac;">UNIVERSAL ACCESSIBILITY OK</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Hotlines Bar -->
            <div style="margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 600;">Layanan Cepat Tanggap 24 Jam:</span>
                    <span style="font-size: 0.85rem; color: #fb923c; font-weight: 800;">4 Hotline WhatsApp Resmi SLF Terverifikasi</span>
                </div>
                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    @foreach($waNumbers as $num)
                        <a href="{{ $num['url'] }}" target="_blank" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #ffffff; padding: 6px 14px; border-radius: 8px; font-size: 0.78rem; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; transition: all 0.2s ease;">
                            <i class="bi bi-whatsapp" style="color: #25d366;"></i> {{ $num['number'] }}
                        </a>
                    @endforeach
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: DIREKTORI WILAYAH PELATIHAN & LAYANAN JASA SLF LENGKAP SAMPAI KECAMATAN (PERSIS TRAINING PUBT) -->
    <section class="section-py wilayah-section-wrap" id="wilayah">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 32px;">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-geo-alt-fill" style="color: #ea580c;"></i> Jangkauan Layanan 38 Provinsi • 514 Kab/Kota • Seluruh Kecamatan
                </span>
                <h2 class="section-title">Direktori Wilayah Layanan Jasa SLF Seluruh Indonesia</h2>
                <p class="section-desc" style="max-width: 840px; margin: 0 auto;">
                    Kami menyelenggarakan pengkajian teknis, audit keandalan struktur bangunan gedung, inspeksi proteksi kebakaran, dan penerbitan Sertifikat Laik Fungsi (SLF) di seluruh 38 provinsi di Indonesia hingga ke tingkat kabupaten, kota, dan kecamatan. Klik pada nama wilayah untuk melihat informasi persyaratan dokumen, jadwal tim pengkaji, dan artikel teknis spesifik di daerah Anda:
                </p>
            </div>

            @php
                // Build lightweight structure for Cascading Explorer & Live Search
                $regionsExplorerData = [];
                foreach($provinces as $pSlug => $pr) {
                    $kabkotItems = [];
                    foreach($pr['kabkot'] as $kk) {
                        $kabkotItems[] = [
                            'name' => $kk['name'],
                            'slug' => $kk['slug'],
                            'kecamatan' => $kk['kecamatan'] ?? [],
                        ];
                    }
                    $regionsExplorerData[$pr['slug']] = [
                        'name' => $pr['name'],
                        'slug' => $pr['slug'],
                        'island' => $pr['island'] ?? 'Indonesia',
                        'total_kabkot' => $pr['total_kabkot'] ?? count($kabkotItems),
                        'kabkot' => $kabkotItems,
                    ];
                }

                $islands = [
                    'Sumatera' => ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Kepulauan Riau', 'Jambi', 'Sumatera Selatan', 'Kepulauan Bangka Belitung', 'Bengkulu', 'Lampung'],
                    'Jawa' => ['DKI Jakarta', 'Jawa Barat', 'Banten', 'Jawa Tengah', 'DI Yogyakarta', 'Jawa Timur'],
                    'Bali & Nusa Tenggara' => ['Bali', 'Nusa Tenggara Barat', 'Nusa Tenggara Timur'],
                    'Kalimantan' => ['Kalimantan Barat', 'Kalimantan Tengah', 'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara'],
                    'Sulawesi' => ['Sulawesi Utara', 'Gorontalo', 'Sulawesi Tengah', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tenggara'],
                    'Maluku & Papua' => ['Maluku', 'Maluku Utara', 'Papua', 'Papua Barat', 'Papua Selatan', 'Papua Tengah', 'Papua Pegunungan', 'Papua Barat Daya']
                ];

                // Showcase top provinces open by default so visitors immediately see Kab/Kot and Kecamatan
                $defaultOpenProvinces = [
                    'Aceh', 'Sumatera Utara', 'DKI Jakarta', 'Jawa Barat', 'Bali', 'Kalimantan Timur', 'Sulawesi Selatan', 'Papua'
                ];
            @endphp

            <!-- 1. KOTAK SELEKSI CEPAT TINGKAT PROVINSI, KABKOT & KECAMATAN -->
            <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 18px; padding: 26px 28px; margin-bottom: 34px; box-shadow: 0 16px 36px -10px rgba(15, 23, 42, 0.45); color: #ffffff; border: 1.5px solid rgba(249, 115, 22, 0.4);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
                    <div>
                        <div style="font-size: 0.76rem; font-weight: 800; color: #fb923c; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px;">
                            <i class="bi bi-compass-fill"></i> Fitur Eksplorasi Interaktif
                        </div>
                        <h3 style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin: 0;">
                            Pencarian Cepat Tingkat Provinsi, Kota & Kecamatan
                        </h3>
                    </div>
                    <span style="font-size: 0.78rem; background: rgba(234, 88, 12, 0.25); color: #fed7aa; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(249, 115, 22, 0.5); font-weight: 700;">
                        <i class="bi bi-lightning-charge-fill" style="color: #facc15;"></i> Langsung ke Halaman Wilayah
                    </span>
                </div>

                <!-- 3-Dropdown Grid -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) 160px; gap: 12px; align-items: end; margin-bottom: 18px;">
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px; display: block;">1. Pilih Provinsi:</label>
                        <select id="homeProvSelect" class="form-control" style="background: #ffffff; color: #0f172a; padding: 11px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; width: 100%; border: none;">
                            <option value="">-- Pilih Provinsi --</option>
                            @foreach($provinces as $p)
                                <option value="{{ $p['slug'] }}">{{ $p['name'] }} ({{ $p['total_kabkot'] }} Wilayah)</option>
                            @endforeach
                        </select>
                    </div>

                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px; display: block;">2. Pilih Kabupaten / Kota:</label>
                        <select id="homeKabkotSelect" class="form-control" style="background: #ffffff; color: #0f172a; padding: 11px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; width: 100%; border: none;" disabled>
                            <option value="">-- Pilih Kabupaten / Kota --</option>
                        </select>
                    </div>

                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #cbd5e1; margin-bottom: 6px; display: block;">3. Pilih Kecamatan:</label>
                        <select id="homeKecamatanSelect" class="form-control" style="background: #ffffff; color: #0f172a; padding: 11px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; width: 100%; border: none;" disabled>
                            <option value="">-- Pilih Kecamatan --</option>
                        </select>
                    </div>

                    <div>
                        <button type="button" id="homeGoRegionBtn" style="width: 100%; justify-content: center; padding: 12px 16px; font-size: 0.88rem; box-shadow: 0 4px 16px rgba(234, 88, 12, 0.45); white-space: nowrap; background: linear-gradient(135deg, #ea580c 0%, #f97316 100%); color: #ffffff; font-weight: 800; border-radius: 8px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
                            <i class="bi bi-box-arrow-up-right"></i> Buka Wilayah
                        </button>
                    </div>
                </div>

                <!-- Live Keyword Search Filter -->
                <div style="position: relative;">
                    <i class="bi bi-search" style="position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: #94a3b8;"></i>
                    <input type="text" id="homeLiveRegionSearch" class="form-control" placeholder="Atau ketik nama Kota, Kabupaten, atau Kecamatan (misal: Bandung, Karawang, Cikarang, Surabaya, Medan, Balikpapan)..." style="background: rgba(255,255,255,0.96); color: #0f172a; padding: 11px 16px 11px 42px; border-radius: 8px; font-size: 0.88rem; width: 100%; border: none;">
                    
                    <!-- Search Results Popup Box -->
                    <div id="homeSearchResultsBox" style="display: none; position: absolute; left: 0; right: 0; top: 105%; background: #ffffff; border-radius: 12px; box-shadow: 0 14px 35px rgba(0,0,0,0.25); z-index: 100; max-height: 320px; overflow-y: auto; padding: 10px; border: 1px solid #cbd5e1;">
                    </div>
                </div>
            </div>

            <!-- 2. ISLAND FILTER TABS & GLOBAL CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; flex-wrap: wrap; gap: 12px;">
                <div style="display: flex; flex-wrap: wrap; gap: 8px;" id="islandFilterTabs">
                    <button type="button" class="island-tab-btn active" data-island="all">
                        Semua Pulau (38)
                    </button>
                    @foreach($islands as $iName => $pList)
                        <button type="button" class="island-tab-btn" data-island="{{ Str::slug($iName) }}">
                            {{ $iName }} ({{ count($pList) }})
                        </button>
                    @endforeach
                </div>

                <div style="display: flex; gap: 8px;">
                    <button type="button" id="btnExpandAllProvs" style="font-size: 0.78rem; font-weight: 700; color: #ea580c; background: #fff7ed; border: 1px solid #fed7aa; padding: 7px 14px; border-radius: 6px; cursor: pointer;">
                        <i class="bi bi-arrows-expand"></i> Buka Semua Kab/Kota & Kec
                    </button>
                    <button type="button" id="btnCollapseAllProvs" style="font-size: 0.78rem; font-weight: 700; color: #64748b; background: #f1f5f9; border: 1px solid #cbd5e1; padding: 7px 14px; border-radius: 6px; cursor: pointer;">
                        <i class="bi bi-arrows-collapse"></i> Tutup Semua
                    </button>
                </div>
            </div>

            <!-- 3. ISLAND GROUPED PROVINCES WITH KAB/KOT & KECAMATAN DETAILS -->
            @foreach($islands as $islandName => $provNames)
                <div class="island-group-block" data-island="{{ Str::slug($islandName) }}" style="margin-bottom: 34px;">
                    <h3 style="font-size: 1.18rem; font-weight: 800; color: #0f172a; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; border-bottom: 2px solid #fed7aa; padding-bottom: 8px;">
                        <i class="bi bi-geo-alt-fill" style="color: #ea580c;"></i> Wilayah {{ $islandName }}
                    </h3>

                    <div style="display: flex; flex-direction: column; gap: 14px;">
                        @foreach($provNames as $pName)
                            @php
                                $provObj = null;
                                foreach($provinces as $pr) {
                                    if(strtolower(trim($pr['name'])) === strtolower(trim($pName))) {
                                        $provObj = $pr;
                                        break;
                                    }
                                }
                                $isOpen = in_array($pName, $defaultOpenProvinces);
                            @endphp
                            @if($provObj)
                                <div class="home-province-card">
                                    <!-- Card Header (Click to toggle accordion) -->
                                    <div class="prov-header-toggle {{ $isOpen ? 'is-open' : '' }}">
                                        <div style="display: flex; align-items: center; gap: 10px;">
                                            <div style="width: 34px; height: 34px; background: #ffffff; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #ea580c; font-size: 0.95rem; border: 1px solid #fed7aa;">
                                                <i class="bi bi-map-fill"></i>
                                            </div>
                                            <div>
                                                <span style="font-size: 0.98rem; font-weight: 800; color: #0f172a;">{{ $provObj['name'] }}</span>
                                                <span class="badge" style="font-size: 0.74rem; font-weight: 700; color: #c2410c; background: #fff7ed; padding: 3px 8px; border-radius: 12px; margin-left: 6px; border: 1px solid #fed7aa;">
                                                    {{ $provObj['total_kabkot'] }} Kab/Kota • Tingkat Kecamatan
                                                </span>
                                            </div>
                                        </div>

                                        <div style="display: flex; align-items: center; gap: 10px;">
                                            <a href="{{ url('/wilayah/' . $provObj['slug']) }}" class="btn-sm" style="font-size: 0.78rem; font-weight: 700; color: #ea580c; background: #ffffff; border: 1px solid #fed7aa; padding: 5px 12px; border-radius: 6px; text-decoration: none; display: inline-flex; align-items: center; gap: 4px;" onclick="event.stopPropagation();">
                                                <span>Buka Provinsi</span> <i class="bi bi-box-arrow-up-right"></i>
                                            </a>
                                            <button type="button" class="btn-toggle-icon" style="background: none; border: none; font-size: 0.86rem; color: #64748b; cursor: pointer; display: flex; align-items: center; gap: 4px;">
                                                <span class="toggle-text" style="font-size: 0.76rem; font-weight: 700; color: {{ $isOpen ? '#ea580c' : '#64748b' }};">{{ $isOpen ? 'Sembunyikan' : 'Lihat Kab/Kot & Kec' }}</span>
                                                <i class="bi bi-chevron-down toggle-chevron" style="transition: transform 0.25s ease; transform: {{ $isOpen ? 'rotate(180deg)' : 'rotate(0deg)' }};"></i>
                                            </button>
                                        </div>
                                    </div>

                                    <!-- Quick Preview Bar (Visible directly on card) -->
                                    <div class="prov-preview-bar">
                                        <span style="font-weight: 700; color: #c2410c; display: flex; align-items: center; gap: 4px;">
                                            <i class="bi bi-pin-map-fill"></i> Cakupan:
                                        </span>
                                        @foreach(array_slice($provObj['kabkot'], 0, 6) as $kkPre)
                                            <span class="prov-preview-tag">{{ $kkPre['name'] }}</span>
                                        @endforeach
                                        @if(count($provObj['kabkot']) > 6)
                                            <span style="font-size: 0.72rem; color: #ea580c; font-weight: 700;">+{{ count($provObj['kabkot']) - 6 }} Kab/Kota lainnya</span>
                                        @endif
                                    </div>

                                    <!-- Card Body (Kabupaten & Kecamatan) -->
                                    <div class="prov-drawer-body" style="display: {{ $isOpen ? 'block' : 'none' }};">
                                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                                            <div style="font-size: 0.84rem; font-weight: 800; color: #1e293b;">
                                                <i class="bi bi-buildings" style="color: #ea580c; margin-right: 6px;"></i> Daftar Lengkap Kabupaten, Kota, & Kecamatan di {{ $provObj['name'] }}:
                                            </div>
                                            <a href="{{ url('/wilayah/' . $provObj['slug']) }}" style="font-size: 0.78rem; color: #ea580c; font-weight: 700; text-decoration: none;">
                                                Buka Panduan & Artikel Lengkap {{ $provObj['name'] }} &rarr;
                                            </a>
                                        </div>

                                        <!-- Grid of Kab/Kot Cards with Kecamatan Pills -->
                                        <div class="kabkot-card-grid">
                                            @foreach($provObj['kabkot'] as $kk)
                                                @php
                                                    $kkKecList = $kk['kecamatan'] ?? [];
                                                    $kabkotUrl = url('/wilayah/' . $provObj['slug'] . '/' . $kk['slug']);
                                                @endphp
                                                <div class="home-kabkot-box">
                                                    <div>
                                                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                                                            <a href="{{ $kabkotUrl }}" style="font-size: 0.88rem; font-weight: 800; color: #0f172a; text-decoration: none; display: flex; align-items: center; gap: 6px;" title="Lihat layanan Jasa SLF di {{ $kk['name'] }}">
                                                                <i class="bi bi-geo-alt-fill" style="color: #ea580c;"></i> {{ $kk['name'] }}
                                                            </a>
                                                            <span style="font-size: 0.68rem; font-weight: 700; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 4px; border: 1px solid #fed7aa;">
                                                                {{ count($kkKecList) }} Kec
                                                            </span>
                                                        </div>

                                                        <!-- Kecamatan Pills -->
                                                        <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px;">
                                                            @foreach($kkKecList as $kec)
                                                                @php
                                                                    $kecSlug = Str::slug($kec);
                                                                    $kecUrl = url('/wilayah/' . $provObj['slug'] . '/' . $kk['slug'] . '/' . $kecSlug);
                                                                @endphp
                                                                <a href="{{ $kecUrl }}" class="home-kec-pill" title="Jasa SLF Bangunan Gedung Kecamatan {{ $kec }}, {{ $kk['name'] }}">
                                                                    {{ $kec }}
                                                                </a>
                                                            @endforeach
                                                        </div>
                                                    </div>

                                                    <div style="border-top: 1px dashed #fed7aa; padding-top: 8px; margin-top: 6px;">
                                                        <a href="{{ $kabkotUrl }}" style="font-size: 0.76rem; font-weight: 700; color: #ea580c; text-decoration: none; display: flex; align-items: center; justify-content: space-between;">
                                                            <span>Lihat Panduan & Artikel {{ $kk['name'] }}</span>
                                                            <i class="bi bi-chevron-right"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                            @endforeach
                                        </div>
                                    </div>
                                </div>
                            @endif
                        @endforeach
                    </div>
                </div>
            @endforeach
        </div>
    </section>

    <!-- SECTION 3: 8 LAYANAN RESMI JASA SLF BANGUNAN GEDUNG -->
    <section class="section-py" id="program" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-buildings-fill" style="color: #ea580c;"></i> Ruang Lingkup Layanan
                </span>
                <h2 class="section-title">8 Layanan Unggulan Jasa SLF & Sertifikasi Keandalan Gedung</h2>
                <p class="section-desc">
                    Program komprehensif pengkajian teknis, audit struktur, uji sistem proteksi kebakaran, dan sertifikasi kelaikan fungsi yang dirancang untuk menjawab kepatuhan regulasi keandalan bangunan gedung:
                </p>
            </div>

            <div class="programs-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 26px;">
                @foreach($programs as $prog)
                    @php
                        $progObj = is_array($prog) ? (object)$prog : $prog;
                        $slug = $progObj->slug ?? '';
                        $detailUrl = route('program.detail', $slug);
                        $directWa = "https://api.whatsapp.com/send?phone=6281399810272&text=" . urlencode("Halo Admin Jasa SLF Indonesia, saya ingin konsultasi layanan {$progObj->title}.");
                    @endphp
                    <div class="program-card" style="background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 14px rgba(234, 88, 12, 0.06); transition: transform 0.3s ease, box-shadow 0.3s ease;">
                        <div class="program-body" style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                                <span style="background: #fff7ed; color: #ea580c; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; border: 1px solid #fed7aa;">
                                    {{ $progObj->badge ?? 'Layanan Resmi SLF' }}
                                </span>
                                <span style="font-size: 0.78rem; font-weight: 700; color: #64748b;">
                                    <i class="bi bi-clock-history" style="color: #ea580c;"></i> {{ $progObj->duration ?? '7-14 Hari Kerja' }}
                                </span>
                            </div>

                            <h3 class="program-title" style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px; line-height: 1.4;">
                                <a href="{{ $detailUrl }}" style="color: inherit; text-decoration: none;">{{ $progObj->title }}</a>
                            </h3>

                            <p class="program-desc" style="font-size: 0.86rem; color: #64748b; line-height: 1.6; margin-bottom: 18px; flex-grow: 1;">
                                {{ Str::limit($progObj->short_description ?? ($progObj->full_description ?? ''), 130) }}
                            </p>

                            <div style="font-size: 0.78rem; color: #9a3412; background: #fff7ed; border: 1px solid #fed7aa; padding: 8px 12px; border-radius: 8px; margin-bottom: 18px;">
                                <strong><i class="bi bi-patch-check-fill" style="color: #ea580c;"></i> Output:</strong> {{ Str::limit($progObj->certification ?? 'Sertifikat Laik Fungsi (SLF) Resmi & Laporan Kajian Teknis', 75) }}
                            </div>

                            <div class="program-footer-btn" style="display: flex; gap: 8px; padding-top: 14px; border-top: 1px solid #f1f5f9;">
                                <a href="{{ $detailUrl }}" class="btn-card-detail" style="flex: 1; text-align: center; background: #f8fafc; color: #0f172a; padding: 9px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 6px; border: 1px solid #cbd5e1; text-decoration: none;">
                                    <i class="bi bi-info-circle"></i> Detail Teknis
                                </a>
                                <a href="{{ $directWa }}" target="_blank" class="btn-card-wa" style="flex: 1; text-align: center; background: linear-gradient(135deg, #ea580c 0%, #f97316 100%); color: #ffffff; padding: 9px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 6px; text-decoration: none; border: 1px solid #fed7aa;">
                                    <i class="bi bi-whatsapp" style="color: #25d366;"></i> Ajukan SLF
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

            <div style="text-align: center; margin-top: 36px;">
                <a href="{{ route('programs') }}" style="background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%); color: #ffffff; padding: 12px 28px; border-radius: 50px; font-size: 0.88rem; font-weight: 800; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; border: 1px solid #fed7aa; box-shadow: 0 4px 14px rgba(234, 88, 12, 0.25);">
                    <i class="bi bi-collection-fill" style="color: #facc15;"></i> Buka Katalog Seluruh 8 Layanan Jasa SLF
                </a>
            </div>
        </div>
    </section>

    <!-- SECTION 4: KEUNGGULAN (MODERN INTERACTIVE CARDS) -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-shield-check" style="color: #ea580c;"></i> Mengapa Memilih Kami
                </span>
                <h2 class="section-title">Keunggulan Layanan Jasa SLF Bangunan Gedung</h2>
                <p class="section-desc">
                    Kepercayaan lebih dari 1.200 pengembang properti, kawasan industri, dan BUMN dibangun di atas integritas kajian teknis, instrumen uji presisi, dan kepastian hukum sertifikat.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-patch-check-fill" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Lembaga Pengkaji Terakreditasi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Sertifikat Laik Fungsi (SLF) yang diterbitkan memiliki legalitas resmi berkekuatan hukum, dilengkapi barcode validasi digital untuk kepatuhan perizinan dan asuransi gedung.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-tools" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Instrumen Uji NDT Terkalibrasi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Pemeriksaan menggunakan peralatan modern (Schmidt Rebound Hammer, Ultrasonic Pulse Velocity, Rebar Scanner, Pitot Gauge, Sound Level Meter) dengan kalibrasi laboratorium KAN.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-people-fill" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Tenaga Ahli Bersertifikat Kompetensi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Didukung tim ahli pengkaji teknis berlatar belakang Magister/Sarjana Teknik Sipil, Arsitektur, Mekanikal, dan Elektrikal dengan sertifikat keahlian jenjang Madya dan Utama.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-clock-history" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Proses Terukur & Efisien</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Metodologi audit yang terencana memungkinkan penerbitan Buku Laporan Kajian Teknis dan Sertifikat SLF selesai dalam 7 hingga 14 hari kerja setelah verifikasi lapangan tuntas.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-geo-alt-fill" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Jangkauan 38 Provinsi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Jaringan perwakilan tim tenaga ahli kami siap hadir langsung di lokasi pabrik, kawasan industri, pertambangan, dan gedung komersial Anda di seluruh pelosok Indonesia.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(234, 88, 12, 0.1); color: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-shield-fill-exclamation" style="color: #ea580c;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 10px;">Mitigasi Bencana Gedung</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Audit kami memberikan rekomendasi rekayasa preventif guna mencegah bahaya keruntuhan struktur gempa dan kebakaran demi mewujudkan Zero Building Disaster.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: ARTIKEL DAERAH (3 CARD DILIMIT) -->
    <section class="section-py" id="artikel" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-journal-text" style="color: #ea580c;"></i> Publikasi Teknis & Panduan
                </span>
                <h2 class="section-title">Artikel & Panduan Sertifikat Laik Fungsi (SLF)</h2>
                <p class="section-desc">
                    Rujukan teknis otoritatif seputar audit keandalan struktur bangunan gedung, uji NDT beton, proteksi kebakaran hydrant sprinkler, dan prosedur perpanjangan SLF berkala.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 26px;">
                @foreach($articles as $art)
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
                        <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                                <span style="background: #fff7ed; color: #ea580c; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">
                                    {{ $art->category ?? 'Jasa SLF' }}
                                </span>
                                <span style="font-size: 0.78rem; color: #64748b;">
                                    <i class="bi bi-clock"></i> {{ $art->read_time ?? 24 }} Menit Baca
                                </span>
                            </div>

                            <h3 style="font-size: 1.12rem; font-weight: 800; color: #0f172a; margin-bottom: 12px; line-height: 1.45;">
                                <a href="{{ route('article.detail', $art->slug) }}" style="color: inherit; text-decoration: none;">{{ $art->title }}</a>
                            </h3>

                            <p style="font-size: 0.86rem; color: #64748b; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">
                                {{ Str::limit($art->excerpt, 140) }}
                            </p>

                            <div style="padding-top: 14px; border-top: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; font-weight: 700; color: #9a3412;">
                                    <i class="bi bi-person-fill" style="color: #ea580c;"></i> {{ Str::limit($art->author ?? 'Tim Ahli SLF', 24) }}
                                </span>
                                <a href="{{ route('article.detail', $art->slug) }}" style="font-size: 0.82rem; font-weight: 800; color: #ea580c; display: inline-flex; align-items: center; gap: 4px; text-decoration: none;">
                                    Baca Panduan <i class="bi bi-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

            <div style="text-align: center; margin-top: 36px;">
                <a href="{{ route('articles') }}" style="background: #ffffff; color: #ea580c; border: 2px solid #ea580c; padding: 12px 28px; border-radius: 50px; font-size: 0.88rem; font-weight: 800; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                    <i class="bi bi-newspaper" style="color: #ea580c;"></i> Buka Seluruh Direktori Artikel Daerah
                </a>
            </div>
        </div>
    </section>

    <!-- SECTION 6: STATISTIK PENCAPAIAN KINERJA -->
    <section class="section-py" style="background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%); color: #ffffff;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 26px; text-align: center;">
                @foreach($statistics as $stat)
                    <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(249, 115, 22, 0.2); border-radius: 16px; padding: 32px 20px;">
                        <div style="font-size: 2.2rem; margin-bottom: 8px; color: #fb923c;">
                            <i class="bi {{ $stat->icon ?? 'bi-patch-check-fill' }}"></i>
                        </div>
                        <div style="font-size: 2.35rem; font-weight: 800; color: #ffffff; margin-bottom: 6px; letter-spacing: -1px;">
                            {{ $stat->value }}
                        </div>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #fed7aa; margin-bottom: 4px;">
                            {{ $stat->label }}
                        </div>
                        <div style="font-size: 0.78rem; color: #cbd5e1;">
                            {{ $stat->description }}
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- SECTION 7: MITRA PENGEMBANG & BUMN -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header" style="margin-bottom: 36px;">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-building-check" style="color: #ea580c;"></i> Kepercayaan Industri Properti
                </span>
                <h2 class="section-title">Mitra Sinergi Sektor Konstruksi, Properti & Industri</h2>
                <p class="section-desc">
                    Mendukung keandalan fisik bangunan dan penerbitan Sertifikat Laik Fungsi di berbagai proyek pengembang BUMN, kawasan industri, dan korporasi properti nasional:
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                @foreach($partners as $partner)
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; display: flex; flex-direction: column;">
                        <div style="font-weight: 800; color: #0f172a; font-size: 0.98rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
                            <i class="bi bi-check2-circle" style="color: #ea580c;"></i> {{ $partner['name'] }}
                        </div>
                        <div style="font-size: 0.78rem; color: #64748b; line-height: 1.5;">
                            {{ $partner['role'] }}
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- SECTION 8: FAQ ACCORDION -->
    <section class="section-py" style="background: #f8fafc;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fff7ed; color: #ea580c; border-color: #fed7aa;">
                    <i class="bi bi-question-circle-fill" style="color: #ea580c;"></i> Tanya Jawab Resmi
                </span>
                <h2 class="section-title">Pertanyaan Seputar Jasa SLF & Sertifikasi Gedung</h2>
                <p class="section-desc">
                    Informasi penting mengenai legalitas, persyaratan dokumen teknis, dan tahapan audit kelaikan fungsi bangunan gedung:
                </p>
            </div>

            <div style="max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 14px;">
                @foreach($faqs as $i => $faq)
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                        <h3 style="font-size: 1.05rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; display: flex; align-items: flex-start; gap: 10px;">
                            <span style="color: #ea580c; font-weight: 800;">Q{{ $i + 1 }}.</span>
                            <span>{{ $faq->question }}</span>
                        </h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.65; margin-left: 28px;">
                            {{ $faq->answer }}
                        </p>
                    </div>
                @endforeach
            </div>
        </div>
    </section>
@endsection

@push('scripts')
<script>
    (function() {
        // ==========================================
        // HOME DIREKTORI WILAYAH ACCORDION & EXPLORER
        // ==========================================
        const regionsData = @json($regionsExplorerData ?? []);

        // 1. Accordion Toggle for Province Cards
        document.querySelectorAll('.prov-header-toggle').forEach(header => {
            header.addEventListener('click', function(e) {
                if (e.target.closest('a')) return;

                const card = this.closest('.home-province-card');
                const drawer = card.querySelector('.prov-drawer-body');
                const chevron = card.querySelector('.toggle-chevron');
                const toggleText = card.querySelector('.toggle-text');
                const isOpen = drawer.style.display === 'block';

                if (isOpen) {
                    drawer.style.display = 'none';
                    if (chevron) chevron.style.transform = 'rotate(0deg)';
                    if (toggleText) {
                        toggleText.textContent = 'Lihat Kab/Kot & Kec';
                        toggleText.style.color = '#64748b';
                    }
                    this.classList.remove('is-open');
                } else {
                    drawer.style.display = 'block';
                    if (chevron) chevron.style.transform = 'rotate(180deg)';
                    if (toggleText) {
                        toggleText.textContent = 'Sembunyikan';
                        toggleText.style.color = '#ea580c';
                    }
                    this.classList.add('is-open');
                }
            });
        });

        // 2. Expand All & Collapse All
        const btnExpandAll = document.getElementById('btnExpandAllProvs');
        const btnCollapseAll = document.getElementById('btnCollapseAllProvs');

        if (btnExpandAll) {
            btnExpandAll.addEventListener('click', () => {
                document.querySelectorAll('.prov-drawer-body').forEach(d => d.style.display = 'block');
                document.querySelectorAll('.toggle-chevron').forEach(c => c.style.transform = 'rotate(180deg)');
                document.querySelectorAll('.toggle-text').forEach(t => {
                    t.textContent = 'Sembunyikan';
                    t.style.color = '#ea580c';
                });
                document.querySelectorAll('.prov-header-toggle').forEach(h => h.classList.add('is-open'));
            });
        }
        if (btnCollapseAll) {
            btnCollapseAll.addEventListener('click', () => {
                document.querySelectorAll('.prov-drawer-body').forEach(d => d.style.display = 'none');
                document.querySelectorAll('.toggle-chevron').forEach(c => c.style.transform = 'rotate(0deg)');
                document.querySelectorAll('.toggle-text').forEach(t => {
                    t.textContent = 'Lihat Kab/Kot & Kec';
                    t.style.color = '#64748b';
                });
                document.querySelectorAll('.prov-header-toggle').forEach(h => h.classList.remove('is-open'));
            });
        }

        // 3. Island Filter Tabs
        const islandTabs = document.querySelectorAll('.island-tab-btn');
        const islandGroups = document.querySelectorAll('.island-group-block');

        islandTabs.forEach(tab => {
            tab.addEventListener('click', function() {
                islandTabs.forEach(t => {
                    t.style.background = '#f8fafc';
                    t.style.borderColor = '#cbd5e1';
                    t.style.color = '#475569';
                    t.classList.remove('active');
                });
                this.style.background = 'linear-gradient(135deg, #ea580c 0%, #f97316 100%)';
                this.style.borderColor = '#ea580c';
                this.style.color = '#ffffff';
                this.classList.add('active');

                const targetIsland = this.getAttribute('data-island');
                islandGroups.forEach(grp => {
                    if (targetIsland === 'all' || grp.getAttribute('data-island') === targetIsland) {
                        grp.style.display = 'block';
                    } else {
                        grp.style.display = 'none';
                    }
                });
            });
        });

        // Helper slugify
        function slugify(text) {
            return text.toString().toLowerCase()
                .replace(/\\s+/g, '-')
                .replace(/[^\\w\\-]+/g, '')
                .replace(/\\-\\-+/g, '-')
                .replace(/^-+/, '')
                .replace(/-+$/, '');
        }

        // 4. Cascading Selectors (Prov -> Kabkot -> Kecamatan)
        const homeProvSelect = document.getElementById('homeProvSelect');
        const homeKabkotSelect = document.getElementById('homeKabkotSelect');
        const homeKecamatanSelect = document.getElementById('homeKecamatanSelect');
        const homeGoBtn = document.getElementById('homeGoRegionBtn');

        if (homeProvSelect && homeKabkotSelect && homeKecamatanSelect && homeGoBtn) {
            homeProvSelect.addEventListener('change', function() {
                const pSlug = this.value;
                homeKabkotSelect.innerHTML = '<option value="">-- Pilih Kabupaten / Kota --</option>';
                homeKecamatanSelect.innerHTML = '<option value="">-- Pilih Kecamatan --</option>';
                homeKecamatanSelect.disabled = true;

                if (!pSlug || !regionsData[pSlug]) {
                    homeKabkotSelect.disabled = true;
                    return;
                }

                homeKabkotSelect.disabled = false;
                const kabkots = regionsData[pSlug].kabkot || [];
                kabkots.forEach(k => {
                    const opt = document.createElement('option');
                    opt.value = k.slug;
                    opt.textContent = k.name;
                    homeKabkotSelect.appendChild(opt);
                });
            });

            homeKabkotSelect.addEventListener('change', function() {
                const pSlug = homeProvSelect.value;
                const kSlug = this.value;
                homeKecamatanSelect.innerHTML = '<option value="">-- Pilih Kecamatan --</option>';

                if (!kSlug || !regionsData[pSlug]) {
                    homeKecamatanSelect.disabled = true;
                    return;
                }

                const kabkot = (regionsData[pSlug].kabkot || []).find(k => k.slug === kSlug);
                if (!kabkot || !kabkot.kecamatan || kabkot.kecamatan.length === 0) {
                    homeKecamatanSelect.disabled = true;
                    return;
                }

                homeKecamatanSelect.disabled = false;
                kabkot.kecamatan.forEach(kc => {
                    const kcName = typeof kc === 'string' ? kc : kc.name;
                    const kcSlug = typeof kc === 'string' ? slugify(kc) : kc.slug;
                    const opt = document.createElement('option');
                    opt.value = kcSlug;
                    opt.textContent = 'Kec. ' + kcName;
                    homeKecamatanSelect.appendChild(opt);
                });
            });

            homeGoBtn.addEventListener('click', function() {
                const pSlug = homeProvSelect.value;
                const kSlug = homeKabkotSelect.value;
                const kcSlug = homeKecamatanSelect.value;

                if (!pSlug) {
                    alert('Silakan pilih provinsi terlebih dahulu.');
                    return;
                }

                if (kcSlug) {
                    window.location.href = `/wilayah/${pSlug}/${kSlug}/${kcSlug}`;
                } else if (kSlug) {
                    window.location.href = `/wilayah/${pSlug}/${kSlug}`;
                } else {
                    window.location.href = `/wilayah/${pSlug}`;
                }
            });
        }

        // 5. Live Search Input
        const liveSearchInput = document.getElementById('homeLiveRegionSearch');
        const searchResultsBox = document.getElementById('homeSearchResultsBox');

        if (liveSearchInput && searchResultsBox) {
            liveSearchInput.addEventListener('input', function() {
                const q = this.value.toLowerCase().trim();
                if (q.length < 2) {
                    searchResultsBox.style.display = 'none';
                    searchResultsBox.innerHTML = '';
                    return;
                }

                let matches = [];
                Object.values(regionsData).forEach(p => {
                    (p.kabkot || []).forEach(k => {
                        if (k.name.toLowerCase().includes(q)) {
                            matches.push({
                                type: 'Kabupaten/Kota',
                                label: k.name + ' (' + p.name + ')',
                                url: `/wilayah/${p.slug}/${k.slug}`,
                                badge: 'Kab/Kot'
                            });
                        }
                        (k.kecamatan || []).forEach(kc => {
                            const kcName = typeof kc === 'string' ? kc : kc.name;
                            const kcSlug = typeof kc === 'string' ? slugify(kc) : kc.slug;
                            if (kcName.toLowerCase().includes(q)) {
                                matches.push({
                                    type: 'Kecamatan',
                                    label: 'Kec. ' + kcName + ', ' + k.name + ' (' + p.name + ')',
                                    url: `/wilayah/${p.slug}/${k.slug}/${kcSlug}`,
                                    badge: 'Kecamatan'
                                });
                            }
                        });
                    });
                });

                if (matches.length === 0) {
                    searchResultsBox.innerHTML = '<div style="padding: 12px; color: #64748b; font-size: 0.85rem; text-align: center;">Tidak ada wilayah yang cocok dengan "' + q + '"</div>';
                    searchResultsBox.style.display = 'block';
                    return;
                }

                let html = '<div style="font-size: 0.74rem; font-weight: 700; color: #ea580c; padding: 6px 10px; border-bottom: 1px solid #f1f5f9;">Ditemukan ' + matches.length + ' wilayah terkait:</div>';
                matches.slice(0, 15).forEach(m => {
                    html += `
                        <a href="${m.url}" style="padding: 9px 12px; display: flex; align-items: center; justify-content: space-between; text-decoration: none; color: #1e293b; font-size: 0.84rem; border-bottom: 1px solid #f8fafc; transition: background 0.15s ease;">
                            <span><i class="bi bi-geo-alt-fill" style="color: #ea580c; margin-right: 6px;"></i> ${m.label}</span>
                            <span style="font-size: 0.7rem; font-weight: 700; color: #c2410c; background: #fff7ed; padding: 2px 6px; border-radius: 4px; border: 1px solid #fed7aa;">${m.badge}</span>
                        </a>
                    `;
                });
                if (matches.length > 15) {
                    html += '<div style="padding: 8px; text-align: center; font-size: 0.75rem; color: #64748b;">...dan ' + (matches.length - 15) + ' wilayah lainnya.</div>';
                }

                searchResultsBox.innerHTML = html;
                searchResultsBox.style.display = 'block';
            });

            // Close on click outside
            document.addEventListener('click', function(e) {
                if (!e.target.closest('#homeLiveRegionSearch') && !e.target.closest('#homeSearchResultsBox')) {
                    searchResultsBox.style.display = 'none';
                }
            });
        }
    })();
</script>
@endpush
"""

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated front/index.blade.php with full PUBT-style wilayah directory structure!")
