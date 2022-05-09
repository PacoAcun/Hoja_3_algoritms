def order(arr):

    for i in range(0, len(arr)):

            for j in range(0, len(arr) -1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr





def search(arr , n):
    l = 0
    r = len(arr) -1

    while l <= r:
        m = (l + r) // 2
        
        if arr[m] == n:
            return m

        elif n < arr[m]:
            r = m - 1
        
        else:
            l = m + 1
    
    return -1
