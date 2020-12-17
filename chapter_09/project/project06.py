nilai = [{'nim':'A01', 'nama':'Agustina', 'mid':50, 'uas':80},
        {'nim':'A02', 'nama':'Budi', 'mid':40, 'uas':90},
        {'nim':'A03', 'nama':'Chicha', 'mid':100, 'uas':50},
        {'nim':'A04', 'nama':'Donna', 'mid':20, 'uas':100},
        {'nim':'A05', 'nama':'Fatimah', 'mid':70, 'uas':100}]

# function tampilkan isi dictionary
def tampil(nilai):
  # label tabel
  print("="*65,"\n","NIM".center(8," "),"NAMA".center(11," "),"N.MID".center(10," "),"N.UAS".center(10," "),"N.AKHIR".center(10," "),"STATUS".center(7," "),"\n"+"-"*65)

  # tampilkan isi dictionary
  for x in nilai:
    # rumus nilai akhir
    akhir = (x['mid']+2*x['uas'])/3
    # cek nilai akhir
    if(akhir<60):
      status = "TIDAK LULUS"
    else:
      status = "LULUS"
    # tampilkan output
    print(x['nim'].center(10," "),(x['nama'].upper()).ljust(10," "),str(x['mid']).center(10," "),str(x['uas']).center(10," "),str(akhir)[:5].center(10," "),status.center(10," "))

  #footer tabel
  print("-"*65)

#panggil function tampilkan nilai
tampil(nilai)



