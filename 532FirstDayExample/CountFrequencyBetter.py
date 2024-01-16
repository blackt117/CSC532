import re
import string
import time

fileSizes = [10, 100, 1000, 5000, 10000, 50000,
             100000, 200000, 300000, 400000, 500000,
             600000, 700000, 800000, 900000, 1000000,
             1100000, 1200000, 1300000, 1400000, 1500000,
             1600000, 1700000, 1800000, 1900000, 2000000]

print("N\tTime")
for fileSize in fileSizes:
    startTime = time.perf_counter()
    filename = "words_" + str(fileSize) + ".txt"
    file = open(filename, 'r', encoding='UTF-8')
    words = file.read()
    file.close()

    splitable = '[' + string.punctuation + string.whitespace + ']'
    tokens = re.split(splitable, words)
    tokens = [s.lower() for s in tokens if s.isalnum()]
    #print(tokens)
    #print("The number of tokens is", len(tokens))
    vocabulary = set(tokens)
    #print("The number of unique words is", len(vocabulary))
    countTable = {}
    for w in tokens:
        if w in countTable:
            countTable[w] = countTable[w] + 1
        else:
            countTable[w] = 1
    # for w in vocabulary:
    #     countTable[w] = tokens.count(w)
    #print(countTable)

    #print("Test case: The probability of seeing the word 'the' is", 100*countTable['the']/len(tokens))
    endTime = time.perf_counter()
    print(fileSize, '\t', endTime - startTime)