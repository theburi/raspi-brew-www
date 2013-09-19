<html>
	<head>
 		<META http-equiv="refresh" content="1"/>
	</head>
<body>
<?php echo '<h1> Brew Control</h1>'; ?>

<?php
	$xmlfile = "/tmp/BrewStatePipe";
	
	$xmldoc = simplexml_load_file($xmlfile);
	
	echo "Temperature: " . $xmldoc->temperature;
	echo "Heater: " . $xmldoc->heater;
 ?>
 


</body>
</html>