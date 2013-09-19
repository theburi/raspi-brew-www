<html>
	<head>
 		<META http-equiv="refresh" content="2"/>
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
		<td>Step:</td>
		<td><?= $xmldoc->step?> C</td>
	</tr>
	<tr>
		<td>Temp:</td>
		<td><?= $xmldoc->temperature?> C</td>
	</tr>
	<tr>
		<td colspan="2" style="background-color: <?php if ($xmldoc->heater==1) { echo"red"; } else {echo "white";}  ?>"> Heater</td>
	
	</tr>
<?php
	if ($xmldoc->action != '' )
	{
		$userAction = $xmldoc->action;
		if (!gifile_exists("/tmp/" . $userAction))
		{
			echo "<tr>";
	
			echo "<td onclick=\'navigate(\'http://raspberrypi?Action=" . $userAction . "\')\'> Press to Action " . $userAction . " </td>	";
			
			echo "</tr>";
		}


	}
	
?>
 </table>


</body>
</html>