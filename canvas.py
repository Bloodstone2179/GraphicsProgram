import numpy as np, struct, math
from binascii import *
def hexify(hexString : int, prefix : bool):
        if prefix == True:
            return "0x{:02x}".format(hexString)
        if prefix == False:
            return "0x{:02x}".format(hexString).removeprefix("0x")
class color_rgba:
    red = 0
    green = 0
    blue = 0
    alpha = 255
    code = None
    def __init__(self, r,g,b,a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a
    
class color_rgb:
    red = 0
    green = 0
    blue = 0
    
    redCode = ""
    greenCode = ""
    blueCode = ""
    def __init__(self, r,g,b) -> None:
        self.red = r
        self.green = g
        self.blue = b
    def code(self):
        return "#" + hexify(self.red, False) + hexify(self.green, False) + hexify(self.blue, False)
    
        

class canvas:
    width = 100
    height = 100
    bit_depth = 24
    CanvasScreen = None
    
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.CanvasScreen =  np.array([[[bytes.fromhex(hexify(255, False)),bytes.fromhex(hexify(255, False)), bytes.fromhex(hexify(255, False))]] * height] * width, dtype=object)
        

    def WritePixel(self, pixel_x, pixel_y, data : color_rgba or color_rgb):
        bluehex = bytes.fromhex(hexify(data.blue, False))
        redHex = bytes.fromhex(hexify(data.red, False))
        greenHex = bytes.fromhex(hexify(data.green, False))
        print(f"Pixel X: {pixel_x} , PIXEL Y: {pixel_y}")
        if pixel_x - 1 > self.width or pixel_y - 1 > self.height:
            print("Not In Bounds")
        else:
            self.CanvasScreen[int(pixel_x - 1)][int(pixel_y - 1) ] = [bluehex, greenHex, redHex]
    def DrawLine(self,pointA: tuple, pointb: tuple, LineColor: color_rgb or color_rgba):
        if pointA[1] == pointb[1]:
            for x in range(pointA[0], pointb[0] + 1):
                
                self.WritePixel(x,pointA[1], LineColor)
        if pointA[0] == pointb[0]:
            for y in range(pointA[1], pointb[1] + 1):
                self.WritePixel(pointA[1],y, LineColor)
        else:
            dx = pointb[0] - pointA[0];
            dy = pointb[1] - pointA[1];
            for x in range(pointA[0], pointb[0] + 1):
                y = dy * (x - pointA[0])/dx + pointA[1];
                self.WritePixel(x,y, LineColor)
        '''if pointA[0] < pointb[0]:
            for x in range(pointA[0], pointb[0] + 1):
                if pointA[1] < pointb[1]:
                    for y in range(pointA[1], pointb[1] + 1):
                        self.WritePixel(x,y, LineColor)
                if pointA[1] > pointb[1]:
                    for y in range(pointb[1], pointA[1] + 1):
                        self.WritePixel(x,y, LineColor)
        if pointA[0] > pointb[0]:
            for x in range(pointb[0], pointA[0] + 1):
                if pointA[1] < pointb[1]:
                    for y in range(pointA[1], pointb[1] + 1):
                        self.WritePixel(x,y, LineColor)
                if pointA[1] > pointb[1]:
                    for y in range(pointb[1], pointA[1] + 1):
                        self.WritePixel(x,y, LineColor)
        else:
            for x in range(pointA[0], pointb[0] + 1):
                for y in range(pointA[1], pointb[1] + 1):
                    self.WritePixel(x,y, LineColor)'''
    def draw_circle(self, center_x, center_y, radius, color: color_rgb or color_rgba):
        x = radius
        y = 0
        error = 1 - x

        while x >= y:
            self.WritePixel(center_y + y, center_x + x, color)
            self.WritePixel(center_y + x, center_x + y, color)
            self.WritePixel(center_y + x, center_x - y, color)
            self.WritePixel(center_y + y, center_x - x, color)

            self.WritePixel(center_y - y, center_x - x , color)
            self.WritePixel(center_y - x, center_x - y , color)
            self.WritePixel(center_y - x, center_x + y , color)
            self.WritePixel(center_y - y, center_x + x , color)
           

            y += 1
            if error < 0:
                error += 2 * y + 1
            else:
                x -= 1
                error += 2 * (y - x) + 1
            '''
                for(float angle = 0.0f; angle < g_k2Pi; angle += 0.1f)
                    glVertex2f(sinf(angle)*_rRadius,  cosf(angle)*_rRadius);
            '''
    def DrawCircleFill(self, center_x, center_y, radius, color: color_rgb or color_rgba):
        x = radius
        y = 0
        error = 1 - x

        while x >= y:
            self.WritePixel(center_y + y, center_x + x, color)
            self.WritePixel(center_y + x, center_x + y, color)
            self.WritePixel(center_y + x, center_x - y, color)
            self.WritePixel(center_y + y, center_x - x, color)

            self.WritePixel(center_y - y, center_x - x , color)
            self.WritePixel(center_y - x, center_x - y , color)
            self.WritePixel(center_y - x, center_x + y , color)
            self.WritePixel(center_y - y, center_x + x , color)
           

            y += 1
            if error < 0:
                error += 2 * y + 1
            else:
                x -= 1
                error += 2 * (y - x) + 1
    def GetCanvas(self, asStr = False):
        if asStr !=  True:
            return self.CanvasScreen
        else:
            return np.array2string(self.CanvasScreen)
    



'''

    bmp 1st data = 42 4D 76 01 00 00 00 00 00 36 00 00 00 00 28 00 00 00 0A 00 00 00 0A 00 00 00 01 00 18  00 00 00 00 00 40 01 00 00 12 0B 00 00 12 0B 00 00  00 00 00 00 00 00 00 00

'''