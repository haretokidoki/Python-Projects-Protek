buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7600, 'duku' : 6500}
total = 0

#function tampilkan buah
def showBuah(buah):
  print("List Buah :")
  for n,i in buah.items():
    print("-",n,str(i)+"/kg")

#function masukkan nama buah
def inputBuah():
  global harga
  beli = input("Nama buah yang ingin dibeli : ")
  habel = buah.get(beli.lower())
  if (habel==None):
    print()
    print("Buah tidak ditemukan!")
    print()
    inputBuah()
  else:
    harga = inputKilo(habel)
    return harga

#function masukkan berat buah
def inputKilo(habel):
  harga = 0
  try:
    kg = int(input("Berat buah yang ingin dibeli (Kg) : "))
    harga = habel*kg
  except ValueError:
    print("Masukkan hanya angka saja!")
    inputKilo(habel)
  return harga

#function tampilkan harga buah
def hargaBuah(total):
  print("="*45)
  print("Total harga buah adalah : Rp. "+str(total))
  
#variabel untuk melakukan perulangan jika input salah
rep = 'y'

print("="*45)
showBuah(buah)
print("="*45)
while(rep.lower() == 'y' ):
  inputBuah()
  ingin = 'y'
  while(ingin != 'n'):
    print()
    rep = input("Ingin menambahkan lagi (y/n)? ")
    print()
    if (rep.lower() == 'y'):
      total += harga
      ingin = 'n'
    elif (rep.lower() == 'n'):
      total += harga
      ingin = 'n'
    else:
      print("Masukkan hanya huruf y/n!")
      print()
      ingin = 'y'
    
hargaBuah(total)