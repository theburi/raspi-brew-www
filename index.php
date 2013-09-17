<html>
<body>
<?php echo '<h1> Hello World Git</h1>'; ?>

<?php
	$xmlstr = "<state><temperature>10</temperature></state>";
	
	$xmldoc = new SimpleXMLElement($xmlstr);
	
	echo "Temperature: " . $xmldoc->temperature;
 ?>
</body>
</html>