#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:35:02 2019

@author: xiaolu
"""


### Make a request to \theyghtcrime.org"
### Extract the two characters generated by the website from the HTML
### Save the male characters in one text file and save the female characters in another text file.
### Repeat this process 50 times.

from requests import get 
import time
import re

### create empty file named male and female 
malefile = open("malefile.txt", "w+") 
femalefile = open("femalefile.txt", "w+")

### use for loop to repeat the script process 50 times 
for i in range(0, 50):
    time.sleep(1)
    resp = get("https://www.theyfightcrime.org/")
    txt0 = resp.text
    txt1 = txt0.split("<P>") ### split the text with paragraph sign
    txt2 = txt1[1] 
    ### split txt2 by He's, the sentence is split into space (before He's) and text (after He's)
    mal = re.split(r"He's", txt2) 
    ### split mal by She's, the sentence is split into text (before She's) and text (after She's)
    feml = re.split(r"She's", mal[1])
    ### split feml by They, the sentence is split into text (before They) and text (after They)
    they = re.split(r"They", feml[1])
    
    ### male sentence is combined by "He's" and feml[0]
    male = "He's" + feml[0]
    ### female sentence is combined by "She's" and they[0]
    female = "She's" + they[0]
    
    malefile.write(male+"\n")
    femalefile.write(female+"\n")  

malefile.close()
femalefile.close()