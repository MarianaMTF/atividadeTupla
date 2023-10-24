def comprimento(palavras):
  tamanho=[]
  for palavra in palavras:
    tamanho.append(len(palavra))
  tamanho=tuple(tamanho)
  return tamanho
palavras=("python", "taylor swift", "amor", "peter")
tamanho=comprimento(palavras)
print(palavras)
print(tamanho)
