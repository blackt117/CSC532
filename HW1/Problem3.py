import random
import time
def merge_sert(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        leftside = list1[:mid]
        rightside = list1[mid:]


        merge_sert(leftside)
        merge_sert(rightside)

        i,j,k = 0,0,0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] <= rightside[j]:
                list1[k] = leftside[i]
                i = i + 1
            else:
                list1[k] = rightside[j]
                j += 1
            k += 1

        while i < len(leftside):
            list1[k] = leftside[i]
            i+=1
            k+=1

        while j < len(rightside):
            list1[k] = rightside[j]
            j+=1
            k+=1

def insert_sort(list1):
    for i in range (1,len(list1)):
        cur_index = i
        cur_val = list1[i]
        while cur_index > 0 and cur_val <= list1[cur_index-1]:
            list1[cur_index] = list1[cur_index-1]
            list1[cur_index-1] = cur_val
            cur_index -= 1


def rec_max(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        result = rec_max(list1[1:])
        if result >= list1[0]:
            return result
        else:
            return list1[0]


def insert_sort_book(list1):
    starttime = time.perf_counter()
    for i in range(1,len(list1)):
        key = list1[i]
        j = i - 1
        while list1[j] > key and j >= 0:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = key
    endtime = time.perf_counter()
    print(endtime - starttime)

list2 = []
list3 = []
for j in range(10000):
    list3.append(random.randint(0,100))
for i in range(10000):
    list2.append(random.randint(0,100))

print()

insert_sort_book(list2)
starttime1 = time.perf_counter()
merge_sert(list3)
endtime1 = time.perf_counter()
print(endtime1 - starttime1)



