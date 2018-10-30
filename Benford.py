import csv
import numpy as np
import pandas as pd
import math as mt

#pegar o vetor do banco de dados
reader = csv.reader(open("vetor.csv", "r"))
x = list(reader)
vetorB = np.array(x).astype("float")

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

