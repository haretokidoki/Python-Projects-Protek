kolom = 5
baris = 5

i = 0
while (i < baris):
  j = kolom
  while(j != i ):
    print('* ', end='')
    j -= 1
  print('')
  i += 1