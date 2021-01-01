#!/bin/python3

import math
import os
import random
import re
import sys

"""Kitty and Katty have N plastic blocks. They label the blocks with sequential numbers from 1 to N 
and begin playing a game in turns, with Kitty always taking the first turn. 
The game's rules are as follows:
For each turn, the player removes 2 blocks, A and B, from the set. 
They calculate A-B, write the result on a new block, and insert the new block into the set.

The game ends when only 1 block is left. The winner is determined by the value written on the final block, X:
 If X%3 = 1, then Kitty wins
If X%3 = 2, then Katty wins
 If X%3 = 0, then the player who moved last wins.
 
 Given the value of N, can you find and print the name of the winner? 
 Assume that both play optimally.
 
 Note: The selection order for A and B matters, as sometimes A-B is not eq to B-A 
 
 """

if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())
