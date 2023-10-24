def somar(tupla_1, tupla_2):
  tupla_aux=[]
  for i in range(len(tupla_1)):
    tupla_aux.append(tupla_1[i]+tupla_2[i])
  tupla_aux=tuple(tupla_aux)
  return tupla_aux
tupla_1=(1,2,3,4,5,6,7,8,9,10)
tupla_2=(11,12,13,14,15,16,17,18,19,20)
tupla_3=somar(tupla_1, tupla_2)
print(tupla_3)
