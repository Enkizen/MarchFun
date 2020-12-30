import math
import math
import os
import random
import re
import sys

def oddeven(n):
#n odd p weird
        if n % 2 !=0:
            print("Weird")
        if  n % 2 == 0:   
            if  n  >= 2 and n <= 5 :  
                  print("Not Weird")
                  
            if  n  >= 6 and n <= 20 :  
                  print("Weird")      
            if  n > 20 :  
                  print("Not Weird")    
                  
                  
if __name__ == '__main__':
    N = int(input())
    oddeven(N)
