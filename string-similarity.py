#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#https://www.hackerrank.com/challenges/string-similarity/problem

def stringSimilarity(s):
    testStrings = []
    
    count = 0

    for j in range(len(s)):
        testStrings.append(s[j:])
    
    i=0


    for strings in testStrings:
        i=0
        while i<len(strings):
            if strings[i] == s[i]:
                count +=1
            else:
                i += len(strings)
            i +=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
