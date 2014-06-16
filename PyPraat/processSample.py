import re
import os
import time
import shutil
import subprocess
import random
import makeLyricFile as ml

errorLog_path='error.log'
error= False
def removeDot():
	try:
		original_string = open('./InputFile/Sample.txt').read()
		new_string = re.sub(r'[^a-zA-Z0-9]', ' ',original_string)
		open('./Sample.txt', 'w').write(new_string)
		errorLog.write("removeDot ok<br>")
	except:
		errorLog.write("removeDot錯誤<br>")
		error= True
def innitialize():
	#os.remove("./Sample.wav")
	programStartTime=time.time()
	try:
		os.system('ffmpeg.exe -i ./InputFile/Sample.mp3 -ar 16000 -ac 1 ./InputFile/Sample.wav 2> ffmpeg.msg')
		os.system('ffmpeg.exe -i ./InputFile/Sample.wav -ar 16000 -ac 1 ./InputFile/Sample.wav 2> ffmpeg.msg')
	except:
		errorLog.write("innitialize錯誤<br>")
		error= True
	finally:
		moveFile2do()
		chechXmlFileTime(programStartTime)
		errorLog.write("innitialize ok<br>")
		
def moveFile2do():
	try:
		shutil.copy("./InputFile/Sample.wav" , "./Sample.wav")
		shutil.copy("./InputFile/Sample.txt" , "./Sample2.txt")
		errorLog.write("複製檔案到主目錄第一次 ok<br>")
		
	except:
		#print("moveFile2do錯誤",file=errorLog)
		error= True
	finally:
		removeDot()
		shutil.copy("./InputFile/Sample.wav" , "./Sample.wav")
		errorLog.write("複製檔案到主目錄第二次 ok<br>")
		#os.system("C:\AppServ\www\CGUSA-master\do.bat")
		p = subprocess.Popen(r'start cmd /c do.bat', shell=True)
		p.wait()
		errorLog.write("moveFile2do ok<br>")
		CleanOld()
		
def movePraatFile():
	try:
		shutil.move("Sample.PITCH" , "./OutputFile/Sample.PITCH")
		shutil.move("Sample.INTENSITY" , "./OutputFile/Sample.INTENSITY")
		shutil.move("Sample.TEXTGRID" , "./OutputFile/Sample.TEXTGRID")
		shutil.move("Sample.MFCC" , "./OutputFile/Sample.MFCC")
		errorLog.write("movePraatFile ok<br>")
	except:
		errorLog.write("movePraatFile錯誤<br>")
		error= True
	
def CleanOld():
	try:
		os.remove("./InputFile/Sample.wav") #刪除舊的上傳檔案
		os.remove("./InputFile/Sample.txt")
		os.remove("./InputFile/Sample.mp3")
		errorLog.write("CleanOld ok<br>")
	except:
		pass

def chechXmlFileTime(StartT):
	
	XmlFileTime = os.stat('./exe/output/output.xml').st_mtime
	
	if XmlFileTime > StartT:
		shutil.copy("./exe/output/output.xml" , "./OutputFile/Sample.xml")
		errorLog.write("Copy Xml File ok<br>")
		
	else:
		random_number = random.randint(0,1)
		time.sleep(random_number)
		chechXmlFileTime(StartT)
		
def reductWord():
    '''This part is used to do reduction, Sample text file was contain with the dot or uppercase word, so this step will reduct the xml file to original word.'''
    text_file = open("./Sample2.txt", "r")
    lines = text_file.read()
    text_file.close()
    words=lines.split()
    
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    
    tree = ET.ElementTree(file='./OutputFile/Sample.xml')
    root = tree.getroot()
    
    sentance=1
    pivot=-1
    for idy,elem in enumerate(tree.findall('cm/word/text')):
        elem.set('sentance',str(sentance))
        if(elem.text!=None):
        
            for idx, word in enumerate(words):        
                if(word!=elem.text)and (elem.text==re.sub(r'[^a-zA-Z0-9]','',word))and (idx>pivot):
                    if(word.find('.')!=-1):
                        sentance+=1
                    elem.text=word
                    pivot=idx
                    break
                else:
                    pass
        else:
            pass
        
    tree.write('./OutputFile/Sample.xml')

    pivot2=-1
    for idx, word in enumerate(words):
        if(word[0].isupper()):
            for idy,elem in enumerate(tree.findall('cm/word/text')):
                
                if(idy>pivot2):
                    if(elem.text!=None) and (elem.text==word.lower()):
                    
                        elem.text=word
                        pivot2=idy 
                        break
                    else:
                        pivot2=idy 
                else:
                    pass
        else:
            if(idx>pivot2):
                pivot2=idx
    tree.write('./OutputFile/Sample.xml') 
    errorLog.write("Reduction finished<br>") 
    
if __name__=="__main__":
    open(errorLog_path,'w').write('')
    errorLog=open('Error.log','w',encoding='utf-8')
    errorLog.write("開始分析<br>")
    innitialize()
    reductWord()
    errorLog.write("分析完成<br>")
    Sample=ml.getSample()
    ml.makeLrc(Sample)
	
    errorLog.close()
    system.exit(0)