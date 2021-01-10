from datetime import *
file = open('txt_file/dataPinjam.txt', 'a')
loop = 'y'

while(loop == 'y'):
  loop = 'x'
  kode = input("Masukkan Kode Member : ")
  nama = input("Masukkan Nama Member : ")
  buku = input("Masukkan Judul Buku  : ")
  tglp = datetime.date(datetime.now())
  tglk = tglp + timedelta(days=7)
  pnjm = kode+'|'+nama+'|'+buku+'|'+str(tglp)+'|'+str(tglk)
  file.write(pnjm+'\n')
  while(loop == 'x'):
    print()
    loop = input('Ingin memasukkan data lagi?(y/n): ')
    if(loop == 'y'):
      print()
    elif(loop == 'n'):
      print()
    else:
      print('\nMasukkan hanya y atau n!')
      loop = 'x'

file.close()