import csv
import numpy as np
import pandas as pd
import math as mt
from random import randint
import copy

#pega matriz de treinamento
arq = open("matrizTreinamento.txt", "r")
matrixA = pd.read_table("matrizTreinamento.txt", delim_whitespace= True, header= None, thousands='.', dtype= np.float32)
matrixA = matrixA.values
#pega matriz de teste
arq = open("matrizTeste.txt", "r")
matrixB = pd.read_table("matrizTeste.txt", delim_whitespace= True, header= None, thousands='.', dtype= np.float32)
matrixB = matrixB.values

#----------------------------------------------------------------------------------------
#normaliza o banco de dados
def normalizador(matrixA):
    for i in range(len(matrixA[0])):
        for j in range(len(matrixA)):
            matrixA[j][i] = (matrixA[j][i] - min(matrixA[:,i]))/ (max(matrixA[:,i]) - min(matrixA[:,i]))
    return matrixA

matrixA = normalizador(matrixA)
matrixB = normalizador(matrixB)

#distancia entre dois vetores
def distancia(X, Y):
    resultado = 0
    for i in range(len(X)):
        resultado += (X[i] - Y[i])**2
    return np.float32(resultado**(1/2))

#within sum
def wSum(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    return soma

def mediaM(X, m, n, div):
    vetor = np.zeros(n, dtype = np.float32)
    for i in range(n):
        media = 0
        for j in range(m):
            media += X[j][i]
        vetor[i] = (media/div)
    return vetor

def Kmeans(X, m, n):
    centroides = np.zeros((m,n), dtype = np.float32)
    centroides_old = np.zeros((centroides.shape), dtype = np.float32)
    centroides_new = np.zeros((centroides.shape), dtype = np.float32)
    k = 2
    contador = 0
    QwSums = np.zeros(len(X))
    diferenca = np.zeros(len(X))
    paradaTotal = False
    while(paradaTotal == False):
        print(k)
        SumTotal = 0
        SumTotalOld = 0
        parada = False
        #criando centroides aleatórios
        for i in range(k):
            aleatorio = randint(0,len(X)-1)
            centroides[i] = X[aleatorio]
        while(parada == False):
            distancias = np.zeros((m,m), dtype = np.float32)
            #alocando as distancias entre cada vetor e cada centroide
            for i in range(k):
                for j in range(len(X)):
                    distancias[j][i] = distancia(X[j], centroides[i])
            
            for i in range(k):
                div = 0
                elementos = np.zeros((m,n), dtype = np.float32)
                clusters = np.zeros(len(X))
                for j in range(m):
                    if(min(distancias[j][0:k]) == distancia(X[j], centroides[i])):
                        elementos[j] = X[j]
                        div += 1
                if(div == 0):
                    div +=1
                centroides_new[i] = mediaM(elementos, m, n, div)
            
            for i in range(m):
                clusters[i] = min(distancias[i][0:k])
            
            SumTotal = wSum(clusters)
            #print(clusters, "clusters")
            dif = SumTotalOld - SumTotal
            if(dif >= 0):
                if(dif <= 0.1):
                    parada = True
                    contador+=1

            SumTotalOld = SumTotal
            #tranformando o atual em old
            centroides_old = copy.deepcopy(centroides)
            #transformando o new em atual

            #print(centroides)
            centroides = copy.deepcopy(centroides_new)
        QwSums[k-2] = SumTotal
        print("WSUM", SumTotal)
        k +=1
        if(contador >= 2):
            print("oi")
            diferenca[contador-2] = (QwSums[contador -2] - QwSums[contador - 1])
        if(contador > 2):
                if(diferenca[contador-2] < (2/100)* QwSums[contador - 1] ):
                    paradaTotal = True
    return centroides_old[:][0:k-1]

def relacionaCentroidsMatrix(centroides, matrix):
    arq = open("resultadoKmeans.txt", "w")
    distancias = np.zeros((len(matrix),len(centroides)), dtype = np.float32)
    for i in range(len(centroides)):
        for j in range(len(matrix)):
            distancias[j][i] = distancia(matrix[j], centroides[i])
    for i in range(len(centroides)):
        np.set_printoptions(precision= 4)
        n = i - 1
        k = len(centroides)
        m = len(matrix)
        arq.write("\nCluster ")
        arq.write(str(n+2))
        arq.write("\n")
        arq.write(str(centroides[i]))
        arq.write("\n")
        for j in range(m):
            if(min(distancias[j][0:k]) == distancia(matrix[j], centroides[i])):
                arq.write(str(np.array(matrix[j])))
                arq.write("\n")
print("primeira parte ok")
relacionaCentroidsMatrix(Kmeans(matrixA, 5165, 5), matrixB)