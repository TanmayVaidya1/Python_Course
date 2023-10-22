import cv2
 
# Configurable Parameter
source = "C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\3_Image_Resizer\\i1.jpg"
destination = "C:\\Users\\tanma\\OneDrive\\Desktop\\Python Course\\79_Projects\\3_Image_Resizer\\newimage.png"
# Percent by which the image is resized
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)



# Calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# Dsize
dsize = (width, height)

# Resize image
output = cv2.resize(src, dsize)
cv2.imwrite(destination , output)
# cv2.waitKey(0)