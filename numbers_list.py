def searchlist():
  import random
  randomlist = random.sample(range(1, 1000), 25)
  print(randomlist)

  y = randomlist[0]
  x = 0

  for i in randomlist:
    if x == 0 or i > x :
      x = i

    elif i < y :
      y = i

  print()
  print("El maximo es:", x)
  print("El minimo es:", y)

print(searchlist())