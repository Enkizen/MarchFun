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
	
	
	
	
	
	
	
	
	#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, l1,l2):
        self.l1=l1
        self.l2=l2
    
    def area(self):
        return float(self.l1*self.l2)
        
class Circle:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return math.pi* self.r**2

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
