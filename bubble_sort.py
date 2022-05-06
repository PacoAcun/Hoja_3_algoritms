def bubble_sort(arr):

    for i in range(0, len(arr)):

            for j in range(0, len(arr) -1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

unsorted_list = [-2, 45, 0, 11, -9]
print("Lista desordenada: ", unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("Lista ordenada: ", sorted_list)