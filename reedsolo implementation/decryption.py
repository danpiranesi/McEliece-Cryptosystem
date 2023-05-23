import numpy as np
import reedsolo as rs

def decrypt(ciphertext, permutation_matrix, non_singular_matrix, t):
    # Step 1: Compute syndrome by multiplying inverse perm (matrix) and ciphertext (vector)
    syndrome = np.matmul(inversePerm(permutation_matrix), ciphertext) # %2 to remain in binary field
    print("perm: ")
    print(permutation_matrix)
    print("syndrome: ")
    print(syndrome)
    print(len(syndrome))
    print("t: ")
    print(t)

    # Step 2: Decode using reddsolo package
    rmes, recc, errata_pos = rs.rs_correct_msg(syndrome, t)

    #GEORGE - resize

    cor_size = recc[0:(len(non_singular_matrix))]
    print(cor_size)

    # Step 3: Convert syndrome to original message by multiplying by inverse of non singular matrix made in key generation
    decrypted_message = np.matmul(cor_size, np.linalg.inv(non_singular_matrix))%2 # to remain in binary field
    
    return decrypted_message

def inversePerm(p): # takes in permuatation matrix and returns the inverse of it
    p = np.asanyarray(p)
    s = np.transpose(p)
    return s