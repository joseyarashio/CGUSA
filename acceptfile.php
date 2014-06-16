<?php

	if(!isset($_REQUEST['filename']))
	{
		exit('No file');
	}
	$myFile = "text2score.txt";
	$fh = fopen($myFile, 'w') or die("can't open file");
	$stringData = $_REQUEST['sentance'];
	fwrite($fh, $stringData);
	fclose($fh);
   
	$upload_path = dirname(__FILE__). '/recorderFile';
	$filename = $_REQUEST['filename'];
	$fp = fopen($upload_path."/".$filename.".wav", "wb");
   
	fwrite($fp, file_get_contents('php://input'));
	fclose($fp);
		//exec("python ./PyPraat/RecordAnalysis.py", $output);
		//$aCommand= 'C:\WinPython-64bit-3.3.5.0\python-3.3.5.amd64\python.exe ./PyPraat/doAnalysis.py ' ;
        exec("python ./PyPraat/doAnalysis.py", $output);
		var_dump( $output);
		
    exit('done');
	
?>