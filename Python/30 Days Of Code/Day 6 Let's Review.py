import sys
userInput = sys.stdin.readlines()
list_of_words = []
for words in userInput:
    if len(words) > 3:
        list_of_words.append(words)
t = map(lambda s: s.strip(), list_of_words)
for S in t:
    print(S[0::2] + " " + S[1::2])