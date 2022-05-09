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

