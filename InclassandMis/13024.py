import random
def exp(num,pow):
    if pow == 1:
        return num
    else:
        return num * exp(num,pow-1)

print(exp(5,3))

def exp_rec(num,pow):
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    elif pow % 2 == 0:
        return exp_rec(num*num,pow//2)
    else:
        return num * exp_rec(num*num,pow//2)


print(exp_rec(5,4))
def divideAndConquer(ans,n):
    if n == 0:
        return 1, 0
    if n == 1:
        return ans, 0
    if n % 2 == 0:
        ans, count = divideAndConquer(ans*ans, n // 2)
        return ans, count + 1
    else:
        ans, count = divideAndConquer(ans*ans, n // 2)
        ans = ans*ans
        return ans, count + 2


def KadanesAlgorithm(A, low, high):
    maxSoFar = float('-inf')
    startSoFar = low
    endSoFar = low

    maxSumEndingHere = 0
    newStart = low
    for i in range(low, high+1):
        maxSumEndingHere = maxSumEndingHere + A[i]
        if (maxSoFar < maxSumEndingHere):
            maxSoFar = maxSumEndingHere
            startSoFar = newStart
            endSoFar = i
        if maxSumEndingHere < 0:
            maxSumEndingHere = 0
            newStart = i+1
    return (startSoFar,endSoFar,maxSoFar)

list1=[]
for i in range(4):
    list1.append(random.randint(-10,10))

print(list1)

print(KadanesAlgorithm(list1,0,len(list1)-1))

