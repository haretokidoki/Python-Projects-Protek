# fungsi untuk mencari nilai tengah dari n
def nilaiTengah(n):
  spt = []
  x = 1
  while(x <= n):
    spt.append(x)
    x += 1
  tengah = sorted(spt)[len(spt)//2]
  return tengah

# fungsi tampilkan bintang
def bintang(n):
  i = 0
  x = 1
  tgh = nilaiTengah(n)

  # jumlah naik
  while (i < tgh):
    print(('*'*x).center(1+2*tgh," "))
    x += 2
    i += 1
  
  nilaiLanjut = n - tgh
  x -= 4

  # jumlah turun
  while (nilaiLanjut > 0):
    print(('*'*x).center(1+2*tgh," "))
    x -= 2
    nilaiLanjut -= 1

# variabel n default untuk memicu perulangan input
n = 2

# input jumlah baris
while(n % 2 == 0):
  n = int(input("Masukkan jumlah baris : "))
  if(n % 2 == 0):
    print("\nMasukkan hanya bilangan ganjil!\n")

# panggil fungsi tampilkan bintang
bintang(n)