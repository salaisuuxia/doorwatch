<?php

$db_username="";
$db_password="";
$database="homelog";


$link = mysql_connect("localhost",$db_username,$db_password);
if (!$link) {
    die('Could not connect: ' . mysql_error());
}


$type=mysql_real_escape_string($_POST["type"]);




$db_selected = mysql_select_db($database, $link);

if (!$db_selected) {
  // If we couldn't, then it either doesn't exist, or we can't see it.
  $query = 'CREATE DATABASE $database';

  if (mysql_query($query, $link)) {
      echo "Database my_db created successfully\n";
  } else {
      echo 'Error creating database: ' . mysql_error() . "\n";
  }
}



$query="CREATE TABLE IF NOT EXISTS log (date text, time text, type text, flagged text)"
mysql_query($query);


$date=date("d/m/y");
$time=date("H:i:s");

$query="INSERT INTO  `homelog`.`log` ( `date` , `time` , `type`  ) VALUES ( '$date',  '$time',  '$type');";
mysql_query($query);
?>
