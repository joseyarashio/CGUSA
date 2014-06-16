import os
import time
import random
import shutil
import math
from dtw import *

def innitialize():
    '''remove some old file and resample the wav file to 16khz .wav'''
    try:
        os.remove("./OutputFile/User.xml")
    except:
        pass
    try:
        os.remove("./userRecord.wav")
        os.system('ffmpeg.exe -i ./recorderFile/userRecord.wav -ar 16000 -ac 1 ./userRecord.wav 2> ffmpeg.msg')
        os.system("douser.bat")
    except:
        pass

def getSample(filename):
    '''parse xml to get data,like word duration,pitch,intensity'''
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    
    text=[]
    Start=[]
    End=[]
    SampleArray=[]
    pitch=[] 
    
    for elem in tree.findall('cm/word/text'):
        text.append(elem.text)
        
    for elem in tree.findall('cm/word/interval'):
        
        a=elem.text.split()[0]
        Start.append(a)
        
        b=elem.text.split()[1]
        End.append(b)
    for elem in tree.findall('cm/word/pitch'):
        a=elem.text.split()
        floats = [float(x) for x in elem.text.split()]
        pitch.append(floats)
        
    SampleArray.append(text)
    SampleArray.append(Start)
    SampleArray.append(End)
    SampleArray.append(pitch)
    return SampleArray
    
def compare(S_index,U_index,Sample,User):
    '''find the DTW path'''
    s1=len(Sample[3][S_index])
    x1=sum(Sample[3][S_index])/s1
    s2=len(User[3][U_index])
    x2=sum(User[3][U_index])/s2
    move=x1-x2
    AdaptUser = [x + move for x in User[3][U_index]]
    
    if(s1/s2)<2 and (s1/s2)>0.5:
        dodtw = Dtw(Sample[3][S_index],AdaptUser,distance_func=lambda x, y: math.fabs(x - y))
        #times=(len(dodtw.get_path()))
        return round(2*(dodtw.calculate()/len(dodtw.get_path())),2)
        
    else:
        return -1
   
def find_matching_list(Sampletext_list,Usertext_list):
    matching=[]
    pivot=-1
    for idy, word_u in enumerate(Usertext_list):
        for idx, word_s in enumerate(Sampletext_list):
            if(word_u==word_s)and(word_u!=None)and(idx>pivot):
                matching.append((idx,idy))
                pivot=idx
                break
    return matching
    
def makeCsv(result):
    '''write the result to csv file'''
    Csv=open('output.txt','w')
    
    Csv.write(result)
    Csv.close()
	
def result2Score(dst):
    '''This function will change the DTW distance to the real 0~100 score'''
    upper=8
    lower=0.3
    if(dst!=-1):
        if(dst>upper):
            return 0
        else:
            if(dst<lower):
                return 100
            else:
                score=(upper-float(dst-0.3))*(100/upper)
                return score
    else:
        return 0
def result_p(opt):
    '''show the compare result of pitch'''
    Sample=getSample('./exe/output/output.xml')
    User=getSample('./exe2user/output/output.xml')
    matching_list=find_matching_list(Sample[0],User[0])
    result=[]
    if(opt==-1):
        for x in matching_list:
            result.append((User[0][x[1]],result2Score(compare(x[0],x[1],Sample,User))))
        
    else:
        compare(matching_list[opt][0],matching_list[opt][1],Sample,User)
    return result
    
def chechXmlFileTime(StartT):
	'''check the xml done time,and copy the xml file to the outputFile folder'''
	XmlFileTime = os.stat('./exe2user/output/output.xml').st_mtime
	
	if XmlFileTime > StartT:
		shutil.copy("./exe2user/output/output.xml" , "./OutputFile/User.xml")
	else:
		random_number = random.randint(0,1)
		time.sleep(random_number)
		chechXmlFileTime(StartT)
  
def combineResult(filename,result):
    '''This function for combining this part of result to the User.xml'''
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    
    pivot=-1
    for item in result:
        for idx,elem in enumerate(tree.findall('cm/word/text')):
            if(item[0]==elem.text)and (idx>pivot):
                
                for idy,score in enumerate(tree.findall('cm/word/timberScore')):
                    if(idy==idx):
                        score.text=score.text+' '+str(item[1])
                        pivot=idx
                        break
                break
    tree.write('./OutputFile/User.xml')
    
if __name__=="__main__":
    
    programStartTime=time.time()
    innitialize()
    chechXmlFileTime(programStartTime)
    #makeCsv(str(result_p(-1)))
    combineResult("./OutputFile/User.xml",result_p(-1))
    system.exit(0)