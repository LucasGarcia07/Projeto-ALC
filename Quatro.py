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
#----------------------------------------------------------------------------------------
#normas vetoriais
#norma p

def normapV(vetor, p, n):
    resultado = 0
    for i in range(len(vetor)):
        resultado += (abs(vetor[i]) ** p)    
    
    resultado **=(1/p)
    return resultado

#norma infinito

def normainfV(vetor, n):
    aux = abs(vetor[0])
    for i in range(1, n):
        if(abs(vetor[i])>aux):
            aux = abs(vetor[i])
    return aux

#----------------------------------------------------------------------------------------
#normas matriciais
#norma p
def normapA(matrix, p, n, m):
    resultado = 0
    for i in range(m):
        for j in range(n):
            resultado += (abs(matrix[i][j])** p)
    resultado **= (1/p)
    return resultado

#norma infinito
def normainfA(matrix, n, m):
    aux = abs(matrix[0][0])
    for i in range(1, n):
        for j in range(0, n):
            if(abs(matrix[i][j])>aux):
                aux = abs(matrix[i][j])
    return aux

#----------------------------------------------------------------------------------------
#angulo entre vetores
def angulo(vetor1, vetor2):
    for i in range(len(vetor1)):
        soma = 0
        soma += vetor1[i] * vetor2[i]
        normav1 = normainfV(vetor1, len(vetor1))
        normav2 = normainfV(vetor2, len(vetor2))
    cosO = (soma/(normav1*normav2))
    return mt.acos(cosO)

#----------------------------------------------------------------------------------------
#número condição

def cond(matrix, n, m):
    normaA = normainfA(matrix, n, m)
    normainvA = normainfA(matrix, n, m)
    return normaA * normainvA
