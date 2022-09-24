from pickle import FALSE, TRUE
import numpy as np
from MatrixIsSingular import MatrixIsSingular
import RowEchelon as ref



def IsMatrixSingular(MatA):
    print("Original Matrix")
    print(MatA)
    print("\n\n")
    try:
        ref.RowEchelon.fixRowZero(MatA)
        print(MatA)
        print("\n\n") 
        ref.RowEchelon.fixRowOne(MatA)
        print(MatA)
        print("\n\n")
        ref.RowEchelon.fixRowTwo(MatA)
        print(MatA)
        print("\n\n")
        ref.RowEchelon.fixRowThree(MatA)
        print(MatA)
        return False
    except MatrixIsSingular:
        print("This Matrix cannot be inverted!")
        return True



A = np.array([
    [2, 1, 3, 4],
    [3, 1, 1, 2],
    [3, 4, 5, 8],
    [1, 3, 2, 7]
], dtype=np.float_)

B = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.int_)


#Singular Matrix
AB = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.float_)


#Non-Singular Matrix
AC = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)


print(IsMatrixSingular(B))
#print(IsMatrixSingular(AC))
