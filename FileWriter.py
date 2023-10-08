import png, numpy as np, canvas, struct


def WriteFile(filename: str, canvas: canvas.canvas):
    canv = canvas.GetCanvas()
    print(len(canv))
    print(len(canv[0]))
    
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 14 + 40 + (canvas.width * canvas.height * 3))  # File size
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 14 + 40)  # Data offset

    # DIB header (BITMAPINFOHEADER)
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', canvas.width)  # Image width
    dib_header += struct.pack('<I',canvas. height)  # Image height
    dib_header += b'\x01\x00'  # Color planes (1)
    dib_header += b'\x18\x00'  # Bits per pixel (24 bits)
    dib_header += b'\x00\x00\x00\x00'  # Compression (none)
    dib_header += struct.pack('<I', canvas.width * canvas.height * 3)  # Image size (uncompressed)
    dib_header += b'\x13\x0B\x00\x00'  # Horizontal resolution (2835 pixels/meter)
    dib_header += b'\x13\x0B\x00\x00'  # Vertical resolution (2835 pixels/meter)
    dib_header += b'\x00\x00\x00\x00'  # Number of colors in the palette (not used)
    dib_header += b'\x00\x00\x00\x00'  # Number of important colors (not used)
    image_data = b''
    
    for y in range(canvas.height):
        for x in range(canvas.width):
            for i in canv[x][y]:#
                image_data += i
                
    with open(filename, 'wb') as bmp_file:
        bmp_file.write(bmp_header)
        bmp_file.write(dib_header)
        bmp_file.write(image_data)
    image_data = ""
def GetTheSizeOfImageInBytes(canvas_ : canvas.canvas):
    x, y = canvas_.width , canvas_.width
    bit_depth = canvas_.bit_depth
    return int(x*y*(bit_depth/8))