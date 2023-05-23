import numpy as np
import math

class decryptor:
    def __init__(self, c, S, P, G, m, matops):
        self.c = c #cipher
        self.S = S #scrambler
        self.P = P #permutation
        self.G = G #generator
        self.m = m #message
        self.matops = matops

        self.decrypted_message = self.decrypt()
        self.isCorrect = (self.m == self.decrypted_message)

    def decrypt(self):
            # decrypt message given SPG

            P_inverse = np.linalg.inv(self.P) #invert permutation
            S_inverse = np.linalg.inv(self.S) #invert scrambler
            c_prime = np.matmul(self.c, P_inverse) #calculate cprime
            self.matops += 1
            
            
            #test to see if keys are correct
            decoded_c = c_prime[0:4]
            #TODO is there an easy way to turn decrytped from floats to int?
            decrypted = np.matmul(decoded_c, S_inverse) % 2
            self.matops +=1
            """
            
            m_prime = self.error_correction(c_prime) # check message with 
            print(m_prime)
            print(S_inverse)
            
            decrypted = np.matmul(m_prime, S_inverse) % 2
            """
            return decrypted
        
    def error_correction(self, c_prime):
            syndrome = np.matmul(c_prime, np.transpose(self.G)) % 2
            #print(syndrome)
            syndrome_err_size = np.ma.size(syndrome, 0) # mask it
            syndrome_total = 0

            for i in range(syndrome_err_size):
                syndrome_total += 2**i * syndrome[i]

            #print(syndrome_total)

            if (int(syndrome_total - 1) & int(syndrome_total)) == 0: # if no errors return
                return c_prime[0:(c_prime.size - syndrome_err_size)]
            
            else: 
                error_message = c_prime
                error_bit = int(syndrome_total - math.ceil(np.log2(syndrome_total)) - 1)
                #print(error_bit)
                #print(c_prime.size)
                #print(syndrome_err_size)
                if error_message[error_bit] == 1:
                    error_message[error_bit] = 0
                    return error_message[0:(c_prime.size - syndrome_err_size)+1]
                elif error_message[error_bit] == 0:
                    error_message[error_bit] = 1
                    return error_message[0:(c_prime.size - syndrome_err_size)+1]
                else:
                    print("Unable to decrypt this message due to too many errors")
            

#---------TESTING---------

c = [0,1,1,0,1,1,0]
S = np.array([[1,1,0,1],
              [1,0, 0, 1],
              [0, 1, 1, 1],
              [1, 1, 0, 0]])
P = np.array([[0,1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0]])
G = np.array([[1,0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1]])
m = [1,1,0,1]

#testDec = decryptor(c,S,P,G,m)
#print(testDec.decrypted_message)
#print(testDec.isCorrect)
    
