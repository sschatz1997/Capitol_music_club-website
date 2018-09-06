<?php

$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$username = $_POST['username'];
$password = $_POST['password'];
$hash = password_hash($password, PASSWORD_BCRYPT);

$file = fopen("pass.txt", "a") or die ("file not open");

$f = $first_name." , ".$last_name." , ".$username." , ".$hash. "\n";
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>