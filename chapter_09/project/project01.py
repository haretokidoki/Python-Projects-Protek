def ubahHuruf(teks, a, b):
  newteks = ""
  for x in teks.split():
    seteks = x.replace(a, b)
  
  return newteks.join(seteks)

teks = input("Masukkan kata : ")
a = input("Masukkan huruf yang akan diganti : ")
b = input("Masukkan huruf pengganti : ")

print("Kata setelah diubah hurufnya : ", ubahHuruf(teks, a, b))