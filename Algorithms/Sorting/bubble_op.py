def bubble_op (arr):
    
    for i in range(0, len(arr)):

        sorted = True

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False

        if sorted == True:
            return arr

    return arr

y = [-2, -9, 6, 8, 50, 32, 23]

print(bubble_op(y))