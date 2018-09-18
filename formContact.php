<?php

$name = $_POST['name'];
$email = $_POST['email'];

$file1 = fopen("contact.txt", "a") or die ("file not open");

$f = $name." , ".$email;
fputs($file1,$f) or die ("no data was written");

fclose($file1);
header("Location: http://10.1.121.102/Redirect.html"); 
$ip = $_SERVER['REMOTE_ADDR'];

$file = "ip.txt";
$content = file_get_contents($file);
$content .= $ip;
file_put_contents($file, $content);

exit();
?>
