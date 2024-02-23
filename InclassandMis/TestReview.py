import random
import time
def mystery1(A,B,k):
    C = [0] * (k+1)

    for i in range(len(A)):
        C[A[i]] = C[i] + C[i-1]
    for j in range(0,k):
        B[C[A[j]]] = C[j] + A[j]


list1 = []
list2 = []
for i in range(100,50000,750):
    list1=[]
    list2=[]
    for j in range(i):
        list1.append(random.randint(-10,10))
        list2.append(random.randint(-10,10))
    starttime = time.perf_counter()
    mystery1(list1,list2,i)
    endtime = time.perf_counter()
    print(i,"\t",endtime-starttime)
