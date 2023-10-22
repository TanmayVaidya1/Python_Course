import os

# Open the file in read-only mode
f = os.open("C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\40_Os_Module\\poem.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 50)

print(contents)

# Close the file
os.close(f)