CGUSA是一套自動化英語評分以及英語訓練的系統。

想要使用本系統在您的電腦主機上，有幾點注意事項請詳讀。
1.您必須先安裝appserv或是wampserv等相關網頁伺服器軟體。

2.安裝python 3.x版本

3.路徑及參數更改:
	3.1.index.html 當中的jRecorder upload host/必須更改ip及檔案路徑，預設為host : 'http://localhost/CGUSA-master/acceptfile.php?filename=userRecord'
注意:將/localhost/改為ip位址即可，上傳檔名不要更動 

	3.2.將python目錄加入到windows系統環境變數path。

	3.3.do.bat以及douser.bat中，cd路徑必須更改，分別設置exe與exe2user絕對路徑位址。


最後，打開chrome瀏覽器輸入網址如localhost/CGUSA-master/index.html後便可操作本系統。