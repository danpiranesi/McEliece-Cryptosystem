# hamming [7,4] key generations
from re import T
import numpy as np

"""
The following were very key resources for the devolopment of these methods:
    general understanding
        meceliece:
            http://www-math.ucdenver.edu/~wcherowi/courses/m5410/ctcmcel.html
            https://www.youtube.com/watch?v=fLwMvbfr76g&t=520s
            https://en.wikipedia.org/wiki/McEliece_cryptosystem
        error correcting codes:
            https://www.youtube.com/watch?v=kO6UlCY6idg
            https://www.youtube.com/watch?v=as_mNSx6OG8
    matrix operations
        https://www.youtube.com/watch?v=8OSAsm5tTwU&t=545s
        https://www.youtube.com/watch?v=fhgHRj2sfq0&t=2s
"""
def invertibleMatrix(k, matrix_ops):
    #generate a random array S of size kxk
    rand_array = np.random.randint(2,size = (k,k))
    matrix_ops += 1
    #try to find it's inverse
    try:
        np.linalg.inv(rand_array)
        matrix_ops += 1
        #if we get annswer return S
    except np.linalg.LinAlgError:
        return invertibleMatrix(k,matrix_ops)
        #else try again with a differnt matrix
    #return s
    return rand_array, matrix_ops

def permMatrix(n, matrix_ops):
    #  create a permutation matrix P of size n by n

    #make a vector S of size n
    ordervector = np.array([i for i in range(n)])
    
    #find a random permutation of the vector call it X
    permvector = np.random.permutation(ordervector)
    matrix_ops+=1
    

    #match the postion of the letter in the first vector to the row # of the second vector

    #create a dictionary of the permutation vector with it's postios
    positions = {}
    for i in range(n):
        positions[permvector[i]] = i
    
    #value is the row,  the key is the column for the perm matric

    #run an algorithm to make the appropriate permutation matrix

    #create an empty matrix P size nxn
    P = np.zeros((n,n),int)
    matrix_ops+=1
    #go through positions dictionary to fill out the matrix
    for y, x in positions.items():
        P[positions[x]][y] = 1
    
    return P, matrix_ops
    

def gen_keys(matrix_ops):

    #fixed hamming (7,4)
    G = np.array([[1,0,0,0,1,1,1],[0,1,0,0,0,1,1],[0,0,1,0,1,0,1],[0,0,0,1,1,1,0]])

    P, matrix_ops = permMatrix(7, matrix_ops)

    S, matrix_ops = invertibleMatrix(4,matrix_ops)

    #multiply it together
    G_hat = np.matmul(np.matmul(S, G),P) % 2
    matrix_ops += 2

    #the private key t is assumed to be 1, because hamming 7,4 can only correct 1 error
    return G_hat, G, P, S, matrix_ops