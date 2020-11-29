buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7600, 'duku' : 6500}

def showBuah(buah):
  print("List Buah :")
  for n,i in buah.items():
    print("-",n,str(i)+"/kg")

def inputBuah():
  beli = input("Nama buah yang ingin dibeli : ")
  habel = buah.get(beli.lower())
  if (habel==None):
    print("Buah tidak ditemukan!")
    inputBuah()
  else:
    kg = int(input("Berat buah yang ingin dibeli (Kg) : "))
    harga = habel*kg
    hargaBuah(beli, kg, harga)

def hargaBuah(beli, kg, harga):
  print("="*45)
  print("Harga buah "+beli.lower()+" sebanyak "+str(kg)+"kg adalah : Rp. "+str(harga))
print("="*45)
showBuah(buah)
print("="*45)
inputBuah()