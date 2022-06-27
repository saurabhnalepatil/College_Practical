# Imports PIL module
from PIL import Image

# open method used to open different extension image file
im = Image.open(r"D:\STUDY MATERIAL\Python programs\download.jpg")

im.split()

#rotate image according to angle given
img = im.rotate(180) 

img.paste(im, (50, 50))

# this method gives us pixel count
print(im.histogram())
img.save("D:\STUDY MATERIAL\Python programs\img1.jpg")

# This method will show image in any image viewer
img.show()
