<?php 
    header('Content-type:text/html;charset=utf8');
    $conn = @ mysql_connect("localhost", "root", "Gz8ymJMXfbr#3*5") or die("datebase can`t been connected");
    mysql_select_db("danmu", $conn);
    mysql_query("set names 'utf8'"); //

    $table=$_POST['tb'];
    //$sql="INSERT INTO `danmu` VALUES ('".$danmu."')";
    $sql="INSERT INTO danmakuinfo(text,color,size,position,time) 
    VALUES (".$table.")";
    echo $sql;
    $query=mysql_query($sql);             
    echo $danmu;

?>