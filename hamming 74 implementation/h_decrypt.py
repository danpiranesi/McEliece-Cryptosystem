import numpy as np
import math

class decryptor:
    def __init__(self, c, S, P, G, m, matops):
        self.c = c #cipher (vector)
        self.S = S #invertable/scrambler (matrix)
        self.P = P #permutation (matrix)
        self.G = G #generator (matrix)
        self.m = m #message (list)
        self.matops = matops #counter for experiment

        self.decrypted_message = self.decrypt() #method call to decrypt the cipher text
        self.isCorrect = (self.m == self.decrypted_message) #bool to be used for verification (this is super handy for dealing with strange bugs we didn't have time to diagnose)

    # decrypt cipher text given SPG matrices
    def decrypt(self):
            P_inverse = np.linalg.inv(self.P) #invert permutation
            S_inverse = np.linalg.inv(self.S) #invert scrambler
            
            c_prime = np.matmul(self.c, P_inverse) #calculate cprime
            self.matops += 1
            
            m_prime = self.error_correction(c_prime) #method call to check c_prime for errors

            if m_prime is None or len(m_prime) != 4: #bug catcher. not that ideal of a solution. hardcoding in an m_prime that'll trigger decryption to start over again
                m_prime = [0, 1, 1, 1]

            decrypted = np.matmul(m_prime, S_inverse) % 2 #final step!!!

            return decrypted
        
    def error_correction(self, c_prime):
            syndrome = np.matmul(c_prime, np.transpose(self.G)) % 2 # product of c_prime and G. we are unsure why we transpose G here and not in encryption, but in debugging we found transposing here to be crucial

            syndrome_total = 0 #counter
            
            for i in range(4): #we will always have syndromes of size 4
                syndrome_total += 2**i * syndrome[i] #this website https://asecuritysite.com/encryption/mce_k inspired my thinking for this counter

            if (int(syndrome_total - 1) & int(syndrome_total)) == 0: # if no errors return the cipher text to finish decryption
                return c_prime[0:(c_prime.size - 4)+1] 
            else: 
                err_loc = int(syndrome_total - math.ceil(np.log2(syndrome_total)) - 1) #thinking for this syntax inspired by last mentioned website
                if err_loc > 6: #a bug this implementation runs into is occasionally the error location will be outside of the length of the syndrome. this if statement is to print message denoting failure. the decryption will be retried when this occurs
                    print ("Computation failed. Trying again.")
                else: #if syndrome is satisfactory flip error (i.e. 0 to 1 or 1 to 0)
                    if c_prime[err_loc] == 1: 
                        c_prime[err_loc] = 0
                        return c_prime[0:(c_prime.size - 4)+1]
                    elif c_prime[err_loc] == 0:
                        c_prime[err_loc] = 1
                        return c_prime[0:(c_prime.size - 4)+1]
                    else:
                        print("Too many errors to decrypt")
            

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
    
