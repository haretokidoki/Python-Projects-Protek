#deklarasi variabel
repeatx = 'y'
sum = 0
n = 0

print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

#masukkan bilangan
def inputNilai():
  global sum
  global n
  global avg

  while(repeatx == 'y'):
    try:
      print()
      nilai = int(input("Masukkan bilangan bulat : "))
      sum = sum + nilai
      n += 1
      avg = sum/n
      ulangiInput()
    except ValueError:
      print("Input yang anda masukkan bukan bilangan bulat!")

#ulangi inputan
def ulangiInput():
  repeatx = input("Ingin menambahkan data lagi (y/n)? ")
  if(repeatx != 'y'):
    if(repeatx != 'n'):
      print("Masukan hanya huruf y atau n kecil saja!")
      print()
      ulangiInput()
    else:
      print()
      print("Rata-ratanya adalah : ", avg)
      exit()

#badan program
inputNilai()