jamMulai = 6
jarak1 = 125
jarak2 = 256
kecepatan1 = 62
kecepatan2 = 70

waktu1 = jarak1/kecepatan1
waktu2 = jarak2/kecepatan2
istirahat = 45/60

waktuTotal = waktu1+istirahat+waktu2

jamSampai = jamMulai + int(waktuTotal)

print('Pukul '+str(jamSampai)+'.00')