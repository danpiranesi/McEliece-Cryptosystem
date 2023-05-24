# Encryption for Hamming(7,4) code version 
import numpy as np

class encryptor:
        # Intialiting the encryptor
        def __init__(self, message, g_hat, matops, t=1):
            self.g_hat = g_hat      # G^: public key
            self.message = message  # message input (4^n) bit
            (k, n) = g_hat.shape    # G^ shape info
            self.n = n              # n: number of rows in G^
            self.t = t              # t: weight (number of errors)
            self.matops = matops    # matops: number of operations
            self.z = self.become_error_ridden()     # apply error array to the encryption
            self.cipher = self.encode()             # encoding the cipher text

        def become_error_ridden(self):
            # A method for generating error array 
            # 1. Make an array of size n with zeros
            self.z = np.zeros(self.n)
            # 2. Ｃhoosing t random indexes in this array to be error (1)
            self.matops += 1
            idx_list = np.random.choice(self.n, self.t, replace=False)
            for idx in idx_list:
                self.z[idx] = 1
            return self.z

        def encode(self):
            # Actual encoding through matrix multiplication / modulo
            # 1. Ecrypt the message using public key and convert it to binary
            self.c_prime = np.matmul(self.message, self.g_hat) % 2
            # 2. Increment to the operation attribute (counting operations)
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
