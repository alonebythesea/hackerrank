#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    for n in ar:
        if n > 10 or n < 1:
            print('error. only 1-10 numbers available') 
        elif ar[n] < 0 or ar[n] > 10**10:
            print('error. numbers must be in range [0 - 10^10]')
    result = sum(ar)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
