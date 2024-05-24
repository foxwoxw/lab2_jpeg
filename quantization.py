import numpy as np
import in_out as io



def quantization_LQT(Q):
    # Luminance quantization table
    LQT = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                [12, 12, 14, 19, 26, 58, 60, 55],
                [14, 13, 16, 24, 40, 57, 69, 56],
                [14, 17, 22, 29, 51, 87, 80, 62],
                [18, 22, 37, 56, 68, 109, 103, 77],
                [24, 35, 55, 64, 81, 104, 113, 92],
                [49, 64, 78, 87, 103, 121, 120, 101],
                [72, 92, 95, 98, 112, 100, 103, 99]], dtype = np.double)
    S = np.double(5000 / Q if (Q > 0 and Q < 50) else 200 - 2 * Q)
    new_qt = (LQT * S + 50) / 100
    new_qt = new_qt.astype(np.double)
    io.save_table(new_qt, 'txt\\LQT.txt')
    return new_qt




def quantization_CQT(Q):
    # Chrominance quantization table
    CQT = np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                [18, 21, 26, 66, 99, 99, 99, 99],
                [24, 26, 56, 99, 99, 99, 99, 99],
                [47, 66, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99]], dtype = np.double)
    S = np.double(5000 / Q if (Q > 0 and Q < 50) else 200 - 2 * Q)
    new_qt = (CQT * S + 50) / 100
    new_qt = new_qt.astype(np.double)
    io.save_table(new_qt, 'txt\\CQT.txt')
    return new_qt
    


def quantization(array2d, QT):
    for i in range(8):
        for j in range(8):
            array2d[i, j] = np.round(array2d[i, j] / QT[i, j])
    array2d = array2d.astype(np.int16)
    return array2d








