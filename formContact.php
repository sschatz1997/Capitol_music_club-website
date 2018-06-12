<?php

$name = $_POST['name'];
$email = $_POST['email'];

$file = fopen("contact.txt", "w+") or die ("file not open");
$f = $name.",".$email."\n";
fputs($file,$f) or die ("no data was written");

$line = date('Y-m-d H:i:s') . " - $_SERVER[REMOTE_ADDR]";
file_put_contents('visitors.log', $line . PHP_EOL, FILE_APPEND);

fclose($file);
header("Location: http://10.0.54.169/Redirect.html"); 
exit();
?>