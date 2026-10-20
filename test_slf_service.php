<?php

require __DIR__ . '/vendor/autoload.php';
$app = require_once __DIR__ . '/bootstrap/app.php';

use App\Services\JasaSlfSchemeService;

$programs = JasaSlfSchemeService::getMasterPrograms();
echo "Total programs: " . count($programs) . PHP_EOL;
foreach ($programs as $i => $p) {
    echo ($i + 1) . ". [" . $p['slug'] . "] " . $p['title'] . PHP_EOL;
}

$titles = JasaSlfSchemeService::get200ArticleTitles();
echo PHP_EOL . "Total titles: " . count($titles) . PHP_EOL;
echo "Title 1: " . $titles[0] . PHP_EOL;
echo "Title 2: " . $titles[1] . PHP_EOL;
echo "Title 200: " . $titles[199] . PHP_EOL;

$art = JasaSlfSchemeService::generateDeepArticle('Training Jasa SLF: Panduan Lengkap Sertifikat Laik Fungsi Bangunan Gedung di DKI Jakarta', 'DKI Jakarta');
$wc = str_word_count(strip_tags($art['content']));
echo PHP_EOL . "Article Word Count: " . $wc . " words." . PHP_EOL;
