import random
randomlist = random.sample(range(1, 1000), 8)
print("Lista desordenada:", randomlist)


def insertion_sort(arr):

    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

        i += 1
    
    return arr

y = randomlist
print("Lista ordenada:", insertion_sort(y))
