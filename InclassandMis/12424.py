import math

nlogn = float(input("What does nlogn = "))

count = 1

if nlogn > 0:
    print("count\tN\tN*1og(n)")
    low = 0
    high = nlogn
    guess = (low + high)/2
    small = .001
    computedresult = guess * math.log2(guess)
    print(str(count) + '\t'+str(guess)+ '\t' + str(computedresult))
    while abs(computedresult - nlogn) > small:
        if computedresult > nlogn:
            high = guess

        else:
            low = guess
        count +=1
        guess = (low + high) /2
        computedresult = guess * math.log2(guess)
        print(str(count) + '\t' + str(guess) + '\t' + str(computedresult))
    print(guess)


