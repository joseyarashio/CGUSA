<?php
set_time_limit(900);
$targetFolder = '/CGUSA-master/InputFile'; // Relative to the root

$verifyToken = md5('unique_salt' . $_POST['timestamp']);

if (!empty($_FILES) && $_POST['token'] == $verifyToken) {
	$tempFile = $_FILES['Filedata']['tmp_name'];
	
	$targetPath = $_SERVER['DOCUMENT_ROOT'] . $targetFolder;
	
		if(substr(strrchr($_FILES['Filedata']['name'],'.'),1)=="wav")
			$_FILES['Filedata']['name']="Sample.wav";
		if(substr(strrchr($_FILES['Filedata']['name'],'.'),1)=="mp3")
			$_FILES['Filedata']['name']="Sample.mp3";
		if(substr(strrchr($_FILES['Filedata']['name'],'.'),1)=="txt")
			$_FILES['Filedata']['name']="Sample.txt";
			
	$targetFile = rtrim($targetPath,'/') . '/' . $_FILES['Filedata']['name'];
	
	// Validate the file type
	$fileTypes = array('wav','mp3','txt'); // File extensions
	$fileParts = pathinfo($_FILES['Filedata']['name']);
	
	if (in_array($fileParts['extension'],$fileTypes)) {
		
		move_uploaded_file($tempFile,$targetFile);
		
        //$aCommand= 'C:\WinPython-64bit-3.3.5.0\python-3.3.5.amd64\python.exe ./PyPraat/processSample.py';//執行Sample後處理
        //$aReturn= system($aCommand, $aParam);
		exec("python ./PyPraat/processSample.py", $output);
		var_dump( $output);
		
	} else {
		echo 'Invalid file type.';
	}
	
}
?>