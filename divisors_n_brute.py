def divisor(n):

    d = []

    for i in range (1, n + 1):
        if n % i == 0:
            d.append(i)
            
    return d

n = input("Ingrese un numero: ")
result = divisor(int(n))
print("numero: "+str(n)+ " divisores: "+str(result))