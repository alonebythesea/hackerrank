#!/bin/python3

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
   i = datetime.strptime(s,"%I:%M:%S%p")
   i = datetime.strftime(i,"%H:%M:%S")
   i = str(i)
   return i


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
