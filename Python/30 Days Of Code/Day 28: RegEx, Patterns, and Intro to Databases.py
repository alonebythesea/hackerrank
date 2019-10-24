#!/bin/python3

import math
import os
import random
import re
import sys

l = []

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        for i in firstNameEmailID:
            if '@gmail.com' in i:
                l.append(firstName)

j = sorted(l)
for k in j:
    print(k)
