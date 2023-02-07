# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np

np.zeros(6)

# 


ar = np.ones(10)
ar

u = np.arange(1,56,3)
u

k = np.linspace(0,10,num=5)
k

lista = np.array([23,7,8,9,12,15,0,-77,78,99,-1,0,56,235,8])
lista

print(type(lista))

print(lista[7])

print(lista[2:6])

print(lista[4:])

print(lista[:7])

print(lista[:len(lista)-2])

print(lista[1::2])

print(lista[::-1])

#macierz wartości
w = np.array([[1,2,4,5],[8,7,6,11],[12,18,20,23]])
w

ln = list([[1,2,4,5],[8,7,6,11],[12,18,20,23]])
ln

print(w[w<5])

pc = (w>=5)
print(w[pc])

pr = w[w%2==0]
print(pr)

c= w[(w>2) & (w<=15)]
print(c)

v = w[(w<=7) | (w>20)]
print(v)

lt = np.arange(1,25)
lt

mt = lt.reshape(4,6)
mt

dane = np.array([1,3,7])

ones = np.ones(3,dtype=int)
tw = np.array([2,2,2])

#operacje na macierzach
print(dane+ones)

print(dane*tw)

l1 = [2,3,4]
l2 = [5,6,7]
l = l1+l2
l

arr = tw+dane
arr

print(dane/tw)

tr= np.array([4,4,6,6])

print(tr+tw)

print(dane.sum())
print(dane.mean())
print(dane.var()) 

tab = np.array([[1,8],[23,9]])
tab

print(tab.sum(axis=0))
print(tab.sum(axis=1))

tab = tab*1.88
tab

print(tab.max())
print(tab.min())
print(tab.sum())

from io import StringIO

dane = u"1-2-3\n5-7-83\n240-923-4"

t = np.genfromtxt(StringIO(dane),delimiter="-")
t

dane = u"""#
#komentarz...
1, 2
45, 7
67, 1 #trzecia linia
9, 3
#pusta linia
10, 0
"""

p = np.genfromtxt(StringIO(dane),comments="#", delimiter=",")
p

