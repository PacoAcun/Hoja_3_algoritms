import sys
sys.setrecursionlimit(2000)

def sum_n(n):

    if n == 1:
        return 1

    else:
        return n + sum_n(n - 1)


n = input("Numero: ")
print(sum_n(int(n)))