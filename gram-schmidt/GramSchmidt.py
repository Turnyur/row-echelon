import numpy as np
import numpy.linalg as la


verySmallNumber = 1e-14 # That's 1×10⁻¹⁴ = 0.00000000000001


def gsBasis4(A) :
    B = np.array(A, dtype=np.float_) # Make B as a copy of A, since we're going to alter it's values.
    # The zeroth column is easy, since it has no other vectors to make it normal to.
    # All that needs to be done is to normalise it. I.e. divide by its modulus, or norm.
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])
    # For the first column, we need to subtract any overlap with our new zeroth vector.
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]
    # If there's anything left after that subtraction, then B[:, 1] is linearly independant of B[:, 0]
    # If this is the case, we can normalise it. Otherwise we'll set that vector to zero.
    if la.norm(B[:, 1]) > verySmallNumber :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:, 1])
    # Now we need to repeat the process for column 2.
    # Insert two lines of code, the first to subtract the overlap with the zeroth vector,
    # and the second to subtract the overlap with the first.
    B[:, 2] = B[:, 2] - B[:, 2] @ B[:, 0] * B[:, 0]
    B[:, 2] = B[:, 2] - B[:, 2] @ B[:, 1] * B[:, 1]
    
    # Again we'll need to normalise our new vector.
    # Copy and adapt the normalisation fragment from above to column 2.
    if la.norm(B[:, 2]) > verySmallNumber :
        B[:, 2] = B[:, 2] / la.norm(B[:, 2])
    else :
        B[:, 2] = np.zeros_like(B[:, 2])
    
    
    
    # Finally, column three:
    # Insert code to subtract the overlap with the first three vectors.
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 0] * B[:, 0]
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 1] * B[:, 1]
    B[:, 3] = B[:, 3] - B[:, 3] @ B[:, 2] * B[:, 2]
    
    
    # Now normalise if possible
    if la.norm(B[:, 3]) > verySmallNumber :
        B[:, 3] = B[:, 3] / la.norm(B[:, 3])
    else :
        B[:, 3] = np.zeros_like(B[:, 3])
    
    
    
    # Finally, we return the result:
    return B

def gsBasis(A) :
    B = np.array(A, dtype=np.float_) # Make B as a copy of A, since we're going to alter it's values.
    # Loop over all vectors, starting with zero, label them with i
    for i in range(B.shape[1]) :
        # Inside that loop, loop over all previous vectors, j, to subtract.
        #let n=B.shape[1]
        #then i=0,1,2 .... n-1
        for j in range(i) :
            #then j= 0,1 ... i-1
            # Complete the code to subtract the overlap with previous vectors.
            # you'll need the current vector B[:, i] and a previous vector B[:, j]
            #B[:, i] = B[:, i] - B[:, i]@ B[:, j] * B[:, j]
            #print()
            
            print(B[:, i])
            print()
            print()
            print(B[:, j])
            # print()
            # print()
            # print()
            # print()
        # Next insert code to do the normalisation test for B[:, i]
            #print(i, j)
        #if la.norm(B[:, i]) > verySmallNumber :
            #B[:, i] = B[:, i] / la.norm(B[:, i])
        #else :
            #B[:, i] = np.zeros_like(B[:, i])
            
        
            
    # Finally, we return the result:
    return B


# This function uses the Gram-schmidt process to calculate the dimension
# spanned by a list of vectors.
# Since each vector is normalised to one, or is zero,
# the sum of all the norms will be the dimension.
def dimensions(A) :
    return np.sum(la.norm(gsBasis(A), axis=0))


def testGround(A):
    B = np.array(A, dtype=np.float_)
    normForm =la.norm(B[:, 1])
    print(B) 
    print(normForm)
    
    
V = np.array([[1,0,2,6],
              [0,1,8,2],
              [2,8,3,1],
              [1,-6,2,3]], dtype=np.float_)

#testGround(V)
#print(V)
#print(gsBasis4(V))
gsBasis(V)
#print(V.shape[0])
#print(V.shape[1])
