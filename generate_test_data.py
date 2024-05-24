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




















#import quantization as q
#import color_channels as cc
#import array_transform as at
#import data_compression as dc
#import dct
#import in_out as io



## qt - матрица квантования
## h, ht - матрицы dct
#def block_processing_encode(matrix, qt, h, ht):
#    matrix = dct.fdct(h, matrix, ht)    # float64
#    matrix = q.quantization(matrix, qt) # int16
#    vector = at.zigzag(matrix)          # int16
#    dc_value = vector[0]
#    vector = dc.rle_encode(vector)
#    return [vector, dc_value]   



#def dct_and_quantization(array2d, qt, h, ht):
#    N, M = array2d.shape[1], array2d.shape[0]
#    vector_ac, vector_dc = [], []
#    prev_dc = 0
#    for j in range(0, M, 8):
#        for i in range(0, N, 8):
#            bpe = block_processing_encode(array2d[j : (j + 8), i : (i + 8)], qt, h, ht)
#            vector_ac += bpe[0]
#            vector_dc.append(bpe[1] - prev_dc)
#            prev_dc = bpe[1]
#    return [vector_ac, vector_dc]
            


## размер картинки, таблица квантования, таблицы хаффмана, сами каналы
#def test(filename, size_ds_x, size_ds_y):
#    Q = 50

#    img_info = cc.init_image(filename)

#    f = open('txt\\result_size.txt', 'w', encoding='utf-8')
#    f.write(str(img_info['width']) + ' ' + str(img_info['height'])+ ' ')

#    cc.RGB_to_YCbCr(img_info)
#    y, cb, cr = img_info['pixels'][0], img_info['pixels'][1], img_info['pixels'][2]

#    h, w = img_info['height'], img_info['width']

#    #ycbcr = np.stack((y[0:h, 0:w], cb[0:h, 0:w], cr[0:h, 0:w]), axis=2)
#    #ycbcr = ycbcr.astype(np.uint8)
#    #with open('txt\\result.txt', 'wb') as f:
#    #    np.save(f, ycbcr)     
#    #print(compression_ratio(filename[3:]))

#    cb = at.downsampling_closest_to_average(cb, size_ds_x, size_ds_y)
#    cr = at.downsampling_closest_to_average(cr, size_ds_x, size_ds_y)
#    f.write(str(size_ds_x) + ' ' + str(size_ds_y) + ' ' + '\n')
#    f.close()

#    #cb = cb.astype(np.uint8)
#    #cr = cr.astype(np.uint8)
#    #f_size = os.path.getsize('txt\\' + filename[3:-4] + '_raw.txt')
#    #r_size = y.shape[0] * y.shape[1] + cb.shape[0] * cb.shape[1] + cr.shape[0] * cr.shape[1]
#    #print(round(f_size/r_size, 4))


#    # до размера блоков 8*8
#    y = at.resize_for_block8(y) #- 128.0
#    cb = at.resize_for_block8(cb) #- 128.0
#    cr = at.resize_for_block8(cr)# - 128.0


#    # матрицы dct, матрицы квантования
#    h, ht = dct.calculate_H()
#    lqt = q.quantization_LQT(Q)
#    cqt = q.quantization_CQT(Q)


#    # дкп, квантование, rle
#    y_ac, y_dc = dct_and_quantization(y, lqt, h, ht) 
#    cb_ac, cb_dc = dct_and_quantization(cb, cqt, h, ht)
#    cr_ac, cr_dc = dct_and_quantization(cr, cqt, h, ht)

#    f_size = os.path.getsize('txt\\' + filename[3:-4] + '_raw.txt')
#    r_size = 2*(len(y_ac) + len(cb_ac) + len(cr_ac)) + len(y_dc) + len(cb_dc) + len(cr_dc)
#    print(round(f_size/r_size, 4))
    

    ## строки с двоичным кодом
    #y_encode = dc.huffman_compress(y_ac, y_dc, 'y') 
    #cb_encode = dc.huffman_compress(cb_ac, cb_dc, 'cb')
    #cr_encode = dc.huffman_compress(cr_ac, cr_dc, 'cr')

    #io.out_encoded_vectors(y_encode + cb_encode + cr_encode)



