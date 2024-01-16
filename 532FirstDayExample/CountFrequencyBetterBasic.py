import re
import string
import time


startTime = time.perf_counter()
filename = "words_50000.txt"
file = open(filename,  'r', encoding='UTF-8')
words = file.read()
file.close()

splitable = '[' + string.punctuation + string.whitespace + ']'
tokens = re.split(splitable, words)
tokens = [s.lower() for s in tokens if s.isalnum()]
#print(tokens)
print("The number of tokens is", len(tokens))
vocabulary = set(tokens)
print("The number of unique words is", len(vocabulary))
countTable = {}
# for w in vocabulary:
#     countTable[w] = tokens.count(w)
for w in tokens:
    if w in countTable:
        countTable[w] += 1
    else:
        countTable[w] = 1

#print(countTable)

print("Test case: The probability of seeing the word 'the' is", 100*countTable['the']/len(tokens))
endTime = time.perf_counter()
print(50000, '\t', endTime - startTime)