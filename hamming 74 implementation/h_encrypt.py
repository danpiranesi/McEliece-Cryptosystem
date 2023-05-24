# Encryption for Hamming(7,4) code version 
import numpy as np

class encryptor:
        def __init__(self, message, g_hat, matops, t=1):
            self.g_hat = g_hat
            self.message = message
            (k, n) = g_hat.shape
            self.n = n
            self.t = t
            self.matops = matops
            self.z = self.become_error_ridden() 
            self.cipher = self.encode()

        def become_error_ridden(self):
            self.z = np.zeros(self.n)
            self.matops += 1
            idx_list = np.random.choice(self.n, self.t, replace=False)
            for idx in idx_list:
                self.z[idx] = 1
            return self.z

        def encode(self):
            self.c_prime = np.matmul(self.message, self.g_hat) % 2
            self.matops += 1
            c = (self.c_prime + self.z) % 2
            return c

        def get_encrypted(self):
            return self.cipher
        
# original method:
"""def encryption(message,G , matops):
    # G transposing
    #G_t = np.transpose(G)
    # x = G^T*p, Pre-mult and modulo 2
    encoded = np.matmul(message,G)%2
    matops +=1
    return encoded, matops"""
