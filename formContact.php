<?php
if($_POST['submit']))
{

$name = $_POST['name'];
$email = $_POST['email'];

$file = fopen("contact.txt", "w+") or die ("file not open");

$f = $name.",".$email."\n";
fputs($file,$f) or die ("no data was written");

fclose($file);
}
?>