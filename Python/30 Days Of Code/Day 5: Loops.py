#!/bin/python3



if __name__ == '__main__':
    n = int(input())
    mult = n
    count = 0
    while count <= 9:
        count += 1
        result = mult * count
        print(mult, 'x', count, '=', result)
