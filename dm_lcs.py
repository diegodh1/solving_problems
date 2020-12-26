#!/bin/python3
import math
import os
import random
import re
import sys

#LINK TO THE ORIGINAL PROBLEM HACKERRANK https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    matrix = []
    n = len(a)
    m = len(b)
    #initialize zero matrix
    for i in range(n+1):
        matrix.append([0] * (m+1))
    #finding the longest subsequence
    for i in range(1,n+1):
        for j in range(1, m+1):
            if(a[i-1]==b[j-1]):
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    #print the subsequence
    subsequence = []
    while n > 0 and m > 0:
        if a[n-1] == b[m-1]:
            subsequence.append(a[n-1])
            n = n - 1
            m = m -1
        else:
            if matrix[n-1][m] > matrix[n][m-1]:
                n = n - 1
            else:
                m = m -1

    return subsequence[::-1]
    

if __name__ == '__main__':

    test_a = [697,953,900,438,899,593,591,963,31,160,894,493,782,445,326,452,988,657,7,544,768,398,791,650,818,12,347,928,828,336,692,339,130,837,548,487,989,333,875,711,957,341,821,319,338,328,234,7,670,328,451,200,685,699,855,668,609,322,752,386,81,635,952,618,133,73,548,163,221,105,773,398,639,579,660,746,718,918,224,984,265,242,506,762,734,98,324,100,896,346,344,27,420,353,532,105,914,130,695]

    test_b = [438,591,768,160,777,894,782,398,445,306,326,282,452,607,241,513,185,7,544,12,347,828,336,83,924,143,692,339,130,515,837,466,989,875,711,957,338,266,305,480,328,28,7,670,328,699,849,668,609,979,100,322,283,386,655,263,826,169,635,952,618,73,238,897,221,863,34,372,732,398,579,666,545,660,794,746,526,718,918,403,615,946,224,822,242,506,734,324,100,55,346,704,24,650,678,532,914,130,423,998]

    test_1a = [3,9,8,3,9,7,9,7,0]
    test_1b = [3,3,9,9,9,1,7,2,0,6]
    test_2a = [1,2,3,4,1]
    test_2b = [3,4,1,2,1,3]
    result = longestCommonSubsequence(test_a, test_b)
    print(result)
