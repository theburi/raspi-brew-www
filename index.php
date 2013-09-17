<html>
<body>
<?php echo '<h1> Brew Control</h1>'; ?>

<?php
	$xmlstr = "<state><temperature>10</temperature></state>";
	
	$xmldoc = new SimpleXMLElement($xmlstr);
	
	echo "Temperature: " . $xmldoc->temperature;
 ?>
 
 <?php
//Open pipe and write some text to it.
//Mode must be r+ or fopen will get stuck.
$pipe = fopen('testpipe','r+');
$pipeoutput= fread($pipe, filesize($filename));
fclose($pipe);
echo $pipeoutput;
?>

</body>
</html>