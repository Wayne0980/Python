# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:05:58 2018

@author: Wayne
"""


sorce = []

total = inscore = 0

while(inscore != -1):
    inscore = int(input("Please keyin the sorce:"))
    sorce.append(inscore)
    total += inscore
    
print("You have:%d students"%(len(sorce)-1))
average = total / (len(sorce)-1)
print("total sorce:%d,avg.%d",(total,average))