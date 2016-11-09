<?php
	function dtm(\DateTime $dateTime)
	{
		$secs = $dateTime->getTimestamp(); // Gets the seconds
		$millisecs = $secs*1000; // Converted to milliseconds
		$millisecs += $dateTime->format("u")/1000; // Microseconds converted to seconds
		return $millisecs;
	}
	
	$file = fopen("ranking.txt", "r") or die("Error!");
	if(file_exists('stop-script')) {
		echo 'Status: Stopped<br>';
	} else {
		echo 'Status: Running<br>';
	}
	echo "Ranking:<br>";
	while(!feof($file)) {
		$arr = explode("|", substr(fgets($file),3));
		$team = $arr[0];
		$date = $arr[1];
		if(substr($team,0,1) == "1") {
			$master_date = new DateTime($date);
		} else {
			$second_date = new DateTime($date);
		}
		if(substr($team,0,1) >= "2") {
			$echo = number_format(Round((dtm($second_date)-dtm($master_date))/1000,3),3);
		}
		//echo substr(fgets($file),3,-28)."<br>";
		echo "<br>".$team/*." ".$date*/; if(isset($echo)) {echo " +".$echo."s"; }
	}
	fclose($file);	
?>
