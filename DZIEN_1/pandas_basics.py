# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

sr = pd.Series([1,2,8,np.nan,17,9])
sr

daty = pd.date_range("20230207",periods=6)
daty

df = pd.DataFrame(np.random.rand(6,4),index=daty,columns=list("ABCD"))
df

s= "lajkonik"
print(s)

print(s[0])
print(s[2])
print(s[2:5])
print(s[4:])

df.head(3)

df.tail(2)

df.index

df.columns

e = df.to_numpy()
e

print(type(df))
print(type(e))

df.describe()

e.describe()

df.T

df.sort_index(axis=1,ascending=False)

df.sort_values(by="B")

df["A"]

df[0:3]

df["20230208":"20230210"]

df.iloc[3]

df.iloc[3:5,0:2]

df.iloc[[1,2,4],[0,2]]

df.iloc[1,1]

df[df["A"]>0.3]

df2 = df.copy()

df2["E"] = ["pierwszy","drugi","trzeci","pierwszy","trzeci","pierwszy"]

df2

df2[df2["E"].isin(["pierwszy","trzeci"])]

df.to_csv('dane.csv')

dnframe = pd.read_csv('dane.csv')

dnframe

dnframe = pd.read_csv('dane.csv',index_col=0)

dnframe

