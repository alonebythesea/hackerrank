#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    for nums in arr:
        arr.sort()
        minsum = sum(arr[:-1])
        maxsum = sum(arr[1:])
    return print(minsum,maxsum)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
