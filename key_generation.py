#Key generation
from array import array
import numpy as np

#Goal, be able to output a public key (G^,t)  and private keys G,P,S



# create a generating matrix G of size n by k that decodable with t errors

def generatingMatrix(k,t): #create a reed-solomon generating matrix
    # k is message size
    #t is number of error  t = (n-k)/2
    #caluculate an n based of t and l
    n = 2*t + k
   
    # generate a vector x of len n, values(0,1,2,3,4,...,n-1)
    x = np.array([i for i in range(n)])

    #generate the matrix G such that each row is x rasised to a that power

    power = lambda ai, kpower :(ai**kpower)%2

    G = np.empty([k,n], dtype=int)

    for i in range(k):
        #create a new row
        new_row = []
        for a in x:
            new_row.append(power(a,i))

        #add that row to an numpy array

        G[i] = np.array(new_row)

    
    #return G , n
    return G, n

# create an inveritble  matrix S of size k by k

def invertibleMatrix(k):
    #generate a random array S of size kxk
    rand_array = np.random.randint(2,size = (k,k))
    
    #try to find it's inverse
    try:
        np.linalg.inv(rand_array)
        #if we get annswer return S
    except np.linalg.LinAlgError:
        invertibleMatrix(k)
        #else try again with a differnt matrix

    #return s
    return rand_array


#  create a permutation matrix P of size n by n

def permMatrix(n):
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
    


# put the tree parts together

def generate_keys(): ##should we we able to input the size of the matrix you want????
    #return G^, G, P, S, t
    
    #choose t, and k
    t=5
    k=10

    G , n = generatingMatrix(k,t)

    P = permMatrix(n)

    S = invertibleMatrix(k)

    midstep = np.matmul(S,G)
    G_hat = np.matmul(midstep,P)
    
    return G_hat , G, P , S, t


#print(permMatrix(10))
#print(invertibleMatrix(10))
#print(generatingMatrix(10,2))
#print(generate_keys())
