import sys
import os
import re
import string
import fileinput
import glob
import numpy

def getSample():
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    
    tree = ET.ElementTree(file='output.xml')
    root = tree.getroot()

    text=[]
    Start=[]
    End=[]
    SampleArray=[]
    
    for elem in tree.findall('cm/word/text'):
        text.append(elem.text)
        
    for elem in tree.findall('cm/word/interval'):
        
        a=elem.text.split()[0]
        Start.append(a)
        
        b=elem.text.split()[1]
        End.append(b)
    
    SampleArray.append(text)
    SampleArray.append(Start)
    SampleArray.append(End)
    return SampleArray
    
def makeLrc(Sample):
    LRC=open('output.lrc','w')
    
    textList=Sample[0]
    timeList=Sample[1]
    
    for i in range(len(textList)):
        if(str(textList[i]) != 'None'):
            LRC.write('['+str(timeList[i])+']'+str(textList[i])+'\n')
        
    LRC.close()
    
if __name__=="__main__":
    Sample=getSample()
    makeLrc(Sample)
