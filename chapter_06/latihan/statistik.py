def sum(*args):
  sums = 0
  for a in args:
    sums += a
  return sums

def average(*args):
  n = 0
  for a in args:
    n += 1
  avg = sum(*args)/n
  return avg

def maks(*args):
  max = args[0]
  for a in args:
    if (a>max):
      max = a
  return max

def min(*args):
  min = args[0]
  for a in args:
    if (a<min):
      min = a
  return min
  