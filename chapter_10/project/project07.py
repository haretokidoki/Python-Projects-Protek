# function untuk melakukan dekripsi huruf
def dekripsi(word):
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
        b = ord("A") + ((ord("A") + ord(a) - hop) % 26)
        c = chr(b)
    #huruf kecil
    elif(a.isupper() == False):
      if(a == ' '):
        b = 32
        c = chr(b)
      elif(a == '\n'):
        c = ''
      else:
        b = ord("a") + ((ord("a") + ord(a) - hop + 14) % 26)
        c = chr(b)
    bowl.append(c)
    bowled = ''.join(bowl)
  return bowled

path = input("Masukkan lokasi dan nama file : ")
try:
  filein = open(path, "r")
except FileNotFoundError:
  print("File tidak ditemukan!")
  exit()

fileout = open(path[:len(path)-4]+"_decrypted.txt", "w+")

# input kunci banyak pergeseran huruf
hop = int(input("Masukkan lompatan abjad : "))
bowl = []

for word in filein:
  dectext = dekripsi(word)
  fileout.write(dectext+"\n")

print("Output sudah disimpan di", fileout.name)

filein.close()
fileout.close()