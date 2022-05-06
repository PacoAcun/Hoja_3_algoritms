import random
randomlist = random.sample(range(1, 1000), 8)
print("Lista desordenada:", randomlist)

def select_sort(arr):

    for i in range (len(arr)):
        l = i

        for j in range (i + 1, len(arr)):
            if arr[j] < arr[l]:
                l = j
        
        arr[i], arr[l] = arr[l], arr[i]

    return arr


y = randomlist
print("Lista ordenada:", select_sort(y))