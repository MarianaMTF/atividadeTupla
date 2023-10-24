def ordem_alfabetica():
  cores=["azul", "vermelho", "amarelo", "verde", "branco", "preto"]
  auxiliar=[]
  alfabeto=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for letra in alfabeto:
    for cor in cores:
      if cor[0] == letra:
        auxiliar.append(cor)
  auxiliar=tuple(auxiliar)
  return auxiliar
cores=ordem_alfabetica()
print(cores)
