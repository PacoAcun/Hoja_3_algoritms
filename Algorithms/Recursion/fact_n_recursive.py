def fact(n):

    if n == 1 or n == 0:
        return 1

    else:
        return n * fact(n - 1)
        

x = input("Ingrese un numero para saber su factorial: ")
y = fact(int(x))

print("El factorial de", x,"es", y)