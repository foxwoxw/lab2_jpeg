import pickle


def save_table(data, filename):
    with open(filename, 'wb') as table_file:
        pickle.dump(data, table_file)


def get_table(in_file):
    with open(in_file, 'rb') as table_file:
        data = pickle.load(table_file)
    return data


# последний байт - количество незначащих нулей в конце
def out_encoded_vectors(str_code):
    f = open('txt\\result.txt', 'wb')
    N = len(str_code)
    tmp = ''
    count = 0
    arr = []
    for i in range(N):
        tmp += str_code[i]
        count += 1
        if count == 8:
            arr.append(int(tmp, 2))
            count = 0
            tmp = ''
    if count != 0:
        delta = 8 - count
        arr.append(int(tmp + '0' * delta, 2))
        arr.append(delta)
    else:
        arr.append(0)
    f.write(bytes(arr))
    f.close()



# rw, rh - реальный размер картинки
# bx, by - ширина и высота блоков для cb, cr
def in_encoded_vectors(filename):
    with open(filename[:-4] + '_size.txt', 'r', encoding='utf-8') as f:
        rw, rh, bx, by = [int(i) for i in f.readline().split()]

    with open(filename, 'rb') as f:
        data = list(f.read())

    delta = data.pop() # лишние биты

    str_code = ''
    for symb in data:
        bin_value = bin(symb)[2:]
        str_code += '0' * (8 - len(bin_value)) + bin_value
    if delta != 0:
        str_code = str_code[:-delta]

    return [str_code, rw, rh, bx, by]

