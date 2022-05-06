def suma(n):
    import random
    randomlist = random.sample(range(1, 1000), 50)
    print(randomlist)

    h = 0
    print("Indice:", n)

    for i in range(len(randomlist)):

        if int(n) > int(i +1) or int(n) == int(i + 1):
            h = randomlist[i] + randomlist[i+1]
        
        elif int(n) < int(i + 1):
            return h
        
