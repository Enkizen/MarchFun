import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())


n = int(input())

count = 0
while n:
    n &= n << 1
    count += 1

print(count)

#print(len(max(bin(int(input().strip()))[2:].split('0'))))

#print(sorted(list(map(len,'{0:b}'.format(int(input().strip())).split("0"))),reverse=True)[0])
