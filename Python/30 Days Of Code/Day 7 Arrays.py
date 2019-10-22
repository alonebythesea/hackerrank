#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
nums1 = []
for nums in arr:
    nums1.append(nums)
nums1.reverse()
print (str(nums1).strip('[]').replace(',',''))