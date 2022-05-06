def order(arr):

    for i in range(0, len(arr)):

            for j in range(0, len(arr) -1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

y = [-2, 45, 0, 11, -9, 8, 30, 60, 2, 20]
print("Lista desordenada: ", y)

z = order(y)
print("Lista ordenada: ", z)




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

n = int(input("Ingresa el numero que quieras buscar: "))
x = search(y , n)


if x == -1:
    print("El numero", n, "no esta en la lista")
    
else:
    print("El numero", n, "esta en el indice", x)
