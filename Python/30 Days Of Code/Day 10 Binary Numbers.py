#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
def maxConsecutive(n):
    toBinary = bin(n)
    x = toBinary[2:]
    return(max(map(len, x.split('0'))))
print(maxConsecutive(n))
