# cek apakah file ada
path = 'txt_file/angkagaris.txt'

try:
  filein = open(path,'r')
except FileNotFoundError:
  print("File tidak ditemukan!")

# buat file tujuan
fileout = open(path[:len(path)-4]+"_hasil.txt",'w+')

# menambahkan angka dari variabel a+b
def numberCounter(filein, fileout):
  for x in filein:
    number = x.split('|')
    a = int(number[0])
    b = int(number[1])
    fileout.write(str(a+b)+"\n")
  print("Output sudah disimpan di", fileout.name)

numberCounter(filein, fileout)
filein.close()
fileout.close()