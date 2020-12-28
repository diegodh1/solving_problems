#!/bin/python3

import math
import os
import random
import re
import sys

# Cost Function
def cost(B):
    A = {'min':0, 'max':0} 
    for i in range(1, len(B)):
        current = {'min':0, 'max':0}
        current['min'] = max(A['min'], A['max']+B[i-1]-1)
        current['max'] = max(A['max']+abs(B[i-1]-B[i]), A['min']+B[i]-1)
        A = current
    return max(A['min'], A['max'])


print(cost([1,2,1]))