<?php

/* counter */

//opens countlog.txt to read the number of hits
$datei = fopen("countlog.txt","a");
$count = fgets($datei,1000);
fclose($datei);
$count=$count + 1 ;
echo "$count" ;
echo " hits" ;
echo "\n" ;

// opens countlog.txt to change new hit number
$datei = fopen("countlog.txt","w");
fwrite($datei, $count);
fclose($datei);

$file = fopen("ip.txt","a");
$ip=$_SERVER['REMOTE_ADDR'];
echo $ip;
echo fwrite($file,$ip);
fclose($file);

?>