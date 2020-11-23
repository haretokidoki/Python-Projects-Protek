#input nama file
path = input("Masukkan nama file : ")

#validasi apakah file ada atau tidak
try:
  trial = open(path, "r")
except:
  print("file tidak ditemukan!")
  exit()

#membuka file yang diinputkan
file = open(path, "a")

#input data baru
def inputData():
  data = input("Masukkan data yang ingin ditambahkan : ")
  file.write("\n"+data)

#ulangi masukan data
def ulangiInput():
  repeatx = input("Ingin menambahkan data lagi (y/n)? ")
  if(repeatx != 'y'):
    if(repeatx != 'n'):
      print("Masukan hanya huruf y atau n kecil saja!")
      print()
    else:
      file.close
      exit()

#badan program
repeatx = 'y'
while(repeatx == 'y'):
  print()
  inputData()
  repeatx = 'n'
  while(repeatx != 'y'):
    ulangiInput()