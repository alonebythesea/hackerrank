#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    countspaces = n - 1
    counthashes = 1
    for n in range(1,n+1):
        printstairs = print(' ' * countspaces + '#'* counthashes)
        countspaces -= 1
        counthashes += 1
    return printstairs

        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
