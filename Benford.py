import csv
import numpy as np
import pandas as pd
import math as mt

#pegar o vetor do banco de dados
arq = open("vetor.txt", "r")
vetorB = pd.read_table("vetor.txt", delim_whitespace= True, header= None, thousands='.', dtype= np.float32)
vetorB = vetorB.values

def benford(vetor, tol):
    vBenford = np.zeros(10)
    Qnum = np.zeros(10)
    Qresult = np.zeros(10)
    n = len(vetor)
    Qdif = np.zeros(10)
    discrepancia = np.zeros(10)
    comparacao = 0
    for i in range(1,10):
        vBenford[i] = mt.log10(1+1/i)

    for i in range(n):
        while(vetor[i] > 9):
            vetor[i] = int((vetor[i]/10))
        if(vetor[i] < 1):
            if(vetor[i] != 0):
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
        Qresult[i] = Qnum[i]/n
    
    for i in range(1,10):
        Qdif[i] = abs(Qresult[i] - vBenford[i])
        print("Benford",i, ":",'{:.4f}'.format(vBenford[i]))
        print("Resultado :", '{:.4f}'.format(Qresult[i]))
        print("Diferenca :", '{:.4f}'.format(Qdif[i]))
        print("-----------------------------")
    
    print("Tolerancia : ", tol,"%")
    discrepancia = max(Qdif)
    for i in range(10):
        if(Qdif[i] == discrepancia):
            print("\nMaior diferenca encontrada foi no Benford", i,":", '{:.4f}'.format(discrepancia))    
    for i in range(1,10):
        if(Qdif[i] > tol/100):
            comparacao +=1
    if(comparacao == 0):
        print("Satisfaz Benford")
    else:
        print("\nNao satisfaz Benford com a tolerancia passada")

print("Esse programa avalia um banco de dados e retorna se o benford,", 
        "com a tolerancia passada, eh satisfeito ou nao.")

tolerancia = int(input("\nDigite 1 se quiser usar a tolerancia padrao = 5%, ou digite 2 se quiser passar uma tolerancia especifica: "))
if(tolerancia == 1):
    benford(vetorB, 5)
elif(tolerancia == 2):
    tolerancia1 = int(input("\nDigite sua tolerancia: "))
    benford(vetorB, tolerancia1)
    
        




