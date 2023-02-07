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

unsorted_df = pd.DataFrame(np.random.randn(13,3),index=[1,4,6,2,3,5,8,9,0,7,10,11,12],columns=['b','a','c'])
print(unsorted_df)

sorted_df = unsorted_df.sort_index()
print(sorted_df)

sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)

sorted_df = unsorted_df.sort_index(axis=1)
print(sorted_df)

sorted_df = unsorted_df.sort_values(by='a')
print(sorted_df)
