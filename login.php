<?php
    $dir = '/root/disk3/password_main.sqlite';
    $dbh = new PDO($dir) or die ("cannot open");
    $password = stripslashes($password);
    $username = $_POST['username'];
    $hash = password_verify[$password, PASSWORD_BCRYPT];
	$password = $hash
    $username = stripslashes($username);
    $query = "SELECT * FROM password_main.sqlite WHERE username='$username' AND password='$password'";
    $result = mysql_query($query);
    $count = mysql_num_rows($result);

    if($count==1){
    echo'loged on';
    }
	
	header("Location: http://10.1.121.102/Redirect.html"); 
	exit();
?>