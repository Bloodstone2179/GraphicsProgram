import numpy as np, canvas, struct, time, multiprocessing
import threading, queue
multiprocessing.freeze_support()

queue_m = queue.Queue()

def process_row(row, rowID):
    
    # Convert each element in the row (y-axis data) to a binary string
    for x in row:
        string = b""
        for y in x:
            # Convert each element to a binary string
            string += y[0] + y[1] + y[2]
        queue_m.put(string)

def GetCanvasData(bmp_file, canv : np.ndarray):
    chunks = np.array_split(canv, len(canv), axis=0)
    imageData = b""
    # Create and start threads
    threads = []
    arrayIndex = 0
    for chunk in chunks:
        thread = threading.Thread(target=process_row, args=(chunk, arrayIndex))
        arrayIndex += 1
        thread.start()
        threads.append(thread)
        #print(threading.active_count())
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    open("test.txt", "wb").write(queue_m.get())
    imageData = queue_m.get()
    bmp_file.write(imageData)


def WriteFile(filename: str, canvas: canvas.canvas):
    print("Writing")
    canv = canvas.GetCanvas()
    bmp_header = b'BM'  # Signature
    bmp_header += struct.pack('<I', 14 + 40 + (canvas.width * canvas.height * 3))  # File size
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += b'\x00\x00'  # Reserved
    bmp_header += struct.pack('<I', 14 + 40)  # Data offset

    # DIB header (BITMAPINFOHEADER)
    dib_header = struct.pack('<I', 40)  # DIB header size
    dib_header += struct.pack('<I', canvas.width)  # Image width
    dib_header += struct.pack('<I',canvas. height)  # Image height
    dib_header += b'\x01\x00\x18\x00\x00\x00\x00\x00'  # Color planes (1)
    dib_header += struct.pack('<I', canvas.width * canvas.height * 3)  # Image size (uncompressed)
    dib_header += b'\x13\x0B\x00\x00\x13\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    start_time = time.time()
    
                
    with open(filename, 'wb') as bmp_file:
        bmp_file.write(bmp_header)
        bmp_file.write(dib_header)
        y = GetCanvasData(bmp_file, canv)
    print(f"Time Taken {time.time() - start_time} seconds")
    print("Written")
def GetTheSizeOfImageInBytes(canvas_ : canvas.canvas):
    x, y = canvas_.width , canvas_.width
    bit_depth = canvas_.bit_depth
    return int(x*y*(bit_depth/8))
