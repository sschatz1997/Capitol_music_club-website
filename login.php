<?php
    $dir = '/root/disk3/password_main.sqlite';
    $dbh = new PDO($dir) or die ("cannot open");

    $myusername = $_POST['username'];
    $mypassword = $_POST['password'];

    $myusername = stripslashes($username);
    $mypassword = stripslashes($password);

    $query = "SELECT * FROM password_main.sqlite WHERE username='$myusername' AND password='$mypassword'";
    $result = mysql_query($query);
    $count = mysql_num_rows($result);

    if($count==1){
    echo'loged on';
    }
	
	if($count!=1){
	echo'no user found. do you have an account?';
	}
	header("Location: http://10.1.121.102/Redirect.html"); 
	exit();
?>