def starFormation1(n):
  i = 0
  while (i < n):
    j = 0
    while(j <= i ):
      print('* ', end='')
      j += 1
    print('')
    i += 1

def starFormation2(n):
  n -= 1
  i = 0
  while (i < n):
    j = n
    while(j != i ):
      print('* ', end='')
      j -= 1
    print('')
    i += 1

n = int(input("Masukkan banyak bintang : "))
print()
starFormation1(n)
starFormation2(n)