#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


#0,2,5,3
def kangaroo(x1, v1, x2, v2):
    jump = 0
    if v1>v2:
        jump = v1-v2
    else:
        jump = v2-v1
    if x1==x2:
        return "YES"
    
    if x1 != x2 and v2==v1:
        return "NO"
    
    difference = 0
    
    if x1>x2:
        difference = x1-x2
    else:
        difference = x2-x1
    
    if x1<x2 and v1>v2:
        if (x2-x1)%jump == 0:
            return "YES"
        else:
            return "NO"
    elif x2<x1 and v2>v1:
        if (x1-x2)%jump == 0:
            return "YES"
        else:
            return "NO"          
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
