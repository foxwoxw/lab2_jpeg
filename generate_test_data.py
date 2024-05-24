from PIL import Image
import numpy as np
import os


def one_color(rc, gc, bc, h, w):
    r = rc * np.ones((h, w), dtype = np.uint8)
    g = gc * np.ones((h, w), dtype = np.uint8)
    b = bc * np.ones((h, w), dtype = np.uint8)
    rgb = np.stack((r, g, b), axis=2)
    Image.fromarray((rgb),mode="RGB").save("png\\one_color.png")



def random_color(h, w):
    rgb = np.random.randint(0, 255, (h, w, 3))
    rgb = rgb.astype(np.uint8)
    Image.fromarray((rgb),mode="RGB").save("png\\random_color.png")



def compression_ratio(filename):
    file_size = os.path.getsize('txt\\' + filename[:-4] + '_raw.txt')
    result = os.path.getsize('txt\\result.txt')
    return round(file_size/result, 4)


