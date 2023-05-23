import numpy as np
from hkey_generation import gen_keys
from h_encrypt import encryption, encrypt
import h_decrypt

message = [1,1,0,1,1,1,0,0,1,0]

# Step 1: KEY GENERATION
# call key generation method
G_hat, G, P, S, = gen_keys()
t=1
#print(G_hat)
#print(G)
#print(S)
#print(P)


# Step 2: ENCRYPTION
# encryption and return the ciphertext
#encrypted_message = encryption(message, G_hat, t)

#print("encrypted:")
#print(encrypted_message)

# Step 3: DECRYPTION
decryptie = h_decrypt.decryptor(c,S,P,G,message) # TODO make output from encryption = c
original_message = decryptie.decrypted_message
print(original_message)