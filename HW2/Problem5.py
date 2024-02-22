import random
from Problem3 import Partition
from Problem3 import quicksort_rightmost
import itertools
import time
from Problem4 import randomized_quicksort
from Problem4 import randomized_partition

def median_partition(A,p,r):
    if r - p >= 3:

        m = (p + r) // 2
        if (A[p] >= A[m] and A[m] >= A[r]) or (A[r] >= A[m] and A[p] <= A[m]):
            A[r], A[m] = A[m], A[r]

        elif (A[r] >= A[m] and A[r] <= A[p]) or (A[r] >= A[p] and A[r] <= A[m]):
            pass  # A[r],A[r] = A[r],A[r]
        else:
            A[p], A[r] = A[r], A[p]
    return Partition(A, p, r)
    # if (A[p] >= A[(p+r)//2] and A[(p+r)//2] >= A[r]) or (A[r] >= A[(p+r)//2] and A[p] <= A[(p+r)//2]):
    #     A[r],A[(p+r)//2] = A[(p+r)//2], A[r]
    # elif (A[r] >= A[(p+r)//2] and A[r] <= A[p]) or (A[r] >= A[p] and A[r] <= A[(p+r)//2]):
    #     A[r]=A[r]
    # else:
    #     A[p],A[r] = A[r],A[p]
    # print(A[r])
    # return Partition(A,p,r)

def median_quicksort(A,p,r):
    if p < r:
        q = median_partition(A,p,r)
        median_quicksort(A,p,q-1)
        median_quicksort(A,q+1,r)


print("N","\t","Median","\t","Rightmost","\t", 'Random')
for i in range(100,100000,950):
    list1 = []
    list2 =[]
    list3 =[]
    for s in range(i):
        list1.append(random.randint(-100000,20000000))
        list2.append(random.randint(-100000,2000000))
        list3.append(random.randint(-100000,2000000))
    start_time_median = time.perf_counter()
    median_quicksort(list1,0,len(list1)-1)
    end_time_median = time.perf_counter()
    start_time_right = time.perf_counter()
    quicksort_rightmost(list2,0,len(list2)-1)
    end_time_right = time.perf_counter()
    start_time_random = time.perf_counter()
    randomized_quicksort(list3,0,len(list3)-1)
    end_time_random = time.perf_counter()
    print(i,"\t", end_time_median-start_time_median,"\t",end_time_right-start_time_right,"\t", end_time_random-start_time_random)

# list1 = []
# for i in range(3):
#     list1.append(random.randint(-10,100))
# print(list1)
# median_quicksort(list1,0,len(list1)-1)
# print(list1)
