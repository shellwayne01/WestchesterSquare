#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:08:22 2017

@author: yorranshellwattson
"""
import csv

tickets = {}
plateID = {}
issuedate = {}
state = {}
carType = {}

f = open("Parking.csv")
reader = csv.DictReader(f)


for row in reader:
    summonsnum = row["Summons Number"]
    tickets[summonsnum] = tickets.get(summonsnum, 0) + 1

    plate = row["Plate ID"]
    plateID[plate] = plateID.get(plate, 0) + 1
           
    date = row["Issue Date"]
    issuedate[date] = issuedate.get(date, 0) + 1  
             
    regstate = row ["Registration State"]
    state[regstate]= state.get(regstate, 0) + 1
    
    car = row ["Plate Type"]
    carType[car] = carType.get(car, 0) + 1
           
f.close()


worstPlateID = sorted(plateID, key = plateID.__getitem__, reverse=True)
worstState = sorted(state, key = state.__getitem__, reverse=True)
worstCarType = sorted(carType, key = carType.__getitem__, reverse=True)


#Top 10 Worst Offenders by ID, State, Car Type 
for i in range(10):
    print("Plate ID", worstPlateID[i], "has", plateID[worstPlateID[i]], "tickets.")
