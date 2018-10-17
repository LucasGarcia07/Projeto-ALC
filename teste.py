import csv
import numpy as np
import pandas as pd

reader = csv.reader(open("teste.csv", "r"), delimiter=",")
x = list(reader)
matrizA = np.array(x).astype("float")

print(result[:][0])

