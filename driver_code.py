import numpy as np

from key_generation import generate_keys
# from encryption import
from decryption import decrypt
from encryption import encryption

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
message = [1,1,0,1,1,1,0,0,1,0]
# read .txt file to collect keys

# encryption and return the ciphertext
encrypted_message = encryption(message,G,t)
print(encrypted_message)

# Step 3: DECRYPTION
# call decryption method
original_message = decrypt(c, P, S)

#print(inversePerm(permMatrix(5)))