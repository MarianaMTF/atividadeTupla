def populoso(paises):
  maior=0
  pais=None
  i=0
  j=1
  while j<len(paises)-1:
    pais_1=paises[i]
    pais_2=paises[j]
    if pais_1[1]>pais_2[1]:
      maior=pais_1[1]
      pais=pais_1[0]
    i+=1
    j+=1
  print(f"{pais} é o mais populoso, {maior} pessoas")
paises=[("brasil", 212600000), ("estados unidos", 319800000), ("china", 144100000), ("india", 138000000), ("eua", 127000000), ("argentina", 108000000)]
populoso(paises)
