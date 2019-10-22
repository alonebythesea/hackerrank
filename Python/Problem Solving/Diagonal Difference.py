#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rangeNumber1 = 0
    rangeNumber2 = 0
    rangeNumber3 = 0
    rangeNumber4 = -1
    listPriDiag = []
    listSecDiag = []
    for lists in arr:
        listPriDiag.append(arr[rangeNumber1][rangeNumber2])
        rangeNumber1 += 1
        rangeNumber2 += 1
        listSecDiag.append(arr[rangeNumber3][rangeNumber4])
        rangeNumber3 += 1
        rangeNumber4 -= 1
    resultPriDiag = sum(listPriDiag)
    resultSecDiag = sum(listSecDiag)  
    return abs(resultPriDiag - resultSecDiag)
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()