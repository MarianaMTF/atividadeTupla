def pares(numeros):
  lista=list(numeros)
  for numero in lista:
    if numero%2==0:
      lista.append(numero)
  nova_tupla=tuple(lista)
  return nova_tupla
numeros=(1,2,3,3,4,5,6,7,8,9,10)
numeros=pares(numeros)
print(numeros)
