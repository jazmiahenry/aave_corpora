# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:47:15 2021

@author: 
"""

import numpy as np
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

import string

#create a function to read all the files in the folder
#append them to a new larger doctument
lines = []
with open('AAVE Corpora/Ashby_RedderBlood.txt') as f:
    data = f.read()
    #print(contents)
#lower case
data = data.lower()

#remove numbers 
data = re.sub(r'\d+', '', data)

#remove punctuation
tokenizer = RegexpTokenizer(r'\w+')
tokenizer.tokenize(data)
#print(data)

#general nltk stopwords
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(data)
result = [i for i in tokens if not i in stop_words]

with open('Pre-processed corpora/redderbloodpre.txt', 'w') as f:
    f.writelines(result)

#defining our own stopwords

