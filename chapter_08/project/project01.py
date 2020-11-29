#import fungsi dari project 2 dan 5
from project02 import *
from project05 import *

try:
  nbil = int(input("Masukkan jumlah bilangan : "))
  n = 1
  bil = []

  while(n <= nbil):
    print("Masukkan bilangan bulat ke-", n," : ", end=" ")
    x = int(input(""))
    bil.append(x)
    n += 1

  bil = list(bil)
  sbil = list(bil)
  sbil.sort(reverse = True)

  print()
  print("Nilai Awal")
  print("List nilai yang anda masukkan : ")
  print(bil)

  print()
  print("Project 1")
  print("List nilai yang anda masukkan dari besar ke kecil : ")
  print(sbil)

  print()
  print("Project 2")
  print("Rata-rata nilai, nilai tertinggi dan nilai terendah : ")
  print(dataStat(bil))

  print()
  print("Project 5")
  print("Hasil kuadrat setiap nilai dalam list (sebelum diurutkan) : ")
  print(kuadrat(bil))

except ValueError:
  print("Data yang anda masukkan harus berupa bilangan bulat!")