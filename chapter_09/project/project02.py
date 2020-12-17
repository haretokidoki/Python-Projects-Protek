def bintang(n):
  i = 0
  x = 1
  while (i < n):
    print(('*'*x).center(1+2*n))
    x += 2
    i += 1

n = int(input("Masukkan panjang baris : "))
bintang(n)