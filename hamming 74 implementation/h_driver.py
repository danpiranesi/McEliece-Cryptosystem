import numpy as np
from hkey_generation import gen_keys
from h_encrypt import encryption
import h_decrypt
import matplotlib.pyplot as plt

message = [1,1,1,1]

def run4bit(message, matrix_ops):
    # Step 1: KEY GENERATION
    # call key generation method
    G_hat, G, P, S, matrix_ops = gen_keys(matrix_ops)
    t=1
    #print(G_hat)
    #print(G)
    #print(S)
    #print(P)

    # Step 2: ENCRYPTION
    # encryption and return the ciphertext
    c, matrix_ops = encryption(message, G_hat, matrix_ops)

    #print("encrypted:")
    #print(c)

    # Step 3: DECRYPTION
    decryptie = h_decrypt.decryptor(c,S,P,G,message, matrix_ops) # TODO make output from encryption = c
    original_message = decryptie.decrypted_message

    matrix_ops = decryptie.matops

    #print("decrptyed")
    #print(original_message)

    return c, original_message, matrix_ops

#run4bit(message, 0)

def parse_4bits(message):
    #take a message and break it into 4 bit chunks
    parsed = []
    #for sake of simplicity only handle message that are divisble by 4
    if len(message)%4 == 0:
        #parse it
        while message:
            four = message[0:4]
            del(message[0:4])
            parsed.append(four)

        return parsed
    else:
        return "sorry, I can only parse messages who's length are mulptples of 4"




def runtime_exp(n): #how many different trials
    message_sizes = []
    operation_list = []

    for i in range(1,n):
        message_sizes.append(4*i)
        message = [1 for x in range(4*i)]
        #print(message)
        full_m = parse_4bits(message)
        
        decryted_chunks = []
        ops = 0
        for m in full_m:
            c, d, ops = run4bit(m,ops)

        operation_list.append(ops)
    return message_sizes, operation_list
        

sizes, mat_ops = runtime_exp(50)
print(sizes)
print(mat_ops)

plt.scatter(sizes, mat_ops)
plt.xlabel("Size of Input Message (bits)")
plt.ylabel("Number of Matrix Operations")
plt.title("Size of Message v Matrix Operation using Hamming [7,4] codes")
plt.show()