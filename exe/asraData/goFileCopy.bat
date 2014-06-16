@echo off

echo ====== Copy common files
copy \users\jang\app\asr\mfcc\mfcc*.cfg

echo ====== Copy files for Japanese
pushd japanese
copy \users\jang\app\asr\dict\japanese\japanese.dic
copy \users\jang\app\asr\dict\japanese\japanese.qiYin
copy \users\jang\app\asr\dict\japanese\japanese.tnm
copy \users\jang\app\asr\dict\japanese\japanese.sdp
copy \users\jang\app\asr\macro\japanese20090806\japanese.macb
copy \users\jang\app\asr\macro\japanese20100129\japanese.macb
popd

echo ====== Copy files for Chinese
pushd chinese
copy \users\jang\app\asr\dict\chinese\chinese.dic
copy \users\jang\app\asr\dict\chinese\chinese.qiYin
copy \users\jang\app\asr\dict\chinese\chinese.tnm
copy \users\jang\app\asr\dict\chinese\chinese.sdp
copy \users\jang\app\asr\dict\chinese\chinese.eps
copy \users\jang\app\asr\dict\chinese\pinyinTable.txt
copy \users\jang\app\asr\dict\chinese\chineseBig5.wpa
copy \users\jang\app\asr\macro\chinese20080108\tcc300.japan20.linsu.macb
copy \users\jang\app\asr\macro\taihua.mdl
:copy \users\jang\app\asr\dict\chinesePaData\output\hanyu.dic
popd

echo ====== Copy files for English
pushd english
copy \users\jang\app\asr\dict\english\english.qiYin
copy \users\jang\app\asr\dict\english\english.wpa
copy \users\jang\app\asr\dict\english\english.wpab
copy \users\jang\app\asr\dict\english\english.wpaAddenda
copy \users\jang\app\asr\dict\english\null.wpaAddenda
copy \users\jang\app\asr\dict\english\english.tnm
copy \users\jang\app\asr\dict\english\english.sdp
copy \users\jang\app\asr\dict\english\english.modelCount
:copy \users\jang\app\asr\macro\english.macb
:copy \users\jang\app\asr\macro\english20060911\english.macb
copy \users\jang\app\asr\macro\english20091108\english.macb
popd