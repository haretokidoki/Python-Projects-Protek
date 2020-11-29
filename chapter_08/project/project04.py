#deklarasi isi list sayur
sayur = ["bayam", "kangkung", "wortel", "selada"]

#function menampilkan daftar sayur
def printSayur():
  print("Daftar Data Sayur : ")
  for i in range(len(sayur)):
    print(i+1,".",sayur[i])
  showMenu()

#function memasukkan data sayur ke dalam list
def inputSayur():
  saybr = input("Masukkan nama sayur yang ingin ditambahkan : ")
  sayur.append(saybr)
  print()
  print(saybr, "berhasil ditambahkan!")
  showMenu()

#function menghapus data sayur
def hapusSayur():
  sayhp = input("Masukkan nama sayur yang ingin dihapus: ")
  try:
    sayur.remove(sayhp)
    print()
    print(sayhp,"berhasil dihapus!")
    showMenu()
  except ValueError:
    print()
    print("Data", sayhp,"tidak ditemukan!")
    print()
    ulangHapus()

#function konfirmasi ulang
def ulangHapus():
  ulang = input("Ulangi(y/n)? ")
  print()
  if(ulang.lower() == "y"):
    hapusSayur()
  elif(ulang.lower() == "n"):
    showMenu()
  else:
    print("Inputan salah!")
    print()
    ulangHapus()

#function menampilkan menu awal
def showMenu():
  print()
  print("Menu : \nA. Tambah Data Sayur \nB. Hapus Data Sayur \nC. Tampilkan Data Sayur \nD. Keluar Program")
  menu = input("Pilih A/B/C/D : ")

  if(menu.upper() == "A"):
    print()
    inputSayur()
  elif(menu.upper() == "B"):
    print()
    hapusSayur()
  elif(menu.upper() == "C"):
    print()
    printSayur()
  elif(menu.upper() == "D"):
    print()
    print("Program telah dihentikan")
    print()
    exit()
  else:
    print()
    print("Data yang anda masukkan salah!")
    showMenu()

print()
print("=========== APLIKASI MANAGER SAYUR ===========")
showMenu()
