# -*- coding: utf-8 -*-

# -- Sheet --

import  matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,2.0,0.01)
s = 1+np.sin(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas (s)', ylabel='napięcie prądu (mv)', title='pomiar prądu w czasie...')
ax.grid()
fig.savefig('wykres.png')
plt.show()

x = np.arange(14)
y = np.sin(x/2)

plt.step(x,y+2,label='pre(domyślny)')
plt.plot(x,y+2,'o--',color='grey',alpha=0.3)

plt.step(x,y+1,label='mid')
plt.plot(x,y+1,'o--',color='grey',alpha=0.3)

plt.step(x,y,label='post')
plt.plot(x,y,'o--',color='grey',alpha=0.3)



plt.grid(axis='x',color='0.95')
plt.legend(title='Parametr:')
plt.title('wartości: pre,mid,post')
plt.show()

#wyświetlanie wielu wykresów na jednej figurze
#przygotowanie danych
x1 = np.linspace(0.0,5.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
x2 = np.linspace(0.0,2.0)
y2 = np.cos(2*np.pi*x2)

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle('Dwa wykresy w jednej figurze...')

ax1.plot(x1,y1,'o-')
ax1.set_ylabel('drgania tłumione')

ax2.plot(x2,y2,'.-')
ax2.set_xlabel('czas (s)')
ax2.set_ylabel('drgania nietłumione')

plt.show()

plt.style.use('fivethirtyeight')

x = np.linspace(0,10)
np.random.seed(196808001)
fig,ax = plt.subplots()

ax.plot(x,np.sin(x)+x+np.random.randn(50))
ax.plot(x,np.sin(x)+0.5*x+np.random.randn(50))
ax.plot(x,np.sin(x)+2*x+np.random.randn(50))
ax.plot(x,np.sin(x)-0.5*x+np.random.randn(50))
ax.plot(x,np.sin(x)-2*x+np.random.randn(50))
ax.plot(x,np.sin(x) + np.random.randn(50))
ax.set_title("styl: fivethirtyeight")
plt.show()

