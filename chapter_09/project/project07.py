mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
      'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
      'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

# function tampilkan tabel
def tabel(mhs):
  # label tabel
  print("="*55)
  print("NIM".ljust(6," "),"NAMA MAHASISWA".ljust(20," "),"TGL LAHIR".ljust(11," "),"TEMPAT LAHIR".ljust(15," "),"\n"+"-"*55)
  # isi tabel (dari list)
  for x in range(len(mhs)):
    spl = mhs[x].split(":")
    tgla = spl[2].split("-")
    tgl = tgla[2]+"/"+tgla[1]+"/"+tgla[0]
    print(spl[0].ljust(6," "),spl[1].ljust(20," "),tgl.ljust(11," "),spl[3].ljust(15," "))
  # footer tabel
  print("-"*55)

#panggil function tampilkan tabel
tabel(mhs)