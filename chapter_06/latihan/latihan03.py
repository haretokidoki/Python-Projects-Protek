def faktorial(n):
  global i 
  i = n
  while (n > 1):
    n -= 1
    i *= n
  return i

def kombinasi(n, r):
  #n! / r!(n-r)!
  c = faktorial(n) / (faktorial(n - r) + faktorial(r))
  print(c)

def permutasi(n, r):
  #n! / (n-r)!
  p = faktorial(n) / faktorial(n-r)
  print(p)

kombinasi(5,3)
permutasi(10,7)
