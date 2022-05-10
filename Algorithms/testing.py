import random
from Brute_force import divisors_n_brute, pin_unlock, sum_n_brute
print()
print("--------------------------------")
print("-----------Brute_force----------")
print("--------------------------------")
print()

print("-----------Divisors of n----------")
n = 25
result = divisors_n_brute.divisor(int(n))
print("numero: "+str(n)+ " divisores: "+str(result))
print()


print("--------4-digit pin unlock--------")
pin = 2482
print(pin_unlock.unlock(str(pin)))
print()


print("------Sum of first n numbers------")
n = 5
print(sum_n_brute.suma(n))
print()





from Lists import list_merge, numbers_list
print()
print("--------------------------------")
print("--------------Lists-------------")
print("--------------------------------")
print()

print("------------List merge------------")
list1 = [1,4,9]
print("Lista 1:", list1)
list2 = [2,3,8]
print("Lista 2:", list2)
print("Lista completa:", list_merge.list_2(list1, list2))
print()


print("------Largest number in list------")
print(numbers_list.searchlist())
print()





from Recursion import countdown, fact_n_recursive, fibonacci_recursive, sum_n_recursive
print()
print("--------------------------------")
print("------------Recursion-----------")
print("--------------------------------")
print()

print("------------Countdown------------")
seg = int(5)
print(countdown.count(int(seg)))
print()


print("---------Divisors of n ----------")
num = 10
fact = fact_n_recursive.fact(int(num))
print("El factorial de", num,"es", fact)
print()


print("--------Sum of first n numbers recursive---------")
num = 10
print("La suma de los primeros", num, "es", sum_n_recursive.sum_n(int(num)))
print()


print("--------Nth fibonacci number---------")
num = 8
print("El numero", num, "en fibonacci es", fibonacci_recursive.fibo(int(num)))
print()





from Searching import binary_search, linearsearch
print()
print("--------------------------------")
print("------------Searching-----------")
print("--------------------------------")
print()

print("------------Binary search------------")
y = [-2, 45, 0, 11, -9, 8, 30, 60, 2, 20]
print("Lista desordenada: ", y)
z = binary_search.order(y)
print("Lista ordenada: ", z)
n = int(8)
x = binary_search.search(y , n)
if x == -1:
    print("El numero", n, "no esta en la lista")
else:
    print("El numero", n, "esta en el indice", x)
print()


print("---------Linear search----------")
randomlist = random.sample(range(1, 1000), 25)
x = 2
print(linearsearch.linearsearch(randomlist, x))
print()





from Sorting import bubble_sort, selection_sort, bubble_op, insertion_sort
print()
print("--------------------------------")
print("-------------Sorting------------")
print("--------------------------------")
print()

print("------------Bubble sort------------")
arr = [-2, 45, 0, 11, -9]
print("Lista desordenada: ", arr)
sorted_list = bubble_sort.bubble_sort(arr)
print("Lista ordenada: ", sorted_list)
print()


print("---------Selection sort----------")
randomlist = random.sample(range(1, 1000), 8)
print("Lista desordenada:", randomlist)
arr = randomlist
print("Lista ordenada:", selection_sort.select_sort(arr))
print()


print("---------Bubble sort optimized----------")
randomlist = random.sample(range(1, 25), 7)
print("Lista desordenada:", randomlist)
arr = randomlist
print("Lista ordenada:", bubble_op.bubble_op(arr))
print()


print("---------Insertion sort----------")
randomlist = random.sample(range(1, 1000), 8)
print("Lista desordenada:", randomlist)
arr = randomlist
print("Lista ordenada:", insertion_sort.insertion_sort(arr))
print()