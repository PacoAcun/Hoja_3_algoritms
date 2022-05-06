def linearsearch(list, x):

  c = False
          
  for i in range (len(list)):

    if x == list[i]:
      print("El numero", list[i], "esta en el indice", i)
      c = True

  if c == False:
    print("El numero ingresado no se encuentra") 