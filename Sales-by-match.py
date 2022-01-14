#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    uniqueArray = []
    matchCount = 0
    print(ar)
    for element in range(len(ar)):
        if not ar[element] in uniqueArray:
            uniqueArray.append(ar[element])
    
    dicto = dict.fromkeys(uniqueArray,0)
    

    for socks in ar:
        for unique_socks in dicto:
            if(socks==unique_socks):
                dicto[unique_socks] += 1
    print(dicto)
    for keys in dicto:
        matchCount += dicto[keys] //2

    return matchCount
    


testCase = [10,10,20,10,10,30,50,10,20]
n = len(testCase)
print(sockMerchant(n, testCase))