# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:43:34 2023

@author: zobae
"""

import PyPDF2
import codecs
import unicodedata



#create file object variable
#opening method will be rb
filename='C:/Users/zobae/OneDrive/Desktop/My presentation/BMW-1-Series-F20-F21-Factory-Repair-Manual-2011-2017.pdf'
filename='D:/Car Manuals/acura/Acura 3.2TL 2.5TL 1995-1998 Approved/1995-1998 Service Manual/TL9596MAINIDX.pdf'
pdffileobj = codecs.open(filename.encode('utf-8'), 'rb')

#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfReader(pdffileobj)

#This will store the number of pages of this pdf file
x=len(pdfreader.pages)

#create a variable that will select the selected number of pages
file1=open(r"D:/Car Manuals/acura/Acura 3.2TL 2.5TL 1995-1998 Approved/1995-1998 Service Manual/12.txt","a")
for i in range (x):
    pageobj=pdfreader.pages[i]
    
    #(x+1) because python indentation starts with 0.
    #create text variable which will store all text datafrom pdf file
    text=pageobj.extract_text()
    
    #save the extracted data from pdf to a txt file
    #we will use file handling here
    #dont forget to put r before you put the file path
    #go to the file location copy the path by right clicking on the file
    #click properties and copy the location path and paste it here.
    #put "\\your_txtfilename"
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    file1.writelines(text)

file1.close()
    
 
'''
import re
import emoji

def clean_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove emojis
    text = emoji.get_emoji_regexp().sub(u'', text)

    # Remove extra punctuations while preserving existing ones
    text = re.sub(r'(?:(?<=\w)[^\w\s]|(?<!\w)[^\w\s]+(?=\w)|[^\w\s]+(?!\w))', '', text)

    return text




filename='C:/Users/zobae/OneDrive/Desktop/My presentation/1.txt'


'''



