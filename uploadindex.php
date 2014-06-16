<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>UploadiFive Test</title>
<script src="uploadify/jquery.min.js" type="text/javascript"></script>
<script src="uploadify/jquery.uploadify.min.js" type="text/javascript"></script>
<link rel="stylesheet" type="text/css" href="uploadify/uploadify.css">
<style type="text/css">
body {
	font: 13px Arial, Helvetica, Sans-serif;
	background: lightgrey; 
    text-align: center; 
}
</style>
</head>

<body>
	<h1>上傳範例聲音檔(Files Uploading)</h1>
	<h3>請選擇您所想要當作練習的聲音檔(wav,mp3格式)以及包含聲音黨內容的文字檔(txt格式)</h3>
	<h3>請耐心等候所有文件產生Complete</h3>
	<form >
		<div id="queue"></div>
		<center><input id="file_upload" name="file_upload" type="file" multiple="true"></center>
	</form>
	<p><a href="index.html">GO BACK</a><br></p>
	<div id=info ></div>
	<div id=Bback ></div>
	<script type="text/javascript">
	$.ajaxSetup({ cache: false });
	var check=''
	var myVar=setInterval(function() {GetUploadInfo()},100);
	
	function GetUploadInfo(){
		$("#info").load("error.log");
		//if(document.getElementById('info').value() =="分析完成")
			//document.getElementById('Bback').innerHTML = '<a href="index.html">BACK</a><br>'; 
	}
		<?php $timestamp = time();?>
		$(function() {
			$('#file_upload').uploadify({
				'formData'     : {
					'timestamp' : '<?php echo $timestamp;?>',
					'token'     : '<?php echo md5('unique_salt' . $timestamp);?>'
				},
				'swf'      : 'uploadify/uploadify.swf',
				'uploader' : 'uploadify.php'
			});
		});
	</script>
</body>
</html>