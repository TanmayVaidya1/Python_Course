with open('C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\44_Seek_Tell_Truncate\\myfile.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)
  print(current_position)