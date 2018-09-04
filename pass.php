<?php

$username = $_POST['username'];
$password = $_POST['password'];
$hash = password_hash($password, PASSWORD_BCRYPT);

$file = fopen("pass.txt", "a") or die ("file not open");

$f = $username." , ".$hash."\n";
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>