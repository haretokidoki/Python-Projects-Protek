# function mencari ganjil/genap
def ganjilgenap():
  try:
    # membuka file
    file = open("txt_file/randomnumbers.txt","r")
    ganjil = 0
    genap = 0
    
    # cek ganjil/genap
    for line in file:
      bil = int(line)
      chk = bil%2
      if(chk == 0):
        genap += 1
      elif(chk == 1):
        ganjil += 1
    
    # tampilkan output
    print('File                   : ',file.name)
    print("Jumlah bilangan ganjil : ",ganjil)
    print("Jumlah bilangan genap  : ",genap)

  except FileNotFoundError:
    print("File tidak ditemukan")

# panggil function ganjil/genap
ganjilgenap()