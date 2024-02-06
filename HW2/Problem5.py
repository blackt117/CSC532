import random
import Problem3

def median_partition(A,p,r):
    if (A[p] >= A[(p+r)//2] and A[(p+r)//2] <= A[r]) or (A[r] >= A[(p+r)//2] and A[p] <= A[(p+r)//2]):
        A[r],A[(p+r)//2] = A[(p+r)//2], A[r]
    elif (A[r] >= A[(p+r)//2] and A[r] <= A[p]) or (A[r] >= A[p] and A[r] <= A[(p+r)//2]):
        A[r],A[r] = A[r],A[r]
    else:
        A[p],A[r] = A[r],A[p]
    return Problem3.Partition(A,p,r)

def median_quicksort(A,p,r):
    if p < r:
        q = median_partition(A,p,r)
        median_quicksort(A,p,q-1)
        median_quicksort(A,q+1,r)

list1 = []
for i in range(0,4):
    list1.append(random.randint(-10,20))
print(list1)
median_quicksort(list1,0,len(list1)-1)
print(list1)
