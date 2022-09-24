from re import M
import numpy as np
import numpy.linalg as la





def rankPage(M, pro_pat=100):
    r = pro_pat * np.ones(M.shape[1]) / M.shape[1] # Sets up this vector (6 entries of 1/6 × 100 each)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        t=lastR-r
        print(la.norm(t))
        i += 1
    print(str(i) + " iterations to convergence.")
    return r

def extendedPageRank(linkMatrix, d) :
    #n = linkMatrix.shape[0]
    pro_pat=100 #100 Procastinating Pats
    M = d * linkMatrix + (1-d)/linkMatrix.shape[1] * np.ones([linkMatrix.shape[0], linkMatrix.shape[1]])
    r = pro_pat * np.ones(M.shape[1]) / M.shape[1] 
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        #t=lastR-r
        #print(la.norm(t))
        i += 1
    return r

def DampMatrix(M, d=0.5):
    resMatrix = d * M + (1-d)/M.shape[1] * np.ones([M.shape[0], M.shape[1]]) # np.ones() is the J matrix, with ones for each entry.
    return resMatrix


L2 = np.array([[0,   1/2, 1/3, 0, 0,   0, 0 ],
               [1/3, 0,   0,   0, 1/2, 0, 0 ],
               [1/3, 1/2, 0,   1, 0,   1/3, 0 ],
               [1/3, 0,   1/3, 0, 1/2, 1/3, 0 ],
               [0,   0,   0,   0, 0,   0, 0 ],
               [0,   0,   1/3, 0, 0,   0, 0 ],
               [0,   0,   0,   0, 0,   1/3, 1 ]])


d=0.5
randomPat=100
print(rankPage(DampMatrix(L2,d), randomPat))
print()
print()
print()
print(extendedPageRank(L2,d))
