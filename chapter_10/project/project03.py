try:
  file = open('txt_file/mahasiswa.txt','r')
  dataMhs = {}
  n = 1

  for x in file:
    part = x.split('|')
    dataMhs[n] = {}
    dataMhs[n]['nim'] = part[0]
    dataMhs[n]['nama'] = part[1]
    dataMhs[n]['alamat'] = str.rstrip(part[2])
    n+=1
  print(dataMhs)

except FileNotFoundError:
  print("File tidak ditemukan")