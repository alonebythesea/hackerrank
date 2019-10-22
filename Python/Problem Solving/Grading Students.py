#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []
    for i in grades:
        if i <= 40:
            if (i + 2) == 40:
                i = (i + 2)
                result.append(i)
            elif (i + 1) == 40:
                i = (i + 1)
                result.append(i)
            else:
                result.append(i)
        elif 40 <= i:
            if (i + 2) % 5 == 0 or (i + 2) % 10 == 0:
                i = (i + 2)
                result.append(i)
            elif (i + 1) % 5 == 0 or (i + 1) % 10 == 0:
                i =  (i + 1)
                result.append(i)
            else:
                result.append(i)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()