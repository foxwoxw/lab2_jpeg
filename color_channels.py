from PIL import Image
import numpy as np



# rgb - три канала вместе, ycbcr - отдельно
def init_image(filename):
    img_info = {}
    with Image.open(filename) as img:
        img_info['name'] = filename
        img_info['height'], img_info['width'] = img.height, img.width
        img = img.convert('RGB')
        arr = np.array(img)
        arr = arr.astype(np.uint8)
        with open('txt' + filename[3:-4] + '_raw.txt', 'wb') as f:
            np.save(f, arr)     # raw
        img_info['pixels'] = arr
    return img_info



def RGB_to_YCbCr(img_info):
    pixels = img_info['pixels']    
    height, width = img_info['height'], img_info['width']
    Y = np.zeros((height, width), dtype = np.double)
    Cb = np.zeros((height, width), dtype = np.double)
    Cr = np.zeros((height, width), dtype = np.double)
    for h in range(height):
        for w in range(width):
            R, G, B = pixels[h, w][0], pixels[h, w][1], pixels[h, w][2]
            Y[h, w] = min(max(0, 0.299 * R + 0.587 * G + 0.114 * B), 255)
            Cb[h, w] = min(max(0, 128 - 0.168736 * R - 0.331264 * G + 0.5 * B), 255)
            Cr[h, w] = min(max(0, 128 + 0.5 * R - 0.418688 * G - 0.08312 * B), 255)
    img_info['pixels'] = [Y, Cb, Cr]




def YCbCr_to_RGB(img_info):
    pixels = img_info['pixels'] # трехмерный массив
    pixels = pixels.astype(np.double)
    height, width = img_info['height'], img_info['width']
    img_RGB = np.zeros((height, width, 3), dtype = np.double)
    for h in range(height):
        for w in range(width):
            Y, Cb, Cr = pixels[h, w][0], pixels[h, w][1], pixels[h, w][2]
            R = min(max(0, Y + 1.402 * (Cr - 128)), 255)
            G = min(max(0, Y - 0.344136 * (Cb - 128) - 0.714136 * (Cr - 128)), 255)
            B = min(max(0, Y + 1.772 * (Cb - 128)), 255)
            img_RGB[h, w] = [R, G, B]
    img_RGB = img_RGB.astype(np.uint8)
    img_info['pixels'] = img_RGB
    return img_RGB



