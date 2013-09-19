<html>
	<head>
 		<META http-equiv="refresh" content="1"/>
	</head>
<body>
<?php echo '<h1> Brew Control</h1>'; ?>

	<?php
	$xmlfile = "/tmp/BrewStatePipe";
	
	$xmldoc = simplexml_load_file($xmlfile);
	
	//need to determine if any actions required
		
	
?>
<table>
	<tr>
		<td>Temp:</td>
		<td><?= $xmldoc->temperature?></td>
	</tr>
	<tr>
		<td colspan="2" style="background-color: <?php if ($xmldoc->heater==1) { echo"red"; } else {echo "white";}  ?>"> Heater</td>
	
	</tr>
<?php
	if ($xmldoc->action != null )
	{
		$userAction = $xmldoc->action;
		if (file_exists("/tmp/" . $userAction))
		{
			echo "<tr>";
	
			echo "<td onclick='navigate('http://raspberrypi?Action=" . $userAction . "?>')'> Press to Action " . $userAction . " </td>	";
			
			echo "</tr>";
		}


	}
	
?>
 </table>


</body>
</html>