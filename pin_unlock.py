def unlock(pin):

    code = pin

    for i in range(10):
        for j in range (10):
            for t in range (10):
                for u in range (10):
                    guess = str(i)+ str(j)+ str(t)+ str(u)
                    print(guess)
                    

                    if guess == code:
                        x = "El pin es: "+ guess
                        return x


n = input("Indique un pin: ")
print(unlock(str(n)))
