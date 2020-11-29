#fungsi saya panggil / gunakan di project 1
def kuadrat(bil):
  global qdr
  qdr = []
  for n in range(len(bil)):
    c = bil[n]**2
    qdr.append(c)
  return qdr