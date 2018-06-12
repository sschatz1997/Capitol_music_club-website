<?php

$name = $_POST['name'];
$email = $_POST['email'];

$file = fopen("contact.txt", "a") or die ("file not open");

$f = $name." , ".$email."\n";
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.0.54.169/Redirect.html"); 
exit();
?>