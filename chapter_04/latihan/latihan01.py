tarifAwal = 200000 #12 jam pertama
tarifLanjut = 10000
jamMulai = 6
jamSelesai = 23
menitSelesai = 50

waktu = (jamSelesai - jamMulai) + menitSelesai // 60

tarif = tarifAwal + (waktu - 12) * 10000

print('Rp', tarif)