nilai = [{'nim':'A01', 'nama':'Agustina', 'mid':50, 'uas':80},
        {'nim':'A02', 'nama':'Budi', 'mid':40, 'uas':90},
        {'nim':'A03', 'nama':'Chicha', 'mid':100, 'uas':50},
        {'nim':'A04', 'nama':'Donna', 'mid':20, 'uas':100},
        {'nim':'A05', 'nama':'Fatimah', 'mid':70, 'uas':100}]

# function tampilkan isi dictionary
def tampil(nilai):
  # label tabel
  print("="*45,"\n","NIM".center(8," "),"NAMA".center(11," "),"N.MID".center(10," "),"N.UAS".center(10," "),"\n"+"-"*45)

  # isi tabel (dari dictionary nilai)
  for x in nilai:
    print(x['nim'].center(10," "),(x['nama'].upper()).center(10," "),str(x['mid']).center(10," "),str(x['uas']).center(10," "))

  #footer tabel
  print("-"*45)

#panggil function tampilkan isi dictionary
tampil(nilai)