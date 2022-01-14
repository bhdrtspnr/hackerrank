#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def jumpingOnClouds(c):
    cur_pos = 0
    jumps = 0
    lastPos = len(c)-1
    last2Pos = len(c)-2
    
    while cur_pos<last2Pos:
        if c[cur_pos+2] == 0:
            cur_pos += 2
        else:
            cur_pos += 1
        jumps += 1
    if cur_pos != lastPos:
        jumps += 1
        
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
