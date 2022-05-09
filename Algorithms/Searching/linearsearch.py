import random
randomlist = random.sample(range(1, 1000), 25)

def linearsearch(randomlist, x):

  print(randomlist)

  c = False
          
  for i in range (len(randomlist)):

    if x == randomlist[i]:
      print("El numero", randomlist[i], "esta en el indice", i)
      c = True

  if c == False:
    print("El numero ingresado no se encuentra") 

x = 2
print(linearsearch(randomlist, x))
