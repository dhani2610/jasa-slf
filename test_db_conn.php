<?php
try {
    $pdo = new PDO('mysql:host=localhost;port=3306;dbname=db_jasa_slf', 'root', '');
    echo "Connected via localhost!" . PHP_EOL;
} catch (Exception $e) {
    echo "localhost error: " . $e->getMessage() . PHP_EOL;
}
try {
    $pdo2 = new PDO('mysql:host=127.0.0.1;port=3306;dbname=db_jasa_slf', 'root', '');
    echo "Connected via 127.0.0.1!" . PHP_EOL;
} catch (Exception $e) {
    echo "127.0.0.1 error: " . $e->getMessage() . PHP_EOL;
}
