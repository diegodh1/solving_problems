#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    fibb_sequence = []
    fibb_sequence.append(t1)
    fibb_sequence.append(t2)
    for i in range(2, n):
        value = fibb_sequence[i-2] + fibb_sequence[i-1] ** 2
        fibb_sequence.append(value)
    
    return fibb_sequence[n-1]

print(fibonacciModified(0,1,5))