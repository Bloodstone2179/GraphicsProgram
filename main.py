import canvas , FileWriter
from canvas import *
r = int(input("Red Amount: ")) | 12
g = int(input("Green Amount: ")) | 120
b = int(input("Blue Amount: ")) | 123

y = canvas(100, 100)
y.WritePixel(1, 1, color_rgb(r, g, b))  # each byte = pixel color 255 colors   255 = red 
print(color_rgb(r, g, 2).code())
#y.WritePixel(100, 100,color_rgb(100, 0, 50).hexCode() )

size = FileWriter.GetTheSizeOfImageInBytes(y) + (y.height * 4) + 54
FileWriter.WriteFile("image_test.bmp", y)
