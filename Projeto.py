import csv
import numpy as np
import pandas as pd

#pegar a matriz do banco de dados
reader = csv.reader(open("matriz.csv", "r"), delimiter=",")
x = list(reader)
matrixA = np.array(x).astype("float")

#pegar o vetor do banco de dados
reader = csv.reader(open("vetor.csv", "r"))
x = list(reader)
vetorB = np.array(x).astype("float")

#substituição para frente  -> matriz triangular inferior
def substituiFrente(A,b):
    n = np.shape(b)[0]
    x = np.zeros(n)
    x[0] = b[0]/A[0][0]
    for i in range(1,n):
        x[i] = ((b[i] - np.dot(A[i][0:i], x[0:i]))/A[i][i])
    return x

#substituição para trás -> matriz triangular superior
def substituiTras(A, b):
    n = np.shape(b)[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
       x[i] = (b[i] - np.dot(A[i, i + 0:n], x[i + 0:n]))/A[i, i]
    return x

#fatoração LU
def fatoraLU(A, b):
    U = np.copy(A)
    n = np.shape(U)[0]
    L = np.eye(n)
    for j in range(n-1):
        for i in range(j+1,n):
            L[i,j] = U[i,j]/U[j,j]
            for k in range(j+1,n):
                U[i,k] = U[i,k] - L[i,j]*U[j,k]
            U[i,j] = 0
    y = substituiFrente(L, b)
    x = substituiTras(U, y)
    return x





