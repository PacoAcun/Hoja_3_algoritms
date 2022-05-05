def suma(h):
    import random
    randomlist = random.sample(range(1, 1000), 50)
    print(randomlist)

    n = input("Indica el indice: ")

    for i in range(len(randomlist)):

        if int(n) > int(i +1) or int(n) == int(i + 1):
            h = randomlist[i] + randomlist[i+1]
            print(i)
            print(i +1)
        
        elif int(n) < int(i + 1):
            return h
        
        #if n > y:
           #h = randomlist[x] + randomlist[y]
           #x += 1
           #y += 1

        #elif y == n:
            #return suma

h = 0
print(suma(h))
