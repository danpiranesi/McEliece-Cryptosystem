# Encryption for Hamming(7,4) code version 
import numpy as np

def encryption(message,G , matops):
    # G transposing
    #G_t = np.transpose(G)
    # x = G^T*p, Pre-mult and modulo 2
    encoded = np.matmul(message,G)%2
    matops +=1

    return encoded, matops


""""
# Testing
P = [1,0,1,1]
G_trans = [[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
G = np.transpose(G_trans)
#print(G)
encryption(P,G)
"""