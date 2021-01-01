#!/bin/python3

import math
import os
import random
import re
import sys

def printmultiple(n):
  for x in range(1, 11):
    multiple = n * x
    st="{} x {} = {}"
    print(st.format(n, x, multiple))

if __name__ == '__main__':
    n = int(input())
    printmultiple(n)
