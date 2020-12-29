try:
  file = open("txt_file/mahasiswa.txt","a")
  rep = 'y'

  while(rep == 'y'):
    print()
    nim    = input("Masukkan NIM    : ")
    nama   = input("Masukkan Nama   : ")
    alamat = input("Masukkan Alamat : ")
    bio = nim+'|'+nama+'|'+alamat+'\n'
    file.write(bio)
    print()
    rep = input("Ingin mengulang lagi?(y/n) : ")

  file.close()
    
except FileNotFoundError:
  print("File tidak ditemukan")