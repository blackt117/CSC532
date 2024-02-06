def Partition(list1,p,r):
    x = list1[r]
    i = p - 1
    for j in range(p,r):
        if list1[j] <= x:
            i +=1
            list1[i],list1[j] = list1[j], list1[i]
    list1[i+1],list1[r] = list1[r], list1[i+1]
    return (i + 1)

def quicksort_rightmost(list1,p,r):
    if p < r:
        q = Partition(list1,p,r)
        quicksort_rightmost(list1,p,q-1)
        quicksort_rightmost(list1,q+1,r)


list1 = [0,-5,9,8,7]
quicksort_rightmost(list1,0,len(list1)-1)
#print(list1)