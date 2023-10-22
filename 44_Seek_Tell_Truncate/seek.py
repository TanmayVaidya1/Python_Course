with open('C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\44_Seek_Tell_Truncate\\myfile.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)