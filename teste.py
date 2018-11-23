import numpy as np

Vetor = [120, 100, 70, 69]
dif = [0,0,0]
for i in range(3):
    dif[i] = Vetor[i] - Vetor[i+1]

for i in range(2):
    if(dif[i]> 5*dif[i+1]):
        print("para")
