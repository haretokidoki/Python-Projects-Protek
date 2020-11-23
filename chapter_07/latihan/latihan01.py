#input nama dan lokasi file
path = input("Masukkan lokasi dan nama file : ")

#pengecekan ada atau tidaknya file yang diinputkan
try:
  file = open(path,"r")
except:
  print("file tidak ditemukan!")
  exit()

#menampilkan isi file
print("Isi dari file", path, "adalah : ")
print(file.read())