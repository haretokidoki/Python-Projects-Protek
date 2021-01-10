from datetime import *

def diffDate(x):
  tglx = datetime.strptime(x, '%Y-%m-%d').date()
  today = datetime.date(datetime.now())
  selisih = tglx - today
  return selisih.days

print(diffDate('2021-01-31'))