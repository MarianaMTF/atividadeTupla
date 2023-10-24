def ordernar_data(datas):
  datas=[(data[2], data[1], data[0])for data in datas]
  datas.sort()
  datas=[(data[2], data[1], data[0])for data in datas]
  return datas
datas=[(15,4,2005),(23,4,2005),(11,1,2001),(10,7,20015),(20,10,20011)]
datas=ordernar_data(datas)
print(datas)
