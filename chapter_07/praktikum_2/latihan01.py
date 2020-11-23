try:
  #membuka file
  file = open("txt_file/data.txt","r")

  #baca baris pertama file lalu simpan ke variabel bil1 sebagai integer
  bil1 = int(file.readline())

  #baca baris kedua file lalu simpan ke variabel bil2 sebagai integer
  bil2 = int(file.readline())
  
  #hitung dan tampilkan hasil bagi
  hasil = bil1/bil2
  print(bil1, ' dibagi ', bil2, ' sama dengan ',  hasil)

except FileNotFoundError:
  print("File tidak ditemukan")

except ZeroDivisionError:
  print("Tidak dapat membagi dengan nol")

