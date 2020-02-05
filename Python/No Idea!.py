_ = input()

elements_input = input().split()


A_input = set(input().split())
B_input = set(input().split())



print(sum((i in A_input) - (i in B_input) for i in elements_input))      
