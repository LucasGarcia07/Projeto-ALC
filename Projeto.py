import csv
import numpy as np
import pandas as pd

reader = csv.reader(open("matriz.csv", "r"), delimiter=",")
x = list(reader)
matrixA = np.array(x).astype("float")

print(matrixA[:][0])





#fatoração LU
def fatoraLU(A):
    U = np.copy(A)
    n = np.shape(U)[0]
    L = np.eye(n)
    for j in np.arange(n-1):
        for i in np.arange(j+1,n):
            L[i,j] = U[i,j]/U[j,j]
            for k in np.arange(j+1,n):
                U[i,k] = U[i,k] - L[i,j]*U[j,k]
            U[i,j] = 0
    return L, U

print(fatoraLU(matrixA))



