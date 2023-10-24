def maior_num(numeros):
  lista=list(numeros)
  maior=0
  for num in lista:
    if maior<num:
      maior=num
  return maior
def menor_num(numeros):
  lista=list(numeros)
  menor=0
  for num in lista:
    if menor>num:
      menor=num
  return menor
numeros=(1, 5, 19, 20, 3, 4, 2, 7, 8, 9, 11, 12, 13, 14, 15,)
maior=maior_num(numeros)
menor=menor_num(numeros)
print(f"{maior} é o maior")
print(f"{menor} é o menor")
