# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:30:16 2019

@author: SupErman
"""
import random
import numpy as np

n = 3 #number of doors
h = 1 #number of doors that the host opens
mc_n = 12000
counter = 0
pos_door = list(range(n))# door indexes
pos_door = np.asarray(pos_door)

for i in range(mc_n):
    door_s = [random.choice(pos_door)] # door you selected
    door_c = [random.choice(pos_door)] # door that has the car
    temp_doors = pos_door
    if door_s == door_c: # if the door you selected has the car, 
        #the host has two doors to open
        temp_doors = np.delete(temp_doors,door_s)
    else:# if the door you selected does not have the car, 
        #the host has one door to open
        temp_doors = np.delete(temp_doors,door_c+door_s)
    door_h = []
    for j in range(h):
        temp = random.choice(temp_doors)
        door_h.append(temp) # door that the host open
        flag = temp_doors == temp
        temp_doors = temp_doors[~flag]
    
    ## the door you switch
    door_switched = pos_door
    door_switched = np.delete(door_switched,door_s+door_h)
   
    
    if door_switched[0] ==door_c:
        counter = counter + 1
        
print(counter/mc_n)
    
