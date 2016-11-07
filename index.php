<html>
<head>
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
	 
	$(function() {
	 
		getStatus();
	 
	});
	 
	function getStatus() {
	 
		$('div#text-file-container').load('loadtxt.php');
		setTimeout("getStatus()",1000);
	 
	}
	
	function stopLoad() {
		window.stop();
		document.execCommand("Stop");
	}
	
	function reload() {
		$(document).load('start.php');
	}
	
	function stop() {
		$(document).load('stop.php');
	}
	 
	</script>
</head>
<body>
	<?php
	echo '<button onclick="reload()">Start</button>';
	echo '<button onclick="stop()">Stop</button><br><br>';
	ob_flush();
	#passthru('sudo /usr/bin/python2.7 /home/pi/python_scripts/buzzer.py');
	#$command = escapeshellcmd("/home/pi/python_scripts/buzzer.py");
	#shell_exec($command);
	#$command = "sudo /usr/bin/python2.7 /home/pi/python_scripts/buzzer.py";
	#exec($command, $output);
	?>
	<table style="border: solid 1px black">
		<tr>
			<td>
				<div id="text-file-container"></div>
			</td>
		</tr>
	</table>
</body>
</html>
