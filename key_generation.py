#Key generation
import numpy as np

#Goal, be able to output a public key (G^,t)  and private keys G,P,S



# create a generating matrix G of size n by m that decodable with t errors

def generatingMatrix():
    pass
    #return G , t

# create an inveritble  matrix S of size m by m

def invertibleMatrix():
    #generate a random array S of size mxm
    #try to find it's inverse
    
    # run numpy. linear algebra. inverse
        #if we get annswer return S
             #return S

        #else try again with a differnt matrix
    pass


#  create a permutation matrix P of size n by n

def permMatrix(n):
    #make a vector S of size n
    randvector = np.array([i for i in range(n)])
    #print(randvector)
    #find a random permutation of the vector call it X
    permvector = np.random.permutation(randvector)
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
    


# put the tree parts together

def generate_keys(): ##should we we able to input the size of the matrix you want????

    #return G^, G, P, S, t
    pass


print(permMatrix(10))
