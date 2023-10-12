import canvas , FileWriter, multiprocessing, os,time
from canvas import *
print(f"CPUS: {str(os.cpu_count())} ")
start = time.time()
'''
r = int(input("Red Amount: ")) | 12
g = int(input("Green Amount: ")) | 120
b = int(input("Blue Amount: ")) | 123
'''
penis = canvas(1920, 1920)
y = canvas(300, 300)
y.DrawCircleFill(50,50, 30, color_rgb(255, 224, 189))
y.WritePixel(33, 50, color_rgb(255, 0, 0))
y.WritePixel(67, 50, color_rgb(255, 0, 0))
y.DrawLine((33,37), (66,37), color_rgb(0,0,0))

y.DrawLine((25,45) ,(32,38), color_rgb(0,0,0))
y.DrawLine((67,38) ,(74,45), color_rgb(0,0,0))
y.DrawCircleFill(11,11, 10, color_rgb(255,0,0))
y.DrawCircleFill(32,11, 10, color_rgb(255,0,0))

y.DrawCircleFill(67,50, 5, color_rgb(0,0,0))
y.DrawCircleFill(33,50, 5, color_rgb(0,0,0))


y.DrawRect([70,70], [150,90], color_rgb(20,20,20), thickness=10)



#draws a penis

penis.DrawCircleFill(int(penis.width/2),int(penis.height/2), 100, color_rgb(0,0,0))
penis.DrawCircleFill(int(penis.width/2) + 200,int(penis.height/2), 100, color_rgb(0,0,0))
penis.DrawRectFill([int(penis.width/2) + 50, int(penis.height/2)], [int(penis.width/2) + 150,int(penis.height/2) + 400], color_rgb(0,0,0))
penis.draw_circle(int(penis.width/2),int(penis.height/2), 200, color_rgb(0,0,0), thickness=10)
FileWriter.WriteFile("image_test.bmp", y)
FileWriter.WriteFile("image_test_penis.bmp", penis)
print(f"END TIME {time.time() - start}")
