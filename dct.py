import numpy as np



def calculate_H():
    H = np.ones((8, 8), dtype = np.double)
    H[0,:] *= 1/np.sqrt(8)
    с = np.sqrt(2/8)
    for p in range(1, 8):
        for q in range(0, 8):
            H[p, q] = с * np.cos((np.pi * (2 * q + 1) * p) / 16)
    H_T = np.transpose(H)
    return [H, H_T]


def fdct(H, A, H_T):
    C = np.matmul(np.matmul(H, A), H_T)
    #C = C.astype(np.double)
    return C

def idct(H, C, H_T):
    A = np.matmul(np.matmul(H_T, C), H)
    return A