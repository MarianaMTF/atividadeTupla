def verificar(numeros):
  pares=[]
  for i in numeros:
    if i%2==0:
      pares.append(i)
  pares=tuple(pares)
  return pares
numeros=(1,2,3,4,5,6,7,8,9,10)
pares=verificar(numeros)
print(pares)
