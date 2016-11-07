<?php
	$file = fopen("ranking.txt", "r") or die("Error!");
	if(file_exists('stop-script')) {
		echo 'Status: Stopped<br>';
	} else {
		echo 'Status: Running<br>';
	}
	echo "Ranking:<br>";
	while(!feof($file)) {
		echo substr(fgets($file),3)."<br>";
	}
	fclose($file);
?>
