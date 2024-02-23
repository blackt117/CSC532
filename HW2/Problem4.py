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
for i in range(3):
    list1.append(random.randint(0,10))
print(list1)
randomized_quicksort(list1,0,len(list1)-1)
print(list1)

list2 =[]

for i in range(10):
    list2.append(random.uniform(0,1))
print(list2)
randomized_quicksort(list2,0,len(list2)-1)
print(list2)