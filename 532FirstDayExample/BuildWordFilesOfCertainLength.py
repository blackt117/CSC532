
import re
import string

filenames = ['MobyDick.txt', 'WarAndPeace.txt', 'ParadiseLost.txt',
             'SwannsWay.txt', 'Ulysses.txt', 'TheOdyssey.txt',
             'FaerieQueene.txt', 'CanterburyTales.txt', 'CritiqueOfPureReason.txt']

size = int(input("How many words do you want in the file? "))
if size:
#for size in range(100000, 2000000, 100000):
    outfileName = "words_" + str(size) + ".txt"
    outFile = open(outfileName, 'w', encoding='UTF-8')

    totalTokens =0
    for filename in filenames:
        file = open(filename, 'r', encoding='UTF-8')
        words = file.read()
        file.close()

        splitable = '[' + string.punctuation + string.whitespace + ']'
        tokens = re.split(splitable, words)
        tokens = [s.lower() for s in tokens if s.isalnum()]

        for w in tokens:
            totalTokens += 1
            outFile.write(w + ' ')
            if totalTokens % 15 == 0:
                outFile.write('\n')
            if totalTokens == size:
                break
        if totalTokens == size:
            break

        #print(tokens)
        print("The number of tokens is", len(tokens))
        vocabulary = set(tokens)
        print("The number of unique words is", len(vocabulary))
        #totalTokens += len(tokens)

    outFile.close()
    print("The total number of tokens is", totalTokens)