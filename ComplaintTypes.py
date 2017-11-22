#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:19:15 2017

@author: yorranshellwattson
"""

import csv 
complaintTypes = {}
f = open("WestchesterSquare.csv" , encoding = "latin-1") #Zip Codes 10461 & 10462 
reader = csv.DictReader(f)

for row in reader:
    complaint = row["Complaint Type"]
    complaintTypes[complaint] = complaintTypes.get(complaint, 0) + 1
f.close()

worstComplaint = sorted(complaintTypes, key = complaintTypes.__getitem__, reverse=True)

#Top 10 Complaints
for i in range(10):
    print("Complaint Type:", worstComplaint[i], "was made", complaintTypes[worstComplaint[i]], "times.")

