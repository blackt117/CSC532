import random
import Problem3

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    A[r], A[i] = A[i], A[r]
    return Problem3.Partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q-1)
        randomized_quicksort(A,q+1,r)


list1 = []
for i in range(0,10):
    list1.append(random.randint(0,10))
print(list1)
randomized_quicksort(list1,0,len(list1)-1)
print(list1)
