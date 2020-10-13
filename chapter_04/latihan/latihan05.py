jmlL = int(input("Jumlah Mahasiswa laki-laki = "))
jmlP = int(input("Jumlah Mahasiswa perempuan = "))

dgL = jmlL//10
dgP = jmlP//10

print()
print('========== Diagram Jenis Kelamin Mahasiswa PTIK 2020 ==========')
print()
print('Laki-Laki    : ', end='')
print('[]' * dgL, '(', jmlL ,')')
print('Perempuan    : ', end='')
print('[]' * dgP, '(', jmlP ,')')