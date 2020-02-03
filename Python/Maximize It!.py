import sys
from itertools import product

#read from stdin
out = sys.stdin.readlines()

#removing \n from str also adding commas between
out = [s.strip().split(' ') for s in out]

#converting string to integer
c = out[:]
out = [[int(x) for x in c] for c in out]

M = out[0][1]


#removing M and N values
N = out[1:]
#removing first number that defines number of testcase nums
N = [nums[1:] for nums in out]
#result using lambda function and product
results = map(lambda x: sum(i**2 for i in x[1:])%M, product(*N))
print(max(results)) 
