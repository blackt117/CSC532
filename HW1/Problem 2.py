import random
import time
def mystery1(mylist):
    x = mylist[0]
    for i in range(0, len(mylist), 2):
        print(i)
        if mylist[i] > x:
            x = mylist[i]
    return x


def mystery2(mylist):
    t =0
    z = 0
    for i in range(len(mylist) - 1):
        j = i
        while j > 0:
            t += 1
            #if mylist[i] == mylist[j]:
                #return False
            j = j // 2
        z += 1
    #return True
    print(z + t)

list1 =[]
for i in range(1):
    list1.append(random.randint(1,10))
#mystery1(list1)
#mystery2(list1)


def mystery5(n):
    if n <= 1:
        print('i')
        return n
    else:
        print('i')
        return n*mystery5(n-1)

def mystery6(myList):
    reversedList = []
    for j in range(len(myList)):
        reversedList.insert(0, myList[j])
    return reversedList

list4 = []
for i in range(100,10000,150):
    for j in range(i):
        list4.append(random.randint(0,100))
    starttime = time.perf_counter()
    mystery6(list4)
    endtime = time.perf_counter()
    print(i,'\t', endtime-starttime)

def mystery4(n):
    c = 1
    k = 1
    i = 0
    while k <= n:
        c += 1
        k = 2 * k
        i +=1
    print(i)
    return c
mystery4(1024)
mystery5(5)

# for i in range(250,10000,100):
#     starttime = time.perf_counter()
#     mystery4(i)
#     endtime = time.perf_counter()
#     print(i,'\t',endtime-starttime)
def interpolationSearch(arr, lo, hi, x):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)

        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1
list1 = []
# for i in range(1000,50000,200):
#     for j in range(i):
#         list1.append(random.randint(0, 100))
#     list1.sort()
#     starttime = time.perf_counter()
#     interpolationSearch(list1,0,len(list1)-1,50)
#     endtime = time.perf_counter()
#     print(i,'\t', endtime-starttime)

