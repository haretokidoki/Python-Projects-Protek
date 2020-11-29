from project08 import *

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7600, 'duku' : 6500}

def showBuah(buah):
  print("List Buah :")
  for n,i in buah.items():
    print(n, i)

def palingMahal():
  sbuah = sorted(buah.items(), key=lambda x: x[1], reverse = True)
  print(sbuah[0][0])

showBuah(buah)
print()
print("Project 7")
print("Buah yang paling mahal harga satuannya: ", end="")
palingMahal("Project 8")
print("Rata- rata harga buah : ",ratarata(buah))