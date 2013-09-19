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
	echo "Action: " . $_GET['Action'];		
	if ($_GET['Action']!=null) 
	{
		file_put_contents("/tmp/" . $_GET['Action'], $_GET['Action']);
		chmod("/tmp/" . $_GET['Action'], 777);
	}

	
	
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

		if (!file_exists("/tmp/" . $userAction))
		{
			echo "<tr>";
			echo "<td>Action: </td>";
			echo "<td> <a href ='http://raspberrypi?Action=" . $userAction . "'> Press to " . $userAction . " </a> </td>	";
			
			echo "</tr>";
		}
		else {
			echo "<tr>";
			echo "<td>Action: </td>";
			echo "<td> submitting... </td>	";
			
			echo "</tr>";
			
		}


	}
	
?>
 </table>


</body>
</html>
