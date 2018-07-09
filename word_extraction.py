# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 00:02:58 2018

@author: Neha Koushik
"""
import csv
from rake_nltk import Rake
from nltk.corpus import stopwords 
import pandas as pd
# Uses stopwords for english from NLTK, and all puntuation characters by
# default

 

with open('job_skills.csv', encoding="utf8", errors='replace') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('jobs_output.csv', 'w') as file1:
        writer1 = csv.writer(file1)
        n  = 0
        for row in reader:
            n=n+1
            r = Rake() 
            text= row["Responsibilities"]
            a=r.extract_keywords_from_text(text)
            b=r.get_ranked_phrases()
            c=r.get_ranked_phrases_with_scores()
            sub_c= b[0:3]
            print(sub_c)
            print("================================================================================")
            
            writer1.writerow([','.join(map(str,sub_c))])
        #print(row["Responsibilities"])
        
