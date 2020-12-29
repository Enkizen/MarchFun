#!/bin/python3

import math
import os
import random
import re
import sys



class Car:
    
    def __init__(self,maxspd,speedtype):
        self.maxspd=maxspd
        self.speedtype=speedtype
    
    def __str__(self):
        st =  "Car with the maximum speed of {} {}"
        return st.format(self.maxspd,self.speedtype)
class Boat:
    def __init__(self,maxspd):
        self.maxspd=maxspd
    
    def __str__(self):
        st= "Boat with the maximum speed of {} knots"
        return st.format(self.maxspd)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
