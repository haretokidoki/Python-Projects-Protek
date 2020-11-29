#langkah 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

print("="*45)
print()
print("Data awal : ")
print("a = ", a)
print("b = ", b)
print()
print("="*45)

#langkah 2 (insert)
a.insert(3,10)
b.insert(2,15)

print()
print("Menyisipkan nilai 10 dalam indeks ke 3 a :")
print("a = ", a)
print("Menyisipkan nilai 15 dalam indeks ke 2 b : ")
print("b = ", b)
print()
print("="*45)

#langkah 3 (append)
a.append(4)
b.append(8)

print()
print("Menyisipkan nilai 4 ke indeks terakhir a : ")
print("a = ", a)w
print("Menyisipkan nilai 8 ke indeks terakhir b : ")
print("b = ", b)
print()
print("="*45)

#langkah 4 (sort)
a.sort()
b.sort()

print()
print("Hasil sorting list a secara ascending : ")
print("a = ", a)
print("Hasil sorting list b secara ascending : ")
print("b = ", b)
print()
print("="*45)

#langkah 5
c = a[:8]
d = b[2:10]

print()
print("List c (sublist dari list a indeks 0-7) :")
print("c = ", c)
print("List d (sublist dari list b indeks 2-9)")
print("d = ", d)
print()
print("="*45)

#langkah 6
e = []
nc = len(c)
for n in range(nc):
  e += [c[n] + d[n]]

print()
print("List e (penjumlahan setiap elemen c dan d) :")
print("e = ", e)

#langkah 7
e = (tuple(e))

print()
print("Mengubah list e ke tuple : ")
print("e = ", e)
print()
print("="*45)

#langkah 8
print()
print("Nilai minimum dari list e           : ", min(e))
print("Nilai maximum dari list e           : ", max(e))
print("Hasil penjumlahan seluruh elemen e  : ", sum(e))
print()
print("="*45)

#langkah 9
myString = "python adalah bahasa pemrograman yang menyenangkan"

#langkah 10
print()
print("Huruf yang digunakan dalam kalimat “", myString,"” :")
print(set(myString))
print()

#langkah 11
listMyString = list(set(myString))
print("List dari huruf diatas : \n", listMyString)

listMyString.sort()

print()
print("List dari huruf diatas jika diurutkan : \n", listMyString)