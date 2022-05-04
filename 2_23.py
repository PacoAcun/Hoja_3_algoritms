def suma(h):
    import random
    randomlist = random.sample(range(1, 1000), 50)
    print(randomlist)

    x = 0
    y = 0
    n = input("Numero: ")

    for i in range(len(randomlist)):

        if n > i +1:
            h = i + (i+1)
        
        elif n == i +1:
            return suma
        
        #if n > y:
           #h = randomlist[x] + randomlist[y]
           #x += 1
           #y += 1

        #elif y == n:
            #return suma

h = 0
print(suma(h))
