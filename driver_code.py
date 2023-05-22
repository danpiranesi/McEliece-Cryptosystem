import numpy as np

from key_generation import generate_keys
from encryption import encryption, encrypt
from decryption import decrypt

message = [1,1,0,1,1,1,0,0,1,0]

# Step 1: KEY GENERATION
# call key generation method
G_hat, G, P, S, t, gen, gen = generate_keys(len(message))
#print(G_hat)

"""put public keys (G hat and t) onto .txt files
ghatFile = open("Ghat.txt", "w")
tFile = open("t.txt", "w")
tFile.write(str(t))
np.savetxt("Ghat.txt", G_hat)
ghatFile.close
tFile.close"""

# Step 2: ENCRYPTION
# input message to send
# read .txt file to collect keys

# encryption and return the ciphertext
encrypted_message = encrypt(b"test larry", t)
print("encrypted:")
print(encrypted_message)

# Step 3: DECRYPTION
# call decryption method
original_message = decrypt(encrypted_message, P, S, t)