import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"C://Users//tanma//OneDrive//Desktop//Python Course//40_Os_Module//data//Day{i+1}")