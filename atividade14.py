def repetidos(numeros):
  repetidos=[]
  for i in numeros:
    if i not in repetidos:
      repetidos.append(i)
  repetidos=tuple(repetidos)
  return repetidos
numeros=(1,1,2,3,4,4,5,6,7,7,8,9,10,10,11,12,13,13,14,15,16)
num_repetidos=repetidos(numeros)
print(num_repetidos)
