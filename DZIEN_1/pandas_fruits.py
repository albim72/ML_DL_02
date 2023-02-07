import numpy as np
import pandas as pd

dane = {
    'jabłko':[3,2,7,0],
    'pomarańcza':[2,1,1,5],
    'kiwi':[0,0,2,1],
    'gruszka':[1,4,0,1]
}

fru = pd.DataFrame(dane)
print(fru)

fru = pd.DataFrame(dane, index=['Tadeusz','Nadia','Roman','Olga'])
print(fru)

fru.to_csv('fruits.csv')
print(fru.info())
