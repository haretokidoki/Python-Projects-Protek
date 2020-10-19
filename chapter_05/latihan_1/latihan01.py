bin = int(input("Masukkan nilai Bhs. Indonesia : "))
mat = int(input("Masukkan nilai Matematika     : "))
ipa = int(input("Masukkan nilai IPA            : "))

print("")

if (bin < 60) or (mat < 70) or (ipa < 60) :
  print("Status Kelulusan              : TIDAK LULUS")
else: 
  print("Status Kelulusan              : LULUS")