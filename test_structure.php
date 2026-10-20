<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$app->make(\Illuminate\Contracts\Console\Kernel::class)->bootstrap();
$p = \App\Services\RegionService::getAllProvinces();
$firstKey = array_key_first($p);
echo 'First key: ' . $firstKey . PHP_EOL;
echo 'Keys of first province: ' . implode(', ', array_keys($p[$firstKey])) . PHP_EOL;
echo 'Is kabkot array: ' . (is_array($p[$firstKey]['kabkot']) ? 'yes' : 'no') . PHP_EOL;
echo 'Kabkot count: ' . count($p[$firstKey]['kabkot']) . PHP_EOL;
echo 'First kabkot type: ' . gettype($p[$firstKey]['kabkot'][0]) . PHP_EOL;
if (is_array($p[$firstKey]['kabkot'][0])) {
    echo 'First kabkot keys: ' . implode(', ', array_keys($p[$firstKey]['kabkot'][0])) . PHP_EOL;
    print_r($p[$firstKey]['kabkot'][0]);
} else {
    echo 'First kabkot value: ' . $p[$firstKey]['kabkot'][0] . PHP_EOL;
}
