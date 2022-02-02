#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#https://www.hackerrank.com/challenges/migratory-birds/problem
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    
    uniqueBirdArray = {}
    
    for i in range(len(arr)):
        if not arr[i] in uniqueBirdArray.keys():
            uniqueBirdArray[arr[i]] = 0
    
    print(uniqueBirdArray.keys())

    for i in range(len(arr)):
        if arr[i] in uniqueBirdArray.keys():
            uniqueBirdArray[arr[i]] +=1

    print(uniqueBirdArray)

    return max(sorted(uniqueBirdArray), key=uniqueBirdArray.get)

    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
