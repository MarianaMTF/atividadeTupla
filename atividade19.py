def maiores(numeros):
  maiores=[]
  for i in numeros:
    if i>=10:
      maiores.append(i)
  maiores=tuple(maiores)
  return maiores
numeros=(4,8,9,10,14,3,5,7,1,2,20)
n_maiores=maiores(numeros)
print(f"{n_maiores} maiores que 10")
