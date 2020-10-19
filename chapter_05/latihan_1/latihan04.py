kodeKry = input("Masukkan Kode Karyawan     : ")
namaKry = input("Masukkan Nama Karyawan     : ")
golKry  = input("Masukkan Golongan Karyawan : ")

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
  print("Golongan yang dimasukkan salah!")
  exit()

gajiBersih = gajiPokok - (gajiPokok * pot)

print("")
print("=============================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------------")
print(" ")
print("Nama Karyawan        : "+namaKry+" (Kode : "+kodeKry+")")
print("Golongan             : "+golKry)
print("")
print("---------------------------------------------")
print("")
print("Gaji Pokok           : Rp "+ str(gajiPokok))
print("Potongan (" + str(pot*100) + "%)      : Rp " + str(int(gajiPokok*pot)))
print("")
print("---------------------------------------------")
print("")
print("Gaji Bersih          : Rp "+ str(int(gajiBersih)))
print("")
print("=============================================")