import math
import RecursivePrac
n_3logn = float(input("What does n^3log(x) = "))

count = 1

if n_3logn > 0:
    print("count\tN\tN^3*1og(n)")
    low = 0
    high = n_3logn
    guess = (low + high)/2
    small = .0001
    computedresult = guess * guess * guess * math.log(guess,10)
    print(str(count) + '\t'+str(guess)+ '\t' + str(computedresult))
    while abs(computedresult - n_3logn) > small:
        if computedresult > n_3logn:
            high = guess

        else:
            low = guess
        count +=1
        guess = (low + high) /2
        computedresult = guess * guess * guess * math.log(guess,10)
        print(str(count) + '\t' + str(guess) + '\t' + str(computedresult))
    print(guess)
    print(math.log(10,10))

print(RecursivePrac.reverse_string("string"))