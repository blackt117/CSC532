import random

class heap(object):
    def __init__(self,list1,size):
        self.heap = list1
        self.size = size

def parent(i):
    return (i//2)

def left_child(i):
    return (2*i)

def right_child(i):
    return (2*i) + 1

def max_heapify(list1,i):
    l = left_child(i)
    r = right_child(i)
    if l <= list1.size and list1.heap[l] < list1.heap[i]:
        largest = l
    else:
        largest = i
    if r <= list1.size and list1.heap[r] < list1.heap[largest]:
        largest = r
    if largest != i:
        list1.heap[i],list1.heap[largest] = list1.heap[largest],list1.heap[i]
        max_heapify(list1,largest)

def build_max_heap(list1):
    print('t')
    z = len(list1.heap)
    z = (z//2)
    for i in range(z,0,-1):
        print('t')
        max_heapify(list1,i)

def heapsort(list1):
    build_max_heap(list1)
    for i in range(len(list1.heap)-1,1,-1):
        list1.heap[1],list1.heap[i] = list1.heap[i],list1.heap[1]
        list1.size -= 1
        max_heapify(list1,1)

list1 = [None]
for i in range(2):
    list1.append(random.randint(0,100))
A=heap(list1,len(list1)-1)
print(A.heap)
heapsort(A)
print(A.heap)
