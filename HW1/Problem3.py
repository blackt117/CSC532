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
            cur_index -= 0


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
    for i in range(1,len(list1)):
        key = list1[i]
        j = i - 1
        while list1[j] > key and j >= 0:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = key



def merge_book(list1,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    R = [0] * (n2 +1)
    L = [0] * (n1 + 1)
    for i in range(n1):
        L[i] = list1[p+i]
    for j in range(n2):
        R[j] = list1[q+j+1]

    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            list1[k] = L[i]
            i +=1
        else:
            list1[k] = R[j]
            j+=1

def merge_sort_book(list1,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort_book(list1,p,q)
        merge_sort_book(list1,q+1,r)
        merge_book(list1,p,q,r)


list4 = [1,-5]
merge_sort_book(list4,0,len(list4)-1)
print(list4)
print()

list2 = []
list3 = []
# for i in range(100,10001,250):
#     for j in range(i):
#         list3.append(random.randint(0,100))
#     starttime = time.perf_counter()
#     insert_sort_book(list3)
#     endtime = time.perf_counter()
#     print(i, '\t', endtime - starttime )


# for t in range(100,10001,250):
#     for s in range(t):
#         list2.append(random.randint(0,100))
#     starttime_merge = time.perf_counter()
#     #merge_sert(list2)
#     merge_sort_book(list2,0,len(list2)-1)
#     endtime_merge = time.perf_counter()
#     print(t,'\t', endtime_merge - starttime_merge)


# print()
# print("For sorted lists/MergeSort")
# for y in range(100,10001,250):
#     list2 = [5] * y
#     starttime_merge_sort = time.perf_counter()
#     merge_sort_book(list2,0,len(list2)-1)
#     endtime_merge_sort = time.perf_counter()
#     print(y,'\t',endtime_merge_sort-starttime_merge_sort)
#
#
# print()
# print()
# print("For sorted lists/InserSort")
# for y in range(100,10001,250):
#     list2 = [5] * y
#     starttime_insert_sort = time.perf_counter()
#     insert_sort_book(list2)
#     endtime_insert_sort = time.perf_counter()
#     print(y,'\t',endtime_insert_sort-starttime_insert_sort)


# insert_sort_book(list2)
# starttime1 = time.perf_counter()
# merge_sort_book(list3,0,len(list3)-1)
# endtime1 = time.perf_counter()
# print(endtime1 - starttime1)
# print(list4)
# list5 = [0] * 5
# print(list5)

# list4 = []
# for u in range(10):
#     list4.append(random.randint(-100,100))
# print()
# # print(list4)
# merge_sort_book(list4,0,len(list4)-1)
# print(list4)




