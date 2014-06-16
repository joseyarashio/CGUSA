# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 11:15:35 2014

@author: joseyarashio
"""
import re

text_file = open("../Sample2.txt", "r")
lines = text_file.read()
text_file.close()

words=lines.split()

print(words)
print('=======================================')
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
tree = ET.ElementTree(file='../OutputFile/Sample.xml')
root = tree.getroot()
pivot=-1
text=[]
for idy,elem in enumerate(tree.findall('cm/word/text')):
    
    if(elem.text!=None):
        text.append(elem.text)
        
        for idx, word in enumerate(words):        
            if(word!=elem.text)and (elem.text==re.sub(r'[^a-zA-Z0-9]','',word))and (idx>pivot):
                elem.text=word
                pivot=idx
                break
            else:
                pass
    else:
        pass
tree.write('../OutputFile/Sample.xml')

pivot2=-1
for idx, word in enumerate(words):
    if(word[0].isupper()):
        print(word)
        for idy,elem in enumerate(tree.findall('cm/word/text')):
            if(idy>pivot2):
                if(elem.text!=None) and (elem.text==word.lower()):
                    print(elem.text)
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
tree.write('../OutputFile/Sample.xml')                 