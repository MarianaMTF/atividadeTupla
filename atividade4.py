def soma_num(numeros):
  lista=list(numeros)
  soma=0
  for i in lista:
    soma+=i
  return soma
numeros=(1,2,3,4,5,6,7,8,9,10)
soma=soma_num(numeros)
print(soma)
