# import fungsi semua fungsi dari library datetime
from datetime import *

# variabel untuk memudahkan perulangan program
loop = 'y'

# function cari data berdasarkan kode member
def findData(file, target):
  dataM = ' '
  for x in file:
    part = x.rstrip().split('|')
    kode = part[0]
    if(kode == target):
      dataM = part
      break
    else:
      dataM = ' '   
  return dataM  

# function tampilkan data
def showData(file, target):
  datM = findData(file, target)
  if(datM == ' '):
    print("Data tidak ditemukan!")
  else:
    today = datetime.date(datetime.now())
    exp = datetime.strptime(str(today), '%Y-%m-%d') - datetime.strptime(datM[4], '%Y-%m-%d')
    # cek keterlambatan, menetapkan nilai denda jika pengembalian terlambat
    if(int(exp.days)>0):
      exp = int(exp.days)
      denda = exp*2000
    else:
      exp = 0
      denda = 0
    print()
    print("Data Peminjam Buku")
    print("Kode Member               :",datM[0])
    print("Nama Member               :",datM[1])
    print("Judul Buku                :",datM[2])
    print("Tanggal Peminjaman        :",datM[3])
    print("Tanggal Pengembalian Max. :",datM[4])
    print("Tanggal Pengembalian      :",today)
    print("Terlambat                 :",str(exp)+' hari')
    print("Denda                     :","Rp."+str(denda))

# badan program
while(loop == 'y'):
  loop = 'x'
 
  try:                                            # membuka file, saya taruh disini agar tidak terjadi error 
    file = open('txt_file/dataPinjam.txt','r')    # saat melakukan perulangan input dimana program akan
  except FileNotFoundError:                       # membaca baris file selanjutnya sehingga menyebabkan error
    print("File tidak ditemukan")

  # input kode member yang ingin dicari
  cari = input("Masukkan Kode Member : ")
  
  # panggil function tampilkan data
  showData(file, cari)

  # konfirmasi untuk mengulangi program
  while(loop == 'x'):
    print()
    loop = input("Ingin mencari lagi?(y/n): ")
    if(loop == 'y'):
      print()
    elif(loop == 'n'):
      print()
    else:
      loop = 'x'
      print("Masukkan hanya y/n!")

    # menutup file sehingga program dapat membaca file dari awal ketika program diulangi
    file.close()