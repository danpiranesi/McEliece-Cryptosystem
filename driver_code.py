import numpy as np

from key_generation import generate_keys
# from encryption import
from decryption import decrypt

# Step 1: KEY GENERATION
# call key generation method
G_hat, G, P, S, t = generate_keys()

# put public keys (G hat and t) onto .txt files
ghatFile = open("Ghat.txt", "w")
tFile = open("t.txt", "w")
tFile.write(str(t))
np.savetxt("Ghat.txt", G_hat)
ghatFile.close
tFile.close

# Step 2: ENCRYPTION
# input message to send
# read .txt file to collect keys
# encrypt message using methods
# return ciphertext

# Step 3: DECRYPTION
# call decryption method
original_message = decrypt(c, P, S)

#print(inversePerm(permMatrix(5)))