import os

# Open the file in write-only mode
f = os.open("C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\40_Os_Module\\text.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)