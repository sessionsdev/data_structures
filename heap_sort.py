import random
import time

def min_heap(lst, index):
    left = 2*index
    right = (2 * index) +1
    smallest = index

    if left <= (len(lst)-1) and lst[index] > lst[left]:
        smallest = left

    if right <= (len(lst)-1) and lst[smallest] > lst[right]:
        smallest = right

    if smallest != index:
        lst[index], lst[smallest] = lst[smallest], lst[index]
        min_heap(lst, smallest)



def build_min_heap(lst):
    for i in reversed(range(len(lst)//2)):
        min_heap(lst, i)



def min_heap_sort(lst):
    build_min_heap(lst)

    sorted = [None] * len(lst)
    for i in range(len(lst)):
        lst[0], lst[-1] = lst[-1], lst[0]
        sorted[i] = lst.pop()
        min_heap(lst, 0)

    return sorted

lst = []
for i in range(10000000):
    i = random.randint(1, 1000)
    lst.append(i)

lst_py = []
for i in range(10000000):
    i = random.randint(1, 1000)
    lst_py.append(i)


start = time.time()
min_heap_sort(lst)
end = time.time()
heap_time = (end - start)

start_py_sort = time.time()
lst_py.sort()
end_py_sort = time.time()
py_time = (end_py_sort - start_py_sort)

print("{:.10f}".format(heap_time))
print("{:.10f}".format(py_time))