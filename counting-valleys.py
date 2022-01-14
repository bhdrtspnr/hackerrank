#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen



def countingValleys(steps, path):
    altitude =0
    valleyCount = 0
    for chars in path:
        if(chars=="U"): #increase altitude if next char is U
            altitude += 1
        if(chars=="D"): #decrease
            altitude -= 1
        
        if altitude==0 and chars == "U": #if altitude becomes 0 with an up step it means we've just left a valley
            valleyCount += 1
    return valleyCount
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
