import quantization as q
import color_channels as cc
import array_transform as at
import data_compression as dc
import dct
import in_out as io
import numpy as np
from PIL import Image



# qt - матрица квантования
# h, ht - матрицы dct
def block_processing_encode(matrix, qt, h, ht):
    matrix = dct.fdct(h, matrix, ht)    # float64
    matrix = q.quantization(matrix, qt) # int16
    vector = at.zigzag(matrix)          # int16
    dc_value = vector[0]
    vector = dc.rle_encode(vector)
    return [vector, dc_value]   



def dct_and_quantization(array2d, qt, h, ht):
    N, M = array2d.shape[1], array2d.shape[0]
    vector_ac, vector_dc = [], []
    prev_dc = 0
    for j in range(0, M, 8):
        for i in range(0, N, 8):
            bpe = block_processing_encode(array2d[j : (j + 8), i : (i + 8)], qt, h, ht)
            vector_ac += bpe[0]
            vector_dc.append(bpe[1] - prev_dc)
            prev_dc = bpe[1]
    return [vector_ac, vector_dc]
            



# размер картинки, таблица квантования, таблицы хаффмана, сами каналы
def encode_jpeg(filename, size_ds_x, size_ds_y, Q):
    img_info = cc.init_image(filename)

    f = open('txt\\result_size.txt', 'w', encoding='utf-8')
    f.write(str(img_info['width']) + ' ' + str(img_info['height'])+ ' ')

    cc.RGB_to_YCbCr(img_info)
    y, cb, cr = img_info['pixels'][0], img_info['pixels'][1], img_info['pixels'][2]

    cb = at.downsampling_closest_to_average(cb, size_ds_x, size_ds_y)
    cr = at.downsampling_closest_to_average(cr, size_ds_x, size_ds_y)

    f.write(str(size_ds_x) + ' ' + str(size_ds_y) + ' ' + '\n')
    f.close()

    # до размера блоков 8*8
    y = at.resize_for_block8(y) - 128
    cb = at.resize_for_block8(cb) - 128
    cr = at.resize_for_block8(cr) - 128


    # матрицы dct, матрицы квантования
    h, ht = dct.calculate_H()
    lqt = q.quantization_LQT(Q)
    cqt = q.quantization_CQT(Q)


    # дкп, квантование, rle
    y_ac, y_dc = dct_and_quantization(y, lqt, h, ht) 
    cb_ac, cb_dc = dct_and_quantization(cb, cqt, h, ht)
    cr_ac, cr_dc = dct_and_quantization(cr, cqt, h, ht)
    

    # строки с двоичным кодом
    y_encode = dc.huffman_compress(y_ac, y_dc, 'y') 
    cb_encode = dc.huffman_compress(cb_ac, cb_dc, 'cb')
    cr_encode = dc.huffman_compress(cr_ac, cr_dc, 'cr')

    io.out_encoded_vectors(y_encode + cb_encode + cr_encode)



def inverse_dct_and_quantization(array2d, qt, h, ht):
    N, M = array2d.shape[1], array2d.shape[0]
    for j in range(0, M, 8):
        for i in range(0, N, 8):
            end_j = j + 8
            end_i = i + 8
            array2d[j : end_j, i : end_i] *= qt
            array2d[j : end_j, i : end_i] = dct.idct(h, array2d[j : end_j, i : end_i], ht)
    array2d = array2d.astype(np.double)
    return array2d




def decode_jpeg(filename):
    data, rw, rh, bx, by = io.in_encoded_vectors(filename)

    y_huff, start_i = dc.huffman_decompress(data, 'y')
    data = data[start_i:]
    cb_huff, start_i = dc.huffman_decompress(data, 'cb')
    data = data[start_i:]
    cr_huff, start_i = dc.huffman_decompress(data, 'cr')

    y = dc.rle_decode(y_huff)
    cb = dc.rle_decode(cb_huff)
    cr = dc.rle_decode(cr_huff)    

    brw = np.ceil(rw / bx)
    brh = np.ceil(rh / by)

    # float64
    y = at.fill_array(y, rw, rh)
    cb = at.fill_array(cb, brw, brh)
    cr = at.fill_array(cr, brw, brh)

    # float64
    h, ht = dct.calculate_H()
    lqt = io.get_table('txt\\LQT.txt')
    cqt = io.get_table('txt\\CQT.txt')

    # float64
    y = inverse_dct_and_quantization(y, lqt, h, ht) + 128
    cb = inverse_dct_and_quantization(cb, cqt, h, ht) + 128 
    cr = inverse_dct_and_quantization(cr, cqt, h, ht) + 128

    cb = at.upsampling_average(cb, bx, by)
    cr = at.upsampling_average(cr, bx, by)

    ycbcr = np.stack((y[0:rh, 0:rw], cb[0:rh, 0:rw], cr[0:rh, 0:rw]), axis=2)

    rgb = cc.YCbCr_to_RGB({'pixels':ycbcr, 'width':rw, 'height':rh})

    Image.fromarray((rgb),mode="RGB").show()
    #Image.fromarray((rgb),mode="RGB").save('results\\random_color50.png')








