#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    matrix = []
    rows = len(c)+1
    cols = n+1
    for i in range(rows):
        matrix.append([0] * (cols))
    #if the unit is 0 there is only a way to change the cois
    for i in range(rows):
        matrix[i][0] = 1
    #change coins
    for i in range(1,rows):
        for j in range(1,cols):
            k = c[i-1]
            #if we can use the coin then 1 + the ways without have used the coin
            if  j >= k:
                matrix[i][j] = matrix[i-1][j] +  matrix[i][j-k]
            #we can't use the coin
            else:
                matrix[i][j] = matrix[i-1][j]
    #return the ways of making change
    return matrix[rows-1][cols-1]

print("#ways to make change ", getWays(10, [2,5,3,6]))