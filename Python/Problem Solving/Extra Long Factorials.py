#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    for i in range(1,n + 1):
        fact = math.factorial(n)
        return print(fact)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
