# praktikum 2 nomor 13
from random import randint
jml = 0
while True:
  bil = randint(0, 10)
  print(bil)
  jml += 1
  if(bil == 5):
    print("Jumlah perulangan : "+str(jml))
    break