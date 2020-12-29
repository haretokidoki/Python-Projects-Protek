# cek apakah file ada
try:
  file = open('txt_file/mahasiswa.txt','r')
except FileNotFoundError:
  print("File tidak ditemukan")

# function cari data berdasarkan nim  
def findData(file, target):
  n = 1
  nim = ' '
  for x in file:
    part = x.split('|')
    nim = part[0]
    if(nim == carinim):
      dataMhs = part
      break
    else:
      dataMhs = ' '
    
  return dataMhs  

# function tampilkan data
def showData(file, target):
  mhs = findData(file, target)
  if(mhs == ' '):
    print("NIM tidak ditemukan!")
  else:
    print("NIM    : ", mhs[0])
    print("Nama   : ", mhs[1])
    print("Alamat : ", mhs[2])

# input nim yang ingin dicari
carinim = input("Masukkan NIM yang ingin dicari : ")

# panggil function tampilkan data
showData(file, carinim)