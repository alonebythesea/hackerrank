from collections import OrderedDict

def merge_the_tools(string, k):
    string_split = [string[i:i+k] for i in range(0, len(string), k)]
    for strings in string_split:
        print(''.join(OrderedDict.fromkeys(strings)))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k) 
