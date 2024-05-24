import jpeg
import generate_test_data as gtd


#gtd.one_color(70, 130, 180, 700, 1000)
#gtd.random_color(700, 1000)

def main():
    print('Выбор изображения: 1 - цветное изображение, 2 - однотонное, 3 - случайный цвет.')
    print('type = ')
    img_type = int(input())
    if img_type == 1:
        file = 'color.png'
    elif img_type == 2:
        file = 'one_color.png'
    elif img_type == 3:
        file = 'random_color.png'
    else:
        print('error')
        return
    print('Качество: Q = ', end = '')
    q = int(input())
    if q < 0 or q > 100:
        print('error')
        return
    jpeg.encode_jpeg('png\\' + file, 2, 2, q)
    print('Результат сохранен в txt\\result.txt')
    print('Коэффициент сжатия: ', end = '')
    print(gtd.compression_ratio(file))
    print('Выполняется декодирование изображения..')
    jpeg.decode_jpeg('txt\\result.txt')



main()
















#a = np.random.randint(10, 20, (8,8))
#print(a)
#print()

#h, ht = dct.calculate_H()


#b = dct.fdct(h, a, ht)
#print(b)
#print()



#c = dct.idct(h, b, ht)
#print(c)
#print()


#with open('s.txt', 'r', encoding='utf-8') as f:
#    s = f.read()

#s1 = io.out_encoded_vectors(s)

#s2 = io.in_encoded_vectors('result.txt')
#print(s2)


#with open('s1.txt', 'w', encoding='utf-8') as f:
#    f.write(s1)

#s1 = s

#print(s == s1)




#c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#print(len(c))
#a = [1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#b = dc.rle_encode(a)
#print(b)

#a = [[3, 5], [0, 0], [15, 0], [2, 2], [12, 4], [1, 5], [0, 0], [0, 0]]
#d = [1, 2, 3]

#a1 = [[0, 0], [0, 1], [0, 1], [0, 2], [2, 4], [0, 0]]
#d1 = [1, 2]

#huff1 = dc.huffman_compress(a, d, 'y')
#huff2 = dc.huffman_compress(a1, d1, 'cb')

#huff = huff1 + huff2

#h, i = dc.huffman_decompress(huff, 'y')
#print(h)
#huff  = huff[i:]
#h1, i = dc.huffman_decompress(huff, 'cb')
#print(h1)

#m = dc.rle_decode(h)
#print(m)

#m1 = dc.rle_decode(h1)
#print(m1)



#a = np.asarray(
#    [[15, 16, 19, 11, 24, 18, 14, 20, 23, 18, 10, 11, 13, 12, 16, 14, 15],
#    [20, 13, 17, 18, 13, 17, 23, 18, 22, 19, 21, 16, 22, 18, 20, 23, 15],
#    [23, 17, 14, 22, 16, 24, 18, 23, 18, 15, 11, 16, 19, 20, 21, 15, 15],
#    [11, 16, 24, 22, 12, 14, 18, 12, 14, 20, 20, 12, 22, 19, 21, 13, 15],
#    [21, 12, 15, 16, 17, 11, 21, 24, 23, 22, 20, 16, 13, 11, 20, 19, 15],
#    [17, 11, 21, 18, 16, 12, 14, 14, 20, 16, 24, 11, 19, 24, 17, 18, 15],
#    [19, 16, 24, 23, 24, 14, 21, 21, 19, 20, 22, 13, 12, 21, 19, 13, 15],
#    [-10, 11, 10, 12, 24, 24, 22, 23, -19, 24, 16, 18, 17, 21, 24, 17, 15],
#    [18, 21, 18, 15, 22, 20, 15, 21, 14, 11, 18, 23, 19, 23, 10, 12, 15],
#    [12, 23, 21, 23, 16, 24, 23, 22, 15, 18, 16, 22, 12, 11, 14, 23, 15],
#    [14, 24, 20, 20, 22, 13, 22, 15, 12, 14, 21, 18, 21, 16, 13, 21, 15],
#    [14, 10, 10, 22, 15, 13, 13, 22, 13, 14, 11, 11, 22, 22, 16, 21, 15],
#    [11, 14, 15, 18, 23, 11, 24, 17, 15, 21, 24, 12, 13, 16, 10, 17, 15],
#    [10, 12, 24, 15, 22, 12, 13, 22, 21, 13, 20, 17, 14, 23, 15, 15, 15],
#    [15, 10, 24, 10, 17, 13, 15, 17, 18, 23, 18, 19, 13, 19, 14, 13, 15],
#    [11, 10, 14, 20, 20, 18, 18, 15, 10, 15, 19, 23, 11, 12, 15, 19, 15]])

