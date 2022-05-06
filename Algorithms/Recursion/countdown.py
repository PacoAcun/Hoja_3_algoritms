import time



def count(n):

    print(n)
    time.sleep(1)

    if n == 1:
        return 0

    else:
        return count(n - 1)

n = input("Cuantos segundos quieres? ")
print(count(int(n)))