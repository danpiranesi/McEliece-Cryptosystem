import numpy as np
import reedsolo as rs

# ErrorVector
def errorVec(n,t):
    # Generate an error array with n = length, t = # of 1s
    # Error vector should have the same dimesion as the input
    error = np.zeros(n, dtype=int)

    # pick t random locations to be 1
    locations = np.random.choice(error.size, t, replace = False)
    print(locations)
    for x in locations:
        error[x] = 1 
    return error

# Binary Encoder
### IMPORTANT: This may not work if the sub list length differ!! (aka if there's a space)
### In utf8, space is a binary with length of 6 while the rest are 7
### Thus the original implementation will return a np.array of list objs in those situation
def BiEncoderUTF8(script):
    # Taking in a message x and encode in binary
    # listBi =  list(list(format(x, 'b')) for x in bytearray(script, "utf-8"))
    BiString= ("".join(format(x, 'b')) for x in bytearray(script, "utf-8"))
    #binary = np.array(listBi)
    return BiString

# Encryption 
# p + error
def encryption(message,Ghat,t):

    # Error generation
    e = errorVec(len(message), t)
    print(e)

    #-----------------------------------------
    # DAN: I think we ought to add errors here
    # y = xG' + e

    noErrorVec = np.matmul(message,Ghat)
    for i, ei in enumerate(e): noErrorVec[i] += ei

    encrypted = noErrorVec
    #------------------------------------------
    
    # This should be a numpy ndarray
    # encrypted = rs.RSCodec(encrypted)
    print(encrypted)
    return encrypted

def read_t(t_path):
    # Get weight t from the txt
    with open(t_path) as t_txt:
        t = t_txt.readline()
    t = int(t)
    return t

def read_P(P_path):
    # Get weight t from the txt
    pkey = np.loadtxt(P_path)
    return pkey

# The full encryption 
def encrypt(message,key,t):
    # codedText = BiEncoderUTF8(message)

    # Take in a public key from file import
    # For testing just use some arbitrary matrix
    
    # Changing this later
    codedText = message
    print ("UTF8:",codedText)

    encrypted_message = rs.RSCodec(message,key,t)
    print ("Encrypted Message:",encrypted_message)
    
# Testing
#encrypt([1,0,1],np.array([[0, 1, 0],[1, 0, 0],[0, 0, 1]]),5)

