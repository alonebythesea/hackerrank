#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    countAlice = 0
    countBob = 0
    for i in a and b:
        if 1 > i or i > 100:
            print('error. number should be in range [1 - 100]')
        elif 1 > i or i > 100:
           print('error. number should be in range [1 - 100]')

    if a[0] > b[0]:
        countAlice += 1
    if a[1] > b[1]:
        countAlice += 1
    if a[2] > b[2]:
        countAlice += 1
    if a[0] < b[0]:
        countBob += 1
    if a[1] < b[1]:
        countBob += 1
    if a[2] < b[2]:
        countBob += 1
    return (countAlice, countBob)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()