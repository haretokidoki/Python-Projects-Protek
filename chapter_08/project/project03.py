#tampilkan output
def printMhs(namamhs):
  for i in range(len(namamhs)):
    print(namamhs[i], " (", len(namamhs[i])," Karakter ) ")

try: 
  #input jumlah mahasiswa
  nmhs = int(input("Masukkan jumlah Mahasiswa : "))
  print()
  
  n = 1
  namamhs = []

  print("="*45)
  print()

  #input nama mahasiswa
  while(n <= nmhs):
    x = ""
    print("Masukkan nama Mahasiswa ke-", n,":", end=" ")
    x = input("")
    namamhs.append(x)
    n += 1

  print()
  print("="*45)
  print()
  
  printMhs(namamhs)
  
  print()
  print("="*45)

except ValueError:
  print("Data yang anda masukkan salah")