#a1 = np.asarray(
#    [[15, 16, 19, 11, 24, 18, 14, 20, 23, 18, 10, 11, 13, 12, 16, 14, 0],
#    [20, 13, 17, 18, 13, 17, 23, 18, 22, 19, 21, 16, 22, 18, 20, 23, 0],
#    [23, 17, 14, 22, 16, 24, 18, 23, 18, 15, 11, 16, 19, 20, 21, 15, 0],
#    [11, 16, 24, 22, 12, 14, 18, 12, 14, 20, 20, 12, 22, 19, 21, 13, 0],
#    [21, 12, 15, 16, 17, 11, 21, 24, 23, 22, 20, 16, 13, 11, 20, 19, 0],
#    [17, 11, 21, 18, 16, 12, 14, 14, 20, 16, 24, 11, 19, 24, 17, 18, 0],
#    [19, 16, 24, 23, 24, 14, 21, 21, 19, 20, 22, 13, 12, 21, 19, 13, 0],
#    [-10, 11, 10, 12, 24, 24, 22, 23, -19, 24, 16, 18, 17, 21, 24, 17, 0],
#    [18, 21, 18, 15, 22, 20, 15, 21, 14, 11, 18, 23, 19, 23, 10, 12, 0],
#    [12, 23, 21, 23, 16, 24, 23, 22, 15, 18, 16, 22, 12, 11, 14, 23, 0],
#    [14, 24, 20, 20, 22, 13, 22, 15, 12, 14, 21, 18, 21, 16, 13, 21, 0],
#    [14, 10, 10, 22, 15, 13, 13, 22, 13, 14, 11, 11, 22, 22, 16, 21, 0],
#    [11, 14, 15, 18, 23, 11, 24, 17, 15, 21, 24, 12, 13, 16, 10, 17, 0],
#    [10, 12, 24, 15, 22, 12, 13, 22, 21, 13, 20, 17, 14, 23, 15, 15, 0],
#    [15, 10, 24, 10, 17, 13, 15, 17, 18, 23, 18, 19, 13, 19, 14, 13, 0],
#    [11, 10, 14, 20, 20, 18, 18, 15, 10, 15, 19, 23, 11, 12, 15, 19, 0]])



#jpeg.encode_jpeg('test.png', 2, 2, 50)
#f = open('bytes.txt', 'r', encoding='utf-8')
#a = f.read()
#f.close()
#print(len(a))
#jpeg.decode_jpeg('result.txt')




#print(a.shape[0])
#print(a.shape[1])

#c = at.resize_for_block8(a) 
#c1 = at.resize_for_block8(a1) 
##print(c)

#bac, bdc = jpeg.dct_and_quantization(c, 1)
#bac1, bdc1 = jpeg.dct_and_quantization(c1, 1)

#huff = dc.huffman_compress(bac, bdc, 'cb')
##print(huff)
#huff1 = dc.huffman_compress(bac1, bdc1, 'y')
##print(huff1)

#f = open('result.txt', 'w', encoding='utf-8')
#f.write(str(17) + ' ' + str(16)+ ' ' + str(2) + ' ' + str(2) + '\n')
#f.close()

#io.out_encoded_vectors(huff + huff1)

#data, rw, rh, bx, by = io.in_encoded_vectors('result.txt')
##print(data)

#dhuff, start = dc.huffman_decompress(data, 'cb')
#data = data[start:]
##print(data)
#dhuff1, start = dc.huffman_decompress(data, 'y')

#db = dc.rle_decode(dhuff)
#db1 = dc.rle_decode(dhuff1)

#db = at.fill_array(db, rw, rh)
#db1 = at.fill_array(db1, rw, rh)


#print(db.shape[0])
#print(db.shape[1])
#print(db1.shape[0])
#print(db1.shape[1])

#db = jpeg.inverse_dct_and_quantization(db, 'cb')
#db1 = jpeg.inverse_dct_and_quantization(db1, 'y')

#print(db[0:rh, 0:rw])
#print('\n\n')
#print(db1[0:rh, 0:rw])
##print(db, end = '\n\n')
##print(db1, end = '\n\n')


#db = np.ndarray.astype(db, dtype = np.int32)
#db1 = np.ndarray.astype(db1, dtype = np.int32)

#print(db[0:rh, 0:rw])
#print('\n\n')
#print(db1[0:rh, 0:rw])







#b = at.downsampling_closest_to_average(a, 2, 2)
#print(b)

#c = at.upsampling_average(b, 2, 2)
#print(c)


#a = [[15, 16, 19, 11, 24, 18, 14, 20, 23, 18, 10, 11, 13, 12, 16, 14],
#    [20, 13, 17, 18, 13, 17, 23, 18, 22, 19, 21, 16, 22, 18, 20, 23],
#    [23, 17, 14, 22, 16, 24, 18, 23, 18, 15, 11, 16, 19, 20, 21, 15],
#    [11, 16, 24, 22, 12, 14, 18, 12, 14, 20, 20, 12, 22, 19, 21, 13],
#    [21, 12, 15, 16, 17, 11, 21, 24, 23, 22, 20, 16, 13, 11, 20, 19],
#    [17, 11, 21, 18, 16, 12, 14, 14, 20, 16, 24, 11, 19, 24, 17, 18],
#    [19, 16, 24, 23, 24, 14, 21, 21, 19, 20, 22, 13, 12, 21, 19, 13],
#    [-10, 11, 10, 12, 24, 24, 22, 23, -19, 24, 16, 18, 17, 21, 24, 17],
#    [18, 21, 18, 15, 22, 20, 15, 21, 14, 11, 18, 23, 19, 23, 10, 12],
#    [12, 23, 21, 23, 16, 24, 23, 22, 15, 18, 16, 22, 12, 11, 14, 23],
#    [14, 24, 20, 20, 22, 13, 22, 15, 12, 14, 21, 18, 21, 16, 13, 21],
#    [14, 10, 10, 22, 15, 13, 13, 22, 13, 14, 11, 11, 22, 22, 16, 21],
#    [11, 14, 15, 18, 23, 11, 24, 17, 15, 21, 24, 12, 13, 16, 10, 17],
#    [10, 12, 24, 15, 22, 12, 13, 22, 21, 13, 20, 17, 14, 23, 15, 15],
#    [15, 10, 24, 10, 17, 13, 15, 17, 18, 23, 18, 19, 13, 19, 14, 13],
#    [11, 10, 14, 20, 20, 18, 18, 15, 10, 15, 19, 23, 11, 12, 15, 19]]


#def block_processing_encode(matrix):
#    print('###### ONE BLOCK ######')
#    vector = at.zigzag(matrix)
#    print(vector, end='\n\n')
#    dc_value = vector[0]
#    vector = dc.rle_encode(vector)
#    print(vector, end='\n\n')
#    return [vector, dc_value]   # list



#def test(array2d):
#    vector_ac = []
#    vector_dc = []
#    prev_dc = 0
#    N, M = array2d.shape[1], array2d.shape[0]
#    for j in range(0, M, 8):
#        for i in range(0, N, 8):
#            bpe = block_processing_encode(array2d[j : (j + 8), i : (i + 8)])
#            vector_ac += bpe[0]
#            cur_dc = bpe[1] - prev_dc
#            vector_dc.append(cur_dc)
#            prev_dc = bpe[1]
#    return [vector_ac, vector_dc]



#vac, vdc = test(a)
#print(vac, end='\n\n')
#print(vdc, end='\n\n')


#h = dc.huffman_compress(vac, vdc, 'y')
#dh = dc.huffman_decompress(h, 'y')
#print(dh, end='\n\n')


#drle = dc.rle_decode(dh, 64)
#print(drle, end='\n\n')

#rr = at.fill_array(drle, 16, 16)
#print(rr)


#print(np.equal(a, rr))


#a = jpeg.encode_jpeg('test2.png', 2, 2, 50)
#f = open('bytes.txt', 'r', encoding='utf-8')
#a = f.read()
#f.close()
#print(len(a))
#a1 = jpeg.decode_jpeg('result.txt')
#print(a == a1)
#print(len(a1))
#print(a == a1)

# (0,57) (0,45) (4,23) (1,-30) (0,-16) (0, 0)

#a = [[0, 57], [0, 45], [4, 23], [1, -30], [0, -16], [0,0]]
#b, c = dc.value_processing(a)
#print(b)
#print(c)



# (15, 1, 0) (7, 5, 27)
#a = [1, 1, 2, 0, 0, 0, 0, 8, 0, 9, 10, -11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, -27, 0, 0, 0]
#print(a)
#print()
#b = dc.rle_encode(a)
#print(b)
#print()
#c = dc.huffman_compress(b, 'y')
#print(c)
#print()
#d = dc.huffman_decompress(c, 'y')
#print(d)
#print()
#e = dc.rle_decode(d, 1, len(a))
#print(e)
#print()

#c = dc.calc_freq(b)
#print(c)
#print()
#d = dc.rle_decode(b, 1, len(a))
#print(d)
#print()
#e = dc.huffman_compress(b)
#compr_data, huff_codes = e[0], e[1]
#print(compr_data)
#print()
#print(huff_codes)
#print()


#a = np.random.randint(-128, 127, (16, 16))
#print(a)
#print()


#jpeg.dct_and_quantization(a, 1)


#jpeg.encode_jpeg('test.png', 2, 2, 8, 8)


#a = np.random.randint(40, 255, (8, 8))
#print(a)


#b = dct.fdct2(a)
#print()
#print(b)


#c = np.random.randint(-127, 128, (8, 8))
#print(a)


#d = dct.fdct2(c)
#print()
#print(d)


#c = qt.quantization_LQT(100)
#print()
#print(c)


#e = qt.quantization(b, c)
#print()
#print(e)


#f = qt.inverse_quantization(e, c)
#print()
#print(f)



#c = dct.idct2(b)
#print()
#print(c)




#img = cc.init_image('test2.png')
#y, cb, cr = cc.RGB_to_YCbCr(img)
#img['pixels'] = cc.merge_channels(y, cb, cr)
#cc.YCbCr_to_RGB(img)
#Image.fromarray((img['pixels']),mode="RGB").show()



#cc.show_one_channel(y, 0)
#cc.show_one_channel(cb, 1)
#cc.show_one_channel(cr, 2)


#Image.fromarray((img['pixels'][0]),mode="YCbCr").show()

##y, cb, cr = YCbCr.RGB_to_YCbCr_3channels(img1)

#YCbCr.RGB_to_YCbCr(img)
#Image.fromarray((img['pixels']),mode="YCbCr").show()
#YCbCr.image_from_array2d(img['pixels'], 'YCbCr')


#img = YCbCr.YCbCr_to_RGB(img)
#Image.fromarray((img['pixels']),mode="RGB").show()
#YCbCr.image_from_array2d(img['pixels'], 'RGB')


#a = np.array([[1, 2, 3, 11, 12], [5, 6, 7, 14, 15], [9, 10, 11, 16, 17], [12, 13, 14, 18, 19]])
#print(a)
#b = YCbCr.downsampling_KxKy(a, 3, 2)
#print()
#print(b)
#c = YCbCr.upsampling_KxKy(b, 3, 2)
#print()
#print(c)


#a = np.array([[1, 2, 3, 11, 12], [5, 6, 7, 14, 15], [9, 10, 11, 16, 17], [12, 13, 14, 18, 19]])
#print(a)
#b = YCbCr.downsampling_KxKy(a, 3, 2)
#print()
#print(b)
#c = YCbCr.upsampling_KxKy(b, 3, 2)
#print()
#print(c)


#d = YCbCr.resize_for_block(a, 1, 2)
#print()
#print(d)

#e = YCbCr.downsampling_average(a, 3, 3)
#print()
#print(e)

#f = YCbCr.upsampling_average(e, 2, 2)
#print()
#print(f)

#g = YCbCr.downsampling_closest_to_average(a, 3, 3)
#print()
#print(g)

#f = YCbCr.upsampling_average(g, 3, 3)
#print()
#print(f)

#a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#a = [[1, 2], [3, 4], [5, 6], [7, 8]]
#v = transform.zigzag(a)
#print(v)