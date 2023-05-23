import numpy as np
from key_generation import generate_keys
from encryption import encryption, encrypt
from decryption import decrypt

message = [1,1,0,1,1,1,0,0,1,0]

# Step 1: KEY GENERATION
# call key generation method
G_hat, G, P, S, t, gen = generate_keys(len(message), 10)
#print(G_hat)
#print(G)
#print(S)
#print(len(P))
print(t)

# Step 2: ENCRYPTION
# input message to send
# read .txt file to collect keys

# encryption and return the ciphertext
encrypted_message = encryption(message, G_hat, t)
#encrypted_message = encrypt("test larry", t)
print("encrypted:")
print(encrypted_message)

# Step 3: DECRYPTION
# call decryption method
original_message = decrypt(encrypted_message, P, S, t)
print(original_message)