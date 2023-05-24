import numpy as np
from hkey_generation import gen_keys
import h_encrypt
import h_decrypt
import matplotlib.pyplot as plt

message = [1,1,1,1]

def run4bit(message, matrix_ops):
    # Step 1: KEY GENERATION
    # call key generation method
    G_hat, G, P, S, matrix_ops = gen_keys(matrix_ops)
    t=1

    # Step 2: ENCRYPTION
    # encryption and return the ciphertext
    #c, matrix_ops = encryption(message, G_hat, matrix_ops)
    encryptie = h_encrypt.encryptor(message, G_hat, matrix_ops, t)
    c = encryptie.get_encrypted()
    matrix_ops = encryptie.matops

    print("Encoded: " + str(encryptie.c_prime))
    print("Encrypted: " + str(encryptie.cipher))
    print("Error Introduced: " + str(encryptie.z))

    # Step 3: DECRYPTION
    decryptie = h_decrypt.decryptor(c,S,P,G,message, matrix_ops)
    decrypted_message = decryptie.decrypted_message
    print("Message: " + str(decryptie.decrypted_message))
    matrix_ops = decryptie.matops

    if False in decryptie.isCorrect: # solution to possible errors we were encountering
        run4bit(message, matrix_ops)

    return c, decrypted_message, matrix_ops
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


def main():     
    sizes, mat_ops = runtime_exp(50)

    plt.scatter(sizes, mat_ops)
    plt.xlabel("Size of Input Message (bits)")
    plt.ylabel("Number of Matrix Operations")
    plt.title("Size of Message v Matrix Operation using Hamming [7,4] codes")
    plt.show()

if __name__ == "__main__":
    main()
