import csv
import numpy as np
import pandas as pd
import math as mt

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
#matrixA = normalizador(matrixA)
#----------------------------------------------------------------------------------------
#normas vetoriais
#norma p

def normapV(vetor, p):
    resultado = 0
    for i in range(len(vetor)):
        resultado += (abs(vetor[i]) ** p)    
    
    resultado **=(1/p)
    return resultado

#norma infinito

def normainfV(vetor):
    aux = abs(vetor[0])
    for i in range(1, len(vetor)):
        if(abs(vetor[i])>aux):
            aux = abs(vetor[i])
    return aux

#----------------------------------------------------------------------------------------
#normas matriciais
#norma p
def normapA(matrix, p):
    resultado = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            resultado += (abs(matrix[i][j])** p)
    resultado **= (1/p)
    return resultado

#norma infinito
def normainfA(matrix):
    aux = abs(matrix[0][0])
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if(abs(matrix[i][j])>aux):
                aux = abs(matrix[i][j])
    return aux

#----------------------------------------------------------------------------------------
#angulo entre vetores
def angulo(vetor1, vetor2):
    for i in range(len(vetor1)):
        soma = 0
        soma += vetor1[i] * vetor2[i]
        normav1 = normainfV(vetor1)
        normav2 = normainfV(vetor2)
    cosO = (soma/(normav1*normav2))
    return mt.acos(cosO)

#----------------------------------------------------------------------------------------
#número condição

def cond(matrix):
    normaA = normainfA(matrix)
    normainvA = normainfA(matrix)
    return normaA * normainvA
#----------------------------------------------------------------------------------------
print("Dado um Vetor e uma matriz esse programa calcula todas as normas da matriz e do vetor, o numero condicao da matriz e o angulo entre a primeira coluna da matriz e o vetor. \n\n")
print("Numero condicao da matriz: ", cond(matrixA), "\n\n")
print("Norma 1 da matriz: ", normapA(matrixA, 1), "\n")
print("Norma 2 da matriz: ", normapA(matrixA, 2), "\n")
print("Norma 3 da matriz: ", normapA(matrixA, 3), "\n")
print("Norma infinito da matriz A: ", normainfA(matrixA), "\n\n")
print("Norma 1 do vetor: ", normapV(vetorB, 1), "\n")
print("Norma 2 do vetor: ", normapV(vetorB, 2), "\n")
print("Norma 3 do vetor: ", normapV(vetorB, 3), "\n")
print("Norma infinito do vetor: ", normainfV(vetorB), "\n\n")
if(len(matrixA) == len(vetorB)):
    print("O angulo entre a matriz e o vetor: ", angulo(matrixA[:][0], vetorB))
else:
    print("O tamanho da matriz e do vetor sao diferentes, nao foi possivel efetuar o calculo do angulo")