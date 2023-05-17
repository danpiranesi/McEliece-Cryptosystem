# FLOW:
# 1. compute inverse of P (P is a pemutation matrix created in key_generation)
# 2. compute c-hat (c = P^(-1)c)
# 3. use decoding algorithm A to decode c-hat to m-hat
# 4. compute m = m-hat*S^(-1)

import numpy as np

def inversePerm(p): # takes in permuatation matrix and returns the inverse of it
    # print("OG Perm Table")
    # print(p)
    p = np.asanyarray(p)
    s = np.transpose(p)
    return s

#P = np.array([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
#print(inversePerm(P))

def c_hat(c, inverseP): # multiplies c (ciphertext from Silvi) by result of inversePerm(P) and returns product
    pass

def decode(chat): # decodes c-hat to to m-hat 
    pass

def message(mhat, inverseS): # computes the message sent by Bob
    pass