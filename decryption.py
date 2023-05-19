import numpy as np

def decrypt(ciphertext, permutation_matrix, non_singular_matrix):
    # Step 1: Compute syndrome by multiplying inverse perm (matrix) and ciphertext (vector)
    syndrome = np.matmul(inversePerm(permutation_matrix).T, ciphertext) % 2 # %2 to remain in binary field

    # Step 2: Convert syndrome to original message by multiplying by inverse of non singular matrix made in key generation
    decrypted_message = np.matmul(syndrome, np.linalg.inv(non_singular_matrix)) % 2 # %2 to remain in binary field

    return decrypted_message

def inversePerm(p): # takes in permuatation matrix and returns the inverse of it
    p = np.asanyarray(p)
    s = np.transpose(p)
    return s

# Example usage
ciphertext = np.array([0, 1, 1])  # Example ciphertext from sender
permutation_matrix = np.array([[0, 1, 0],
                               [1, 0, 0],
                               [0, 0, 1]])  # Example permutation matrix

non_singular_matrix = np.array([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 1]])  # Example non-singular matrix

original_message = decrypt(ciphertext, permutation_matrix, non_singular_matrix)
print("Orignal message:", original_message) 