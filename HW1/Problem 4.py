import random
import time
def max_subarray_crossing_book(list1,low,mid,high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + list1[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1,high+1,1):
        sum = sum + list1[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left,max_right,left_sum + right_sum)

def find_max_subarray_book(list1,low,high):
    if high == low:
        return (low,high,list1[low])
    else:
        mid = ((low + high)//2)
        (left_low,left_high,left_sum) = find_max_subarray_book(list1,low,mid)
        (right_low,right_high,right_sum) = find_max_subarray_book(list1,mid+1,high)
        (cross_low,cross_high,cross_sum) = max_subarray_crossing_book(list1,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)




def brute_force_maxarray(list1):
    sum_max = float('-inf')
    for i in range(len(list1)-1):
        sum_sub = list1[i]
        for j in range(i+1,len(list1)):
            sum_sub = sum_sub + list1[j]
            if sum_sub > sum_max:
                sum_max = sum_sub
                low_index = i
                right_index = j
    return (low_index,right_index,sum_max)


list2 = []
for i in range(10):
    list2.append(random.randint(-10,20))

# print(list2)
# print(brute_force_maxarray(list2))
# print(find_max_subarray_book(list2,0,len(list2)-1))


for i in range(100,10001,500):
    list3 =[]
    for y in range(i):
        list3.append(random.randint(-1000,1000))
    starttime = time.perf_counter()
    brute_force_maxarray(list3)
    endtime = time.perf_counter()
    print(i, '\t', endtime-starttime)




