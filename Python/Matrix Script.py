#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


somestr = ''
for i in range(m):
    for j in range(n):
        somestr = somestr + matrix[j][i]
       

t1 = re.match(r'\W*',somestr[::-1]).group()

t1= t1[::-1]

t2 = re.match(r'\W*',somestr).group()

s = re.sub('[^0-9a-zA-Z]+', ' ', somestr).rstrip().lstrip()

k = t2 + s + t1

print((k, t1) [s==''])