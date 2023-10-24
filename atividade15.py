def encontrar(frutas, fruta_usu):
  for fruta in frutas:
    if fruta==fruta_usu:
      print(f"{fruta} encontrada")
frutas=("pera", "banaana", "laranja", "manga", "uva", "morango", "abacaxi", "melancia", "goiaba", "kiwi")
fruta_usu=input("digite uma fruta:")
encontrar(frutas, fruta_usu)
