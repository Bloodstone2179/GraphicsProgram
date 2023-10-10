import canvas , FileWriter, multiprocessing, os
from canvas import *
print(f"CPUS: {str(os.cpu_count())} ")
'''
r = int(input("Red Amount: ")) | 12
g = int(input("Green Amount: ")) | 120
b = int(input("Blue Amount: ")) | 123
'''
y = canvas(300, 300)

y.DrawCircleFill(50,50, 30, color_rgb(255, 224, 189))
y.WritePixel(33, 50, color_rgb(255, 0, 0))
y.WritePixel(67, 50, color_rgb(255, 0, 0))
y.DrawLine((33,37), (66,37), color_rgb(0,0,0))

y.DrawLine((25,45) ,(32,38), color_rgb(0,0,0))
y.DrawLine((67,38) ,(74,45), color_rgb(0,0,0))
y.draw_circle(11,11, 10, color_rgb(255,0,0))
y.draw_circle(11,32, 10, color_rgb(255,0,0))

y.DrawCircleFill(67,50, 5, color_rgb(0,0,0))
y.DrawCircleFill(33,50, 5, color_rgb(0,0,0))
'''
y.WritePixel(25, 45, color_rgb(0, 0, 0))
y.WritePixel(26, 44, color_rgb(0, 0, 0))
y.WritePixel(27, 43, color_rgb(0, 0, 0))
y.WritePixel(28, 42, color_rgb(0, 0, 0))
y.WritePixel(29, 41, color_rgb(0, 0, 0))
y.WritePixel(30, 40, color_rgb(0, 0, 0))
y.WritePixel(31, 39, color_rgb(0, 0, 0))
y.WritePixel(32, 38, color_rgb(0, 0, 0))

y.WritePixel(33, 37, color_rgb(0, 0, 0))
y.WritePixel(34, 37, color_rgb(0, 0, 0))
y.WritePixel(35, 37, color_rgb(0, 0, 0))
y.WritePixel(36, 37, color_rgb(0, 0, 0))
y.WritePixel(37, 37, color_rgb(0, 0, 0))
y.WritePixel(38, 37, color_rgb(0, 0, 0))
y.WritePixel(39, 37, color_rgb(0, 0, 0))
y.WritePixel(40, 37, color_rgb(0, 0, 0))
y.WritePixel(41, 37, color_rgb(0, 0, 0))
y.WritePixel(42, 37, color_rgb(0, 0, 0))
y.WritePixel(43, 37, color_rgb(0, 0, 0))
y.WritePixel(44, 37, color_rgb(0, 0, 0))
y.WritePixel(45, 37, color_rgb(0, 0, 0))
y.WritePixel(46, 37, color_rgb(0, 0, 0))
y.WritePixel(47, 37, color_rgb(0, 0, 0))
y.WritePixel(48, 37, color_rgb(0, 0, 0))
y.WritePixel(49, 37, color_rgb(0, 0, 0))
y.WritePixel(50, 37, color_rgb(0, 0, 0))
y.WritePixel(51, 37, color_rgb(0, 0, 0))
y.WritePixel(52, 37, color_rgb(0, 0, 0))
y.WritePixel(53, 37, color_rgb(0, 0, 0))
y.WritePixel(54, 37, color_rgb(0, 0, 0))
y.WritePixel(55, 37, color_rgb(0, 0, 0))
y.WritePixel(56, 37, color_rgb(0, 0, 0))
y.WritePixel(57, 37, color_rgb(0, 0, 0))
y.WritePixel(58, 37, color_rgb(0, 0, 0))
y.WritePixel(59, 37, color_rgb(0, 0, 0))
y.WritePixel(60, 37, color_rgb(0, 0, 0))
y.WritePixel(61, 37, color_rgb(0, 0, 0))
y.WritePixel(62, 37, color_rgb(0, 0, 0))
y.WritePixel(63, 37, color_rgb(0, 0, 0))
y.WritePixel(64, 37, color_rgb(0, 0, 0))
y.WritePixel(65, 37, color_rgb(0, 0, 0))
y.WritePixel(66, 37, color_rgb(0, 0, 0))

y.WritePixel(74, 45, color_rgb(0, 0, 0))
y.WritePixel(73, 44, color_rgb(0, 0, 0))
y.WritePixel(72, 43, color_rgb(0, 0, 0))
y.WritePixel(71, 42, color_rgb(0, 0, 0))
y.WritePixel(70, 41, color_rgb(0, 0, 0))
y.WritePixel(69, 40, color_rgb(0, 0, 0))
y.WritePixel(68, 39, color_rgb(0, 0, 0))
y.WritePixel(67, 38, color_rgb(0, 0, 0))
#y.WritePixel(100, 100,color_rgb(100, 0, 50).hexCode() )
'''
size = FileWriter.GetTheSizeOfImageInBytes(y) + (y.height * 4) + 54
FileWriter.WriteFile("image_test.bmp", y)
