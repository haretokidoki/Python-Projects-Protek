bin = int(input("Masukkan nilai Bhs. Indonesia : "))
mat = int(input("Masukkan nilai Matematika     : "))
ipa = int(input("Masukkan nilai IPA            : "))

print("")

if (bin > 100) or (mat > 100) or (ipa > 100) :
  print("Error, nilai tidak boleh lebih dari 100")
if (bin < 0) or (mat < 0) or (ipa < 0) :
  print("Error, nilai tidak boleh kurang dari 0")
elif (bin < 60) or (mat < 70) or (ipa < 60) :
  print("Status Kelulusan              : TIDAK LULUS")
  print("Sebab : ")
  if(bin<60):
    print("   - Nilai Bhs. Indonesia kurang dari 60")
  if(mat<70):
    print("   - Nilai Matematika kurang dari 70")
  if(ipa<60):
    print("   - Nilai IPA kurang dari 60")
else: 
  print("Status Kelulusan              : LULUS")

