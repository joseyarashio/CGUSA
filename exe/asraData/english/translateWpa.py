# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:48:11 2013

@author: user
"""

import sys
import re
def removeDot():
	try:
		original_string = open('english.wpa').read()
		new_string = re.sub(r'[^a-zA-Z0-9]', ' ',original_string)
		open('english2.wpa', 'w').write(new_string)
	except:
		pass
if __name__=="__main__":
    removeDot()