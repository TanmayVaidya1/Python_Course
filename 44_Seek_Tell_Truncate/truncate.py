with open('C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\44_Seek_Tell_Truncate\\sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\44_Seek_Tell_Truncate\\sample.txt', 'r') as f:
  print(f.read())