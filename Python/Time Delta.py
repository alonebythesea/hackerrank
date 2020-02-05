#!/bin/python3
import os
from datetime import datetime as dt

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    for i in range(t):
        return (str(int(abs(dt.strptime(t1, time_format) - dt.strptime(t2, time_format)).total_seconds())))
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close() 
