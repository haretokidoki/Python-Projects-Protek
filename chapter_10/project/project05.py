# cek apakah file ada
try:
  filein = open('txt_file/angkagaris.txt','r')
except FileNotFoundError:
  print("File tidak ditemukan!")

#input file tujuan
filex = input("Masukkan nama file tujuan : ")

# buka file tujuan
fileout = open('txt_file/'+filex+'.txt','a')

# menambahkan angka dari variabel a+b
def numberCounter(filein, fileout):
  for x in filein:
    number = x.split('|')
    a = number[0]
    b = number[1]
    fileout.write(a+b)
  print("Output sudah disimpan di", fileout.name)

numberCounter(filein, fileout)
filein.close()
fileout.close()