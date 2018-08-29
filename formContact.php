<?php

$name = $_POST['name'];
$email = $_POST['email'];

$file = fopen("contact.txt", "a") or die ("file not open");

$f = $name." , ".$email;
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>
