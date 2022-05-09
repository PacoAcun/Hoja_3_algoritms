import sys
sys.setrecursionlimit(2000)

def fibo(num):

    if num == 1:
        return 1

    elif num == 0:
        return 0

    else:
        return fibo(num - 1) + fibo(num - 2)
