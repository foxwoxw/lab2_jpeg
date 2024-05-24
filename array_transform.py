import numpy as np


def zigzag(array2d):
    col, rows = array2d.shape[1], array2d.shape[0]
    array1d = []
    x = 0
    y = -1
    all_diagonals = rows + col - 1
    for diagonal in range(all_diagonals):
        if diagonal % 2 == 0:
            y += 1
            while x > -1 and y < rows:
                array1d.append(array2d[y][x])
                x -= 1
                y += 1
            if y == rows:
                y -= 1
                x += 1
        else:
            x += 1
            while y > -1 and x < col:
                array1d.append(array2d[y][x])
                y -= 1
                x += 1
            if x == col:
                x -= 1
                y += 1
    array1d = np.asarray(array1d, dtype = np.int16)
    return array1d



def fill_zigzag(vector):
    array2d = np.zeros((8, 8), dtype = np.int32)
    col, rows = 8, 8
    x = 0
    y = -1
    i = 0
    all_diagonals = 15
    for diagonal in range(all_diagonals):
        if diagonal % 2 == 0:
            y += 1
            while x > -1 and y < rows:
                array2d[y][x] = vector[i]
                i += 1
                x -= 1
                y += 1
            if y == rows:
                y -= 1
                x += 1
        else:
            x += 1
            while y > -1 and x < col:
                array2d[y][x] = vector[i]
                i += 1
                y -= 1
                x += 1
            if x == col:
                x -= 1
                y += 1
    return array2d



def fill_array(vector, width, height):
    # размер в блоках по 64
    width = int(np.ceil(width / 8)) 
    height = int(np.ceil(height / 8))

    i = 0
    for h in range(height):
        tmp_x = []
        for w in range(width):
            array = fill_zigzag(vector[i : i + 64])
            i += 64
            if w == 0:
                tmp_x = array
            else:
                tmp_x = np.concatenate((tmp_x, array), axis = 1)
        if h == 0:
            tmp_y = tmp_x
        else:
            tmp_y = np.concatenate((tmp_y, tmp_x), axis = 0)
    tmp_y = tmp_y.astype(np.double)
    return tmp_y




# Kx, Ky - коэф сжатия
# array2d - np.arrray
def downsampling_KxKy(array2d, Kx, Ky):
    N, M = array2d.shape[1], array2d.shape[0]
    if Kx == 0: Kx = 1
    if Ky == 0: Ky = 1
    new_N = int(np.ceil(N / Kx))
    new_M = int(np.ceil(M / Ky))
    result = np.zeros((new_M, new_N), dtype = np.double)
    new_j = 0
    for j in range(0, M, Ky):
        new_i = 0
        for i in range(0, N, Kx):
            result[new_j, new_i] = array2d[j, i]
            new_i += 1
        new_j += 1
    return result




# Kx, Ky - коэф сжатия
# array2d - np.arrray
def upsampling_KxKy(array2d, Kx, Ky):
    N, M = array2d.shape[1], array2d.shape[0]
    if Kx == 0: Kx = 1
    if Ky == 0: Ky = 1
    new_N = N * Kx
    new_M = M * Ky
    result = np.zeros((new_M, new_N), dtype = np.double)
    old_j = 0
    for j in range(0, new_M):
        old_i = 0
        for i in range(0, new_N):
            result[j, i] = array2d[old_j, old_i]
            if (i + 1) % Kx == 0:
                old_i += 1
        if (j + 1) % Ky == 0:
            old_j += 1
    return result





# x_size, y_size - количество недостающих строк/столбцов
def resize_for_block(array2d, x_size, y_size):
    N = array2d.shape[1]    # x
    M = array2d.shape[0]    # y 
    if x_size != 0:
        new_array = array2d[:, (N - x_size): N]
        array2d = np.concatenate((array2d, new_array), axis = 1)
    if y_size != 0:
        new_array = array2d[(M - y_size): M, :]
        array2d = np.concatenate((array2d, new_array), axis = 0)
    return array2d



# добить для блоков 8 на 8
def resize_for_block8(array2d):
    N, M = array2d.shape[1], array2d.shape[0]
    col = N % 8
    rows = M % 8
    if col != 0:
        col = 8 - col
    if rows != 0:
        rows = 8 - rows
    return resize_for_block(array2d, col, rows)



# size_x, size_y - размер блока
# rows, col - кол-во недостающих строк и столбцов
def downsampling_average(array2d, size_x, size_y):
    N, M = array2d.shape[1], array2d.shape[0]
    col = size_x - N % size_x
    rows = size_y - M % size_y
    if col != 0 or rows != 0:
        array2d = resize_for_block(array2d, col, rows)
        N += col
        M += rows
    #print('\n', array2d)
    result = np.zeros((M // size_x, N // size_y), dtype = np.double)
    total = size_x * size_y
    new_j = 0
    for j in range(0, M, size_y):
        new_i = 0
        for i in range(0, N, size_x):
            result[new_j, new_i] = np.sum(array2d[j : (j + size_y), i : (i + size_x)]) / total
            new_i += 1
        new_j += 1
    return result





# size_x, size_y - размер блока
# rows, col - кол-во недостающих строк и столбцов
def upsampling_average(array2d, size_x, size_y):
    N, M = array2d.shape[1], array2d.shape[0]
    new_N = size_x * N
    new_M = size_y * M
    result = np.zeros((new_M, new_N), dtype = np.double)
    old_j = 0
    for j in range(new_M):
        old_i = 0
        for i in range(new_N):
            result[j, i] = array2d[old_j, old_i]
            if (i + 1) % size_x == 0:
                old_i += 1
        if (j + 1) % size_y == 0:
            old_j += 1
    return result





def closest_to_average(array2d, average, size_x, size_y):
    closest_value = array2d[0, 1]
    min_delta = 2**8
    for j in range(size_y):
        for i in range(size_x):
            delta = abs(array2d[j, i] - average)
            if delta < min_delta:
                min_delta = delta
                closest_value = array2d[j, i]
    return closest_value

            



# size_x, size_y - размер блока
# rows, col - кол-во недостающих строк и столбцов
def downsampling_closest_to_average(array2d, size_x, size_y):
    N, M = array2d.shape[1], array2d.shape[0]
    col = N % size_x
    rows = M % size_y
    if col != 0 or rows != 0:
        if col != 0:
            col = size_x - col
        if rows != 0:
            rows = size_y - rows
        array2d = resize_for_block(array2d, col, rows)
        N += col
        M += rows
    #print('\n', array2d)
    result = np.zeros((M // size_x, N // size_y), dtype = np.double)
    total = size_x * size_y
    new_j = 0
    for j in range(0, M, size_y):
        new_i = 0
        for i in range(0, N, size_x):
            arr_slice = array2d[j : (j + size_y), i : (i + size_x)]
            average = np.sum(arr_slice) / total
            result[new_j, new_i] = closest_to_average(arr_slice, average, size_x, size_y)
            new_i += 1
        new_j += 1
    return result



