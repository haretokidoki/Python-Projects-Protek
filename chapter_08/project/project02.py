#fungsi saya penggil / gunakan di project 1
def dataStat(x):
  a = sum(x)/len(x)
  b = max(x)
  c = min(x)
  data = [a,b,c]
  return data