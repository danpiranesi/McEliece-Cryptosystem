#Key generation
from array import array
import numpy as np
import reedsolo as rs

#Goal, be able to output a public key (G^,t)  and private keys G,P,S
# create a generating matrix G of size n by k that decodable with t errors 

def generatingMatrix(k,n): #create a reed-solomon generating matrix
    # k is message size
    # t is number of errors  t = (n-k)/2
    t = (n-k)//2

    #use reedsolo to create a generator poly
    #code from documentation for set-up
    prim = rs.find_prime_polys(c_exp=12, fast_primes=True, single=True)
    rs.init_tables(c_exp=12, prim=prim)

    
    gen = rs.rs_generator_poly(n-1)
    gen_poly = [int(i) for i in gen]
    #print(gen_poly)
   
    # generate a vector x of len n from the gen_poly
    x = np.array(gen_poly)

    #generate the matrix G such that each row is x rasised to a that power

    power = lambda ai, kpower :(ai**kpower) % n

    G = np.empty([k,n], dtype=int)

    for i in range(k):
        #create a new row
        new_row = []
        for a in x:
            new_row.append(power(a,i))

        #add that row to an numpy array

        G[i] = np.array(new_row)

    
    #return G , t
    return G, t , gen

# create an inveritble  matrix S of size k by k

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

def generate_keys(k, n): ##should we we able to input the size of the matrix you want????
    #return G^, G, P, S, t
    
    #choose t, and k

    G , t , gen = generatingMatrix(k,n)

    P = permMatrix(n)

    S = invertibleMatrix(k)

    midstep = np.matmul(S,G) #% 2
    G_hat = np.matmul(midstep,P) #% 2

    return G_hat, G, P, S, t, gen


#print(permMatrix(10))
#test = invertibleMatrix(10)
#print(test)
#print (np.linalg.inv(test))

#print(generatingMatrix(10,2))
#print(generate_keys(10))
