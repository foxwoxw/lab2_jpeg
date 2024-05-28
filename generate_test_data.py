from PIL import Image
import numpy as np
import os
import pygame
import random


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



def blocks(w, h, s):
    pygame.init()
    width, height = w, h
    surface = pygame.Surface((width, height))
    block_size = s
    blocks_x = width // block_size
    blocks_y = height // block_size
    unique_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(blocks_x * blocks_y)]
    color_index = 0
    for x in range(blocks_x):
        for y in range(blocks_y):
            color = unique_colors[color_index]
            pygame.draw.rect(surface, color, (x * block_size, y * block_size, block_size, block_size))
            color_index += 1
    pygame.image.save(surface, 'png\\blocks.png')
    pygame.quit()



def basic_color(s):
    h = s * 4
    r = np.ones((h, h), dtype = np.uint8)
    g = np.ones((h, h), dtype = np.uint8)
    b = np.ones((h, h), dtype = np.uint8)
    colors = [[0] * 3, [128] * 3, [192] * 3, [255] * 3,
              [255, 0, 255], [128, 0, 128], [255, 0, 0], [128, 0, 0],
              [255, 255, 0], [128, 128, 0], [0, 255, 0], [0, 128, 0],
              [0, 255, 255], [0, 128, 128], [0, 0, 255], [0, 0, 128]]
    k = 0
    for j in range(0, h, s):
        for i in range(0, h, s):
            r[j : (j + s), i : (i + s)] *= colors[k][0]
            g[j : (j + s), i : (i + s)] *= colors[k][1]
            b[j : (j + s), i : (i + s)] *= colors[k][2]
            k += 1
    rgb = np.stack((r, g, b), axis=2)
    Image.fromarray((rgb),mode="RGB").save("png\\basic_color.png")




def compression_ratio(filename):
    file_size = os.path.getsize('txt\\' + filename[:-4] + '_raw.txt')
    result = os.path.getsize('txt\\result.txt')
    return round(file_size/result, 4)
