import numpy as np
from hkey_generation import gen_keys
from h_encrypt import encryption, encrypt
#from h_decrypt import decrypt

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
# call decryption method
#original_message = decrypt(encrypted_message, P, S, t)
#print(original_message)