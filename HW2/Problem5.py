import random
from Problem3 import Partition
import itertools

def median_partition(A,p,r):
    if (A[p] >= A[(p+r)//2] and A[(p+r)//2] >= A[r]) or (A[r] >= A[(p+r)//2] and A[p] <= A[(p+r)//2]):
        A[r],A[(p+r)//2] = A[(p+r)//2], A[r]
    elif (A[r] >= A[(p+r)//2] and A[r] <= A[p]) or (A[r] >= A[p] and A[r] <= A[(p+r)//2]):
        A[r],A[r] = A[r],A[r]
    else:
        A[p],A[r] = A[r],A[p]
    return Partition(A,p,r)

def median_quicksort(A,p,r):
    if p < r:
        q = median_partition(A,p,r)
        median_quicksort(A,p,q-1)
        median_quicksort(A,q+1,r)


list1 = []
for i in range(10):
    list1.append(random.randint(-10,20))
perms = itertools.permutations(list1)
print(list1)
median_quicksort(list1,0,len(list1)-1)
print(list1)
