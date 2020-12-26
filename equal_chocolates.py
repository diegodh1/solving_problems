#!/bin/python3

import math
import os
import random
import re
import sys

#LINK TO THE ORIGINAL PROBLEM HACKERRANK https://www.hackerrank.com/challenges/equal/problem

# Complete the equal function below.
def equal(arr):
    #get the min
    min_bar = min(arr)
    #min number of ops
    min_op = sys.maxsize
    #the min will be between min - 4  and min
    for i in range(5):
        op = 0
        for j in range(len(arr)):
            t = arr[j] - (min_bar-i)
            #the number of operations that we need to transform t to min_bar
            op += t//5 + t % 5 // 2 + t % 5 % 2
        min_op = min(min_op, op)
            
    #return the number of operations needed
    return min_op
                    

test = [53,361,188,665,786,898,447,562,272,123,229,629,670,848,994,54,822,46,208,17,449,302,466,832,931,778,156,39,31,777,749,436,138,289,453,276,539,901,839,811,24,420,440,46,269,786,101,443,832,661,460,281,964,278,465,247,408,622,638,440,751,739,876,889,380,330,517,919,583,356,83,959,129,875,5,750,662,106,193,494,120,653,128,84,283,593,683,44,567,321,484,318,412,712,559,792,394,77,711,977,785,146,936,914,22,942,664,36,400,857]
print(equal(test))
