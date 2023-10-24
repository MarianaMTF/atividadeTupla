def maior(tupla):
  for i in tupla:
    if len(i)>=5:
      print(f"a palavra {i} tem mais de 5 caracteres")
tupla=("cachorro", "escola", "mariana", "banana", "enzo", "jogo")
maior(tupla)
