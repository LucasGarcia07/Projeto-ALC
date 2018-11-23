import numpy as np
import pandas as pd
import math as mt
from numpy import linalg as la

#pegar a matriz do banco de dados
arq = open("matriz.txt", "r")
matrixA = pd.read_table("matriz.txt", delim_whitespace= True, header= None, thousands='.', dtype= np.float32)
matrixA = matrixA.values

#pegar o vetor do banco de dados
arq = open("vetor.txt", "r")
vetorB = pd.read_table("vetor.txt", delim_whitespace= True, header= None, thousands='.', dtype= np.float32)
vetorB = vetorB.values

#----------------------------------------------------------------------------------------
def normalizador(matrixA):
    for i in range(len(matrixA[0])):
        for j in range(len(matrixA)):
            matrixA[j][i] = (matrixA[j][i] - min(matrixA[:,i]))/ (max(matrixA[:,i]) - min(matrixA[:,i]))
    return matrixA

matrixA = normalizador(matrixA)
#substituição para frente  -> matriz triangular inferior
def substituiFrente(A,b):
    n = np.shape(b)[0]
    x = np.zeros(n)
    for i in range(0,n):
        x[i] = ((b[i] - np.dot(A[i][0:i], x[0:i]))/A[i][i])
    return x
#----------------------------------------------------------------------------------------
def calculaResiduo(A, b, x):
    aux = np.dot(A, x)
    for i in range(len(b)):
        b[i] = b[i] - aux[i]
    return la.norm(b, 2)

#Verifica os dados de entrada da substituição para frente
def verificaTinf(A):
    aux = 0
    if(len(A) != len(A[0])):
        aux += 1
    for i in range(len(A)):
        for j in range(len(A)):
            if(j>i):
                if(A[i][j] != 0):
                    aux += 1                    
    if(aux == 0):
        return 0
    else:
        return 1
def verificaCriterioLinha(A):
    aux2 = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = abs(A[i][j])
    for i in range(len(A)):
        aux = 0
        for j in range(len(A[0])):
            if(i != j):
                aux += A[i][j]
        if(A[i][i] <= aux):
            aux2+=1
    if(aux2 != 0):
        return 1
    else:
        return 0
        
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

#falando com o usuário e pegando a escolha dos métodos

print("\nESCOLHA UM DOS METODOS PARA A RESOLUCAO DO SISTEMA\n\n"
        , "1: Substituicao para Frente\n"
        , "2: Fatoracao L U\n"
        , "3: Metodo de Jacobi\n")
entrada = input("Digite um numero: ")

if(entrada == '1'):
    condicao = verificaTinf(matrixA)
    if(condicao == 0):
        x = substituiFrente(matrixA, vetorB)
        y = calculaResiduo(matrixA, vetorB, x)
        print("\nSeu vetor resposta eh: \n", x,"\nA norma do residuo eh: \n",'{:.10f}'.format(y))
        arq = open("resultado.txt", "w")
        arq.write("Vetor resultado: \n")
        arq.write(str(x))
        arq.write("\nNorma do residuo: \n")
        arq.write('{:.10f}'.format(y))
    else:
        print("Nao foi possivel usar o metodo. Matriz nao condiz com as regras")
    

elif(entrada == '2'):
    if(len(matrixA) == len(matrixA[0]) & len(matrixA) == len(vetorB)):
        x = fatoraLU(matrixA, vetorB)
        y = calculaResiduo(matrixA, vetorB, x)
        print("Vetor resultado: \n", x, "\n Norma do residuo: \n", '{:.10f}'.format(y))
        arq = open("resultado.txt", "w")
        arq.write("Vetor resultado: \n")
        arq.write(str(x))
        arq.write("\nNorma do residuo: \n")
        arq.write('{:.10f}'.format(y))
    else:
        print("Nao foi possivel usar o metodo. Matriz nao eh quadrada")

elif(entrada == '3'):
    temp = verificaCriterioLinha(matrixA)
    if(len(matrixA) == len(matrixA[0])):
        p = float(input("Digite a tolerancia para o jacobi: "))
        x = jacobi(matrixA, vetorB, p)
        print("\n Vetor resultado: \n", x)
        arq = open("resultado.txt", "w")
        arq.write("Vetor resultado: \n")
        arq.write(str(x))
        if(temp != 0):
            print("\nA matriz nao satisfaz o criterio das linhas, portanto nao temos certeza se ela converge. \n")
        else:
            print("\nA matriz satisfaz o criterio das linhas, logo converge. \n")
    else:
        print("\nA matriz precisa ser quadrada\n")

    