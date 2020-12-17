# mengimport fungsi random dari pustaka
import random

#function menentukan faktorial dari len(string) untuk menentukan batas akhir dari huruf yang dapat disusun
def faktorial(x):
  k = len(x) 
  i = k
  while (k > 1):
    k -= 1
    i *= k
  return i

#function program utama untuk memproses input dan menampilkan output
def mainprocess(x, n):
  listx = []
  fact = faktorial(x)
  i = 0
  while(i<n):
    a = shuffleString(x, n)
    if(a in listx):
      if(i == fact):
        break
      else:
        i+=0
    else:
      listx.append(a)
      i+=1
  print(listx)

#function untuk mengacak string dan memasukkannya dalam list
def shuffleString(x, n):
  str2 = ""
  str1 = random.sample(x, len(x))
  return str2.join(str1)

x = input("Masukkan kata yang akan di random : ")
n = int(input("Masukkan banyak kata yang dihasilkan : "))

print("\n Hasil setelah diacak :")
mainprocess(x, n)