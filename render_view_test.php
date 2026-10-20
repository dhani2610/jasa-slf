<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(\Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$start = microtime(true);
try {
    $request = \Illuminate\Http\Request::create('/', 'GET');
    $response = $app->make(\Illuminate\Contracts\Http\Kernel::class)->handle($request);
    $end = microtime(true);
    echo "Status code: " . $response->getStatusCode() . PHP_EOL;
    echo "Time taken: " . round($end - $start, 3) . "s" . PHP_EOL;
    echo "Body length: " . strlen($response->getContent()) . " bytes" . PHP_EOL;
} catch (\Throwable $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
    echo $e->getTraceAsString() . PHP_EOL;
}
