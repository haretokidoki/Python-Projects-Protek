# function untuk melakukan enkripsi kalimat
def enkripsi(word):
  bowl = []

  for a in word:
    # huruf kapital
    if(a.isupper() == True):
      if(a == ' '):
        b = 32
        c = chr(b)
      elif(a == '\n'):
        c = ''
      else:
        b = ord("A") + ((ord("A") + ord(a) + hop) % 26)
        c = chr(b)
    #huruf kecil
    elif(a.isupper() == False):
      if(a == ' '):
        b = 32
        c = chr(b)
      elif(a == '\n'):
        c = ''
      else:
        b = ord("a") + ((ord("a") + ord(a) + hop - 12) % 26)
        c = chr(b)
    # sambung huruf
    bowl.append(c)
    bowled = ''.join(bowl)
  return bowled

path = input("Masukkan lokasi dan nama file : ")
try:
  filein = open(path, "r")
except FileNotFoundError:
  print("File tidak ditemukan!")
  exit()

# file keluaran
fileout = open(path[:len(path)-4]+"_encrypted.txt", "w+")

hop = int(input("Masukkan lompatan abjad : "))
bowl = []

for word in filein:
  enctext = enkripsi(word)
  fileout.write(enctext+"\n")

print("Output sudah disimpan di", fileout.name)
filein.close()
fileout.close()