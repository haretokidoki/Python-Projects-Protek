try:
  file = open("txt_file/data.txt", "r")
  sum = 0
  for data in file:
    sum = sum + int(data)
  print(sum)

except ValueError:
  print("Data tidak boleh mengandung huruf (alphabet)") 