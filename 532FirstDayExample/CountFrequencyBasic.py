import re
import string
import time

startTime = time.perf_counter()
filename = "words_5000.txt"
file = open(filename,  'r', encoding='UTF-8')
words = file.read()
file.close()
print(words)

splitable = '[' + string.punctuation + string.whitespace + ']'
#print(splitable)
tokens = re.split(splitable, words)
tokens = [s.lower() for s in tokens if s.isalnum()]
#print(tokens)
print("The number of tokens is", len(tokens))
vocabulary = set(tokens)
print(tokens)
print("The number of unique words is", len(vocabulary))
countTable = {}
for w in vocabulary:
    countTable[w] = tokens.count(w)
#print(countTable)

print("Test case: The probability of seeing the word 'the' is", 100*countTable['the']/len(tokens))
endTime = time.perf_counter()
print(5000, '\t', endTime - startTime)