# hamming [7,4] key generations
from re import T
import numpy as np


def invertibleMatrix(k):
    #generate a random array S of size kxk
    rand_array = np.random.randint(2,size = (k,k))
    
    #try to find it's inverse
    try:
        np.linalg.inv(rand_array)
        #if we get annswer return S
    except np.linalg.LinAlgError:
        return invertibleMatrix(k)
        #else try again with a differnt matrix

    #return s
    return rand_array



def permMatrix(n):
    #  create a permutation matrix P of size n by n

    #make a vector S of size n
    ordervector = np.array([i for i in range(n)])
    #print(randvector)
    #find a random permutation of the vector call it X
    permvector = np.random.permutation(ordervector)
    #print(permvector)

    #match the postion of the letter in the first vector to the row # of the second vector

    #create a dictionary of the permutation vector with it's postios
    positions = {}
    for i in range(n):
        positions[permvector[i]] = i
    #print(positions)
    #value is the row,  the key is the column for the perm matric

    #run an algorithm to make the appropriate permutation matrix
    #create an empty matrix P size nxn

    P = np.zeros((n,n),int)
    for y, x in positions.items():
        P[positions[x]][y] = 1
    #print(P)
    return P
    

def gen_keys():

    G = np.array([[1,0,0,0,1,1,1],[0,1,0,0,0,1,1],[0,0,1,0,1,0,1],[0,0,0,1,1,1,0]])

    P = permMatrix(7)

    S = invertibleMatrix(4)

    #When do we want to convert to binary? - George
    midstep = np.matmul(S,G) % 2
    G_hat = np.matmul(midstep,P) % 2

    return G_hat, G, P, S

G_hat, G, P, S = gen_keys()

print("g")
print(G)

print("s")
print(S)

print("p")
print(P)

print("g^")
print(G_hat)



