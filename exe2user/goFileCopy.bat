@echo off

set mainDir=\users\jang\app\asr\source
copy %mainDir%\assess.exe
copy %mainDir%\recog.exe
copy \users\jang\c\lib\wave\flv2wav\example\flv2wav.exe
rem copy \users\jang\app\pt32\pt32.exe pt4pmp.exe

: Delete all subfolders
for %%a in (asraData output) do (
	rmdir /s /q %%a & mkdir %%a
)

xcopy %mainDir%\asraData asraData /s /e /y
rem ==== 以下是華語辨識相關檔案
copy %mainDir%\chinese.vc.prm
copy %mainDir%\chinese.sa.prm
rem ==== 以下是英語辨識相關檔案
copy %mainDir%\english.vc.prm
copy %mainDir%\english.sa.prm
rem ==== 以下是日語辨識相關檔案
copy %mainDir%\japanese.vc.prm
copy %mainDir%\japanese.sa.prm
rem ==== 以下是台語辨識相關檔案
copy %mainDir%\taiwanese.vc.prm
copy %mainDir%\taiwanese.sa.prm


rem === This is for speak2me only!
rem copy \users\jang\app\asr\dict\english\english_speak2me.tnm asraData\english\english.tnm