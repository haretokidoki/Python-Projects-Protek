kodeKry = input("Masukkan Kode Karyawan               : ")
namaKry = input("Masukkan Nama Karyawan               : ")

#golongan karyawan
golKry  = input("Masukkan Golongan Karyawan           : ")

if(golKry == "A") :
  gajiPokok = int(10000000)
  pot = float(0.025)
elif(golKry == "B") :
  gajiPokok = int(8500000)
  pot = float(0.02)
elif(golKry == "C") :
  gajiPokok = int(7000000)
  pot = float(0.015)
elif(golKry == "D") :
  gajiPokok = int(5500000)
  pot = float(0.01)
else :
  print("")
  print("Data yang anda masukkan salah!")
  exit()

#tunjangan nikah dan anak
staKry  = input("Masukkan Status (1:menikah, 2:belum) : ")

if(staKry == "1"):
  status = "Sudah Menikah"
  tunNikah = 0.1
  anak = input("Masukkan jumlah anak : ")
  tunAnak = 0.05 * int(anak)
elif(staKry == "2"):
  status = "Belum Menikah"
  tunNikah = 0
  anak = "0"
  tunAnak = 0
else:
  print("")
  print("Data yang anda masukkan salah!")
  exit()

gajiKotor = gajiPokok + (gajiPokok*tunNikah) + (gajiPokok*tunAnak)
gajiBersih = gajiKotor - (gajiPokok * pot)

print("")
print("=============================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------------")
print(" ")
print("Nama Karyawan        : "+namaKry+" (Kode : "+kodeKry+")")
print("Golongan             : "+golKry)
print("Status Menikah       : "+status)
print("Jumlah Anak          : "+anak)
print("")
print("---------------------------------------------")
print("")
print("Gaji Pokok           : Rp "+ str(gajiPokok))
print("Tunjangan Istri/Suami: Rp "+ str(int(gajiPokok*tunNikah)))
print("Tunjangan Anak       : Rp "+ str(int(gajiPokok*tunAnak)))
print("")
print("---------------------------------------------")
print("---------------------------------------------")
print("")
print("Gaji Kotor           : Rp "+ str(int(gajiKotor)))
print("Potongan (" + str(pot*100) + "%)      : Rp " + str(int(gajiKotor*pot)))
print("")
print("---------------------------------------------")
print("")
print("Gaji Bersih          : Rp "+ str(int(gajiBersih)))
print("")
print("=============================================")