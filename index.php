<html>
	<head>
 		<META http-equiv="refresh" content="1"/>
	</head>
<body>
<?php echo '<h1> Brew Control</h1>'; ?>

	<?php
	$xmlfile = "/tmp/BrewStatePipe";
	
	$xmldoc = simplexml_load_file($xmlfile);
?>
<table>
	<tr>
		<td>Temp:</td>
		<td><?= $xmldoc->temperature?></td>
	</tr>
	<tr>
		<td colspan="2" style="background-color: <?php if ($xmldoc->heater==1) { echo"red"; } else {echo "white";}  ?>"> Heater</td>
	
	</tr>
 </table>


</body>
</html>