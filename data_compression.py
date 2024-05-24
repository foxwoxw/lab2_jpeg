import in_out as io
import heapq


#  57 45 0 0 0 0 23 0 -30 -16 0 ... 0
# (0,57) (0,45) (4,23) (1,-30) (0,-16) (EOB)
def rle_encode(vector):      
    N = len(vector)
    start_of_seq0 = N + 1
    for i in range(-1, -N - 1, -1):
        start_of_seq0 -= 1
        if vector[i] != 0:
            break
  
    count0 = 0
    encode_data = []
    i = 1
    while i < start_of_seq0:
        if vector[i] == 0:
            count0 += 1
            if count0 == 15:
                i += 1
                encode_data.append([count0, vector[i]]) 
                count0 = 0
        else:
            encode_data.append([count0, vector[i]])
            count0 = 0
        i += 1
    if count0 != 0:
        encode_data.append([count0, vector[i]])
    encode_data.append([0,0])  # eob
    return encode_data




# vector = (0,57) (0,45) (4,23) (1,-30) (0,-16) (EOB)
def calc_freq_ac(vector):
    symb_freq = {}
    N = len(vector)
    for i in range(N):
        key = chr(vector[i][0] << 4 | int(vector[i][1]).bit_length())
        if key in symb_freq:
            symb_freq[key] += 1
        else:
            symb_freq[key] = 1
    return symb_freq




# коды по длине двоичной записи
def calc_freq_dc(vector):
    symb_freq = {}
    N = len(vector)
    for i in range(N):
        key = chr(int(vector[i]).bit_length())
        if key in symb_freq:
            symb_freq[key] += 1
        else:
            symb_freq[key] = 1
    return symb_freq




def build_huffman_tree(symb_freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in symb_freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]



def create_huffman_codes(symb_freq):
    heap = build_huffman_tree(symb_freq)
    huff_codes = {}
    for pair in heap[1:]:
        symbol, code = pair
        huff_codes[symbol] = code
    return huff_codes



# (количество нулей, категория, переменный код)
# 57 = 0b111001, 45 = 0b101101, 23 = 0b10111, 30 = 0b11110, 16 = 0b10000
# (0,57) (0,45) (4,23) (1,-30) (0,-16) (0, 0) ->
# -> (0,6,011001) (0,6,001101) (4,5,00111) (1,5,11110) (0,5,10000) (EOB)


def huffman_compress(vector_ac, vector_dc, channel):
    vector_ac.append([1, 0]) # eob for huffman
    vector_dc.append(0)

    symb_freq_ac = calc_freq_ac(vector_ac)
    symb_freq_dc = calc_freq_dc(vector_dc)

    huff_codes_ac = create_huffman_codes(symb_freq_ac)
    huff_codes_dc = create_huffman_codes(symb_freq_dc)
    io.save_table(huff_codes_ac, 'txt\\huff_codes_' + channel + '_ac.txt')
    io.save_table(huff_codes_dc, 'txt\\huff_codes_' + channel + '_dc.txt')

    encode_data = ""
    N = len(vector_ac)
    i = 0
    j = 1

    if vector_dc[0] <= 0:
        value_dc = bin(vector_dc[0])[3:]
    else:
        value_dc = '0' + bin(vector_dc[0])[3:]
    length = len(value_dc)
    encode_data += huff_codes_dc[chr(length)]
    encode_data += value_dc

    while i < N:
        if vector_ac[i][1] <= 0:
            value_ac = bin(vector_ac[i][1])[3:]
        else:
            value_ac = '0' + bin(vector_ac[i][1])[3:]
        length = len(value_ac)
        encode_data += huff_codes_ac[chr(vector_ac[i][0] << 4 | length)]
        encode_data += value_ac

        if vector_ac[i] == [0, 0]:
            if vector_dc[j] <= 0:
                value_dc = bin(vector_dc[j])[3:]
            else:
                value_dc = '0' + bin(vector_dc[j])[3:]
            length = len(value_dc)
            encode_data += huff_codes_dc[chr(length)]
            encode_data += value_dc
            j += 1

        i += 1
    return encode_data




# channel - для файла с нужной таблицей кодов
# decoded_data = [(0,57) (0,45) (4,23) (1,-30) (0,-16) (EOB)]
def huffman_decompress(compressed_data, channel):
    huff_codes_ac = io.get_table('txt\\huff_codes_' + channel + '_ac.txt')
    huff_codes_dc = io.get_table('txt\\huff_codes_' + channel + '_dc.txt')

    huff_codes_reversed_ac = {code: symbol for symbol, code in huff_codes_ac.items()}
    huff_codes_reversed_dc = {code: symbol for symbol, code in huff_codes_dc.items()}

    decoded_data = []
    temp_code = ""
    decoded_values = []
    i = 0

    while decoded_values != [1,0]:
        decoded_values = []
        temp_code += compressed_data[i]
        if temp_code in huff_codes_reversed_dc:
            symb = huff_codes_reversed_dc[temp_code]
            length = ord(symb)
            i += 1
            value = compressed_data[i : i + length]

            if value != '':
                if value[0] == '0':
                    value = int('1' + value[1:], 2)
                else:
                    value = -int(value, 2)
            else:
                value = 0
            decoded_data.append(value)

            temp_code = ""
            i += length

            while decoded_values != [0, 0] and decoded_values != [1, 0]:
                temp_code += compressed_data[i]
                if temp_code in huff_codes_reversed_ac:
                    symb = huff_codes_reversed_ac[temp_code]

                    number = ord(symb)
                    count0 = number // 2**4     # количество нулей
                    length = number % 2**4      # категория

                    i += 1
                    value = compressed_data[i : i + length]
            
                    if value != '':
                        if value[0] == '0':
                            value = int('1' + value[1:], 2)
                        else:
                            value = -int(value, 2)
                    else:
                        value = 0

                    decoded_values = [count0, value]

                    decoded_data.append(decoded_values)
                    temp_code = ""
                    i += length
            
                else:
                    i += 1

        else:
            i += 1
    return [decoded_data, i]



# (0,10) (0,11) (2,5) (0,1) (EOB)
# ? 2 3 0 0 5 1 0...0
def rle_decode(vector):
    prev_dc = vector[0]
    decode_data = [vector[0]]
    i = 1
    start_of_seq0 = 1
    while vector[i] != [1, 0]:
        if vector[i] == [0,0]:
            decode_data += [0] * (64 - start_of_seq0)
            i += 1
            prev_dc = vector[i] + prev_dc
            decode_data += [prev_dc]
            start_of_seq0 = 1
        else:
            decode_data += [0] * vector[i][0] + [vector[i][1]]
            start_of_seq0 += vector[i][0] + 1
        i += 1
    decode_data.pop()
    return decode_data

