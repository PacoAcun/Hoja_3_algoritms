import sys
sys.setrecursionlimit(2000)

def sum_n(num):

    if num == 1:
        return 1

    else:
        return num + sum_n(num - 1)