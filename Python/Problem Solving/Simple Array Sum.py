#!/bin/python3

import os
import sys
import math

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    for i in ar:
        if i >= 1000:
            print('error. your number is greater or equal 1000')
        elif i < 0:
            print('error. your number is lower than 0')
    return sum(ar)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
