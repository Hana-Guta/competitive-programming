#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    up = 0
    down = 0
    for i in path:
        if i == 'U':
            up += 1
            if  down == up :
                valleys += 1
        if i == 'D':
            down +=1
    return valleys
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

    
