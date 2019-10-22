#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    countEq = 0
    countNeg = 0
    countPos = 0
    for nums in arr:
        if nums > 0:
            countPos += 1
        elif nums < 0:
            countNeg += 1
        elif nums == 0:
            countEq += 1 
    resultPositive = countPos / length
    resultNegative = countNeg / length
    resultEquals = countEq / length
    return print(round(resultPositive,6)), print(round(resultNegative,6)), print(round(resultEquals,6))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)