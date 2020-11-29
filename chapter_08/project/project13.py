nilaiMhs = [{'nim':'A01', 'nama':'Amir', 'mid':50, 'uas':80},
            {'nim':'A02', 'nama':'Budi', 'mid':40, 'uas':90},
            {'nim':'A03', 'nama':'Cici', 'mid':50, 'uas':50},
            {'nim':'A04', 'nama':'Dedi', 'mid':20, 'uas':30},
            {'nim':'A05', 'nama':'Fifi', 'mid':70, 'uas':40}]

def cariNilai(nilaiMhs):
  nilaiAkhir = None
  hasil = {}
  for n in nilaiMhs:
    nilai = (n['mid'] + (2 * n['uas'])) / 3
    if(nilaiAkhir is None) or (nilai > nilaiAkhir):
            nilaiAkhir = nilai
            hasil['nim']  = n['nim']
            hasil['nama'] = n['nama'] 
  return hasil

hasil = cariNilai(nilaiMhs)
print("Mahasiswa yang memiliki nilai tertinggi adalah",hasil['nama'],"dengan nim",hasil['nim'])