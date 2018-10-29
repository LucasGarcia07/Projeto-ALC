import csv
import numpy as np
import pandas as pd
import math as mt

#pegar a matriz do banco de dados
reader = csv.reader(open("matriz.csv", "r"), delimiter=",")
x = list(reader)
matrixA = np.array(x).astype("float")

#pegar o vetor do banco de dados
reader = csv.reader(open("vetor.csv", "r"))
x = list(reader)
vetorB = np.array(x).astype("float")

#escreve o vetor ou matriz resultado num arquivo
def settArquivo(vetor):
    x = np.around(vetor)
    np.savetxt("resultado.txt", x, delimiter= ",")

settArquivo(vetorB)
#----------------------------------------------------------------------------------------

#substituição para frente  -> matriz triangular inferior
def substituiFrente(A,b):
    n = np.shape(b)[0]
    x = np.zeros(n)
    for i in range(0,n):
        x[i] = ((b[i] - np.dot(A[i][0:i], x[0:i]))/A[i][i])
    return x
#----------------------------------------------------------------------------------------

#substituição para trás -> matriz triangular superior
def substituiTras(A, b):
    n = np.shape(b)[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
       x[i] = (b[i] - np.dot(A[i, i + 0:n], x[i + 0:n]))/A[i, i]
    return x
#----------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------

#Método iterativo jacobi
def jacobi(A, b, tol):

    n=np.shape(A)[0]
    x = np.zeros(n)
    M0 = np.zeros(n)   
    it = 0
    while (it < 10000):
        it += 1   
        for i in np.arange(n):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):
                x[i] -= A[i,j]*M0[j]
            x[i] /= A[i,i]
        if (np.linalg.norm(x-M0,np.inf) < tol):
            return x
        M0 = np.copy(x)
    return x

#----------------------------------------------------------------------------------------


#Verificador da lei de Benford

def benford(vetor, tol):
    vBenford = np.zeros(10)
    Qnum = np.zeros(10)
    Qcomp = np.zeros(10)
    n = len(vetor)
    Qresult = np.zeros(10)

    for i in range(1,10):
        vBenford[i] = mt.log10(1+1/i)

    for i in range(n):
        if(vetor[i] < 1):
            vetor[i] *= 10
        if(vetor[i] == 1):
            Qnum[1] += 1
        if(vetor[i] == 2):
            Qnum[2] += 1
        if(vetor[i] == 3):
            Qnum[3] += 1
        if(vetor[i] == 4):
            Qnum[4] += 1
        if(vetor[i] == 5):
            Qnum[5] += 1
        if(vetor[i] == 6):
            Qnum[6] += 1
        if(vetor[i] == 7):
            Qnum[7] += 1
        if(vetor[i] == 8):
            Qnum[8] += 1
        if(vetor[i] == 9):
            Qnum[9] += 1
    
    for i in range(1,10):
        Qcomp[i] = Qnum[i]/n
    
    for i in range(1,10):
        Qresult[i] = abs(Qcomp[i] - vBenford[i])
        print("Benford",i,vBenford[i])
        print("Resultado:",Qcomp[i])
        print("Diferenca:",Qresult[i])
        print("-----------------------------")
    
    print("tolerancia:", tol)

    for i in range(1,10):
        if(Qresult[i] > tol/100):
            print("Nao satisfaz benford")
            break
    else:
        print("Satisfaz benford")

benford(vetorB, 1)