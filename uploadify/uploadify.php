<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="refresh" content="3;url=index.html"> 
<title>無標題文件</title>
<style>
        body{
            font: 14pt Arial, sans-serif; 
            background: lightgrey; 
            text-align: center; 
            margin-top: 12pt;}
        
        
        
</style>
</head>

<body>
<?php
/*
Uploadify
Copyright (c) 2012 Reactive Apps, Ronnie Garcia
Released under the MIT License <http://www.opensource.org/licenses/mit-license.php> 
*/

// Define a destination
$targetFolder = '/AudioAssV20/InputFile'; // Relative to the root

$verifyToken = md5('unique_salt' . $_POST['timestamp']);

if (!empty($_FILES) && $_POST['token'] == $verifyToken) {
	$tempFile = $_FILES['Filedata']['tmp_name'];
	
	$targetPath = $_SERVER['DOCUMENT_ROOT'] . $targetFolder;
	
		if(substr(strrchr($_FILES['Filedata']['name'],'.'),1)=="wav")
			$_FILES['Filedata']['name']="Sample.wav";
		if(substr(strrchr($_FILES['Filedata']['name'],'.'),1)=="mp3")
			$_FILES['Filedata']['name']="Sample.mp3";
			
	$targetFile = rtrim($targetPath,'/') . '/' . $_FILES['Filedata']['name'];
	
	// Validate the file type
	$fileTypes = array('jpg','jpeg','gif','png','wav','mp3'); // File extensions
	$fileParts = pathinfo($_FILES['Filedata']['name']);
	
	if (in_array($fileParts['extension'],$fileTypes)) {
		
		move_uploaded_file($tempFile,$targetFile);
		
                $aCommand= 'c:/Python32/python.exe ./PyPraat/ryPraat001.py ' .$targetFile;
                $aReturn= system($aCommand, $aParam);
                echo '<p>'; 
                //echo '<br>aCommand= '  .$aCommand;
                //echo '<br>aParam= '    .$aParam;
                //echo '<br>aReturn= '   .$aReturn;
				echo '<br>檔案上傳成功';
				echo '<br>頁面轉載中...';
                echo '</p>'; 
        
	} else {
		echo 'Invalid file type.';
	}
	
}
?>
</body>
</html>