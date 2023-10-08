import numpy as np, struct
from binascii import *
def hexify(hexString : str, prefix : bool):
        if prefix == True:
            return hex(255)
        if prefix == False:
            print(hexString)
            return hex(hexString).removeprefix("0x")
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
    CanvasScreen = np.array([[[bytes.fromhex(hexify(255, False)),bytes.fromhex(hexify(255, False)), bytes.fromhex(hexify(255, False))]] * height] * width, dtype=object)
    
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        

    def WritePixel(self, pixel_x, pixel_y, data : color_rgba or color_rgb):
        print(pixel_x)
        print(pixel_y)

        self.CanvasScreen[pixel_x - 1][pixel_y - 1 ] = [bytes.fromhex(hexify(data.blue, False)),bytes.fromhex(hexify(data.green, False)), bytes.fromhex(hexify(data.red, False))]
        print(self.CanvasScreen[pixel_x - 1][pixel_y - 1 ])
    def GetCanvas(self, asStr = False):
        if asStr !=  True:
            return self.CanvasScreen
        else:
            return np.array2string(self.CanvasScreen)
    



'''

    bmp 1st data = 42 4D 76 01 00 00 00 00 00 36 00 00 00 00 28 00 00 00 0A 00 00 00 0A 00 00 00 01 00 18  00 00 00 00 00 40 01 00 00 12 0B 00 00 12 0B 00 00  00 00 00 00 00 00 00 00

'''