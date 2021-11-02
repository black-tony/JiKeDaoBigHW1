query.php
<?php 
header('Content-type:text/html;charset=utf8');
$conn = @ mysql_connect("localhost", "root", "Gz8ymJMXfbr#3*5") or die("datebase can`t been connected");
mysql_select_db("bighw1", $conn);
mysql_query("set names 'utf8'"); //
class Danmu 
{
    public $text;
    public $color;
    public $size;
    public $position;
    public $time;
}
$data = array();
$sql="SELECT text,color,size,position,time FROM `danmakuinfo`";
$result =mysql_query($sql);
while($row= mysql_fetch_array($result, MYSQL_ASSOC)){
    $danmu = new Danmu();
    $danmu->text = $row["text"];
    $danmu->color = $row["color"];
    $danmu->size = $row["size"];
    $danmu->position = $row["position"];
    $danmu->time = $row["time"];
    $data[]=$danmu;
}   
echo json_encode($data);

?>