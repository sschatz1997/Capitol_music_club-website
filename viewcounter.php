<?php

/* counter */
// opens countlog.txt to change new hit number

//opens countlog.txt to read the number of hits
/*$datei = fopen("countlog.txt","a");
$count = fgets($datei,1000);
fclose($datei);
$count=$count + 1 ;
echo "$count" ;
echo " hits" ;
echo "\n" ;

$datei = fopen("countlog.txt","w");
fwrite($datei, $count);
fclose($datei);*/

$ip = $_SERVER['REMOTE_ADDR'];

$file = "ip.txt";
$content = file_get_contents($file);
$content .= $ip . "\n";
file_put_contents($file, $content);


?>