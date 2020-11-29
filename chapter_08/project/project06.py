#function mengurutkan buah berdasar 
def sortStringByChar(buah):
  buah.sort(key = len, reverse = True)
  return buah

nbuah = int(input("Masukkan jumlah buah : "))
buah = []
loop = 1

while (loop <= nbuah):
  print("Masukkan nama buah ke-"+str(loop),":", end=" ")
  b = input("")
  buah.append(b)
  loop += 1

print("\nList nama buah dari karakter terbanyak ke paling sedikit:")
print(sortStringByChar(buah))
