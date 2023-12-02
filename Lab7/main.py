import numpy as np
import matplotlib.pyplot as plt
from math import *
from random import randint
import time
import scipy


lst1 = [randint(0, 100) for i in range(1000000)]
lst2 = [randint(0, 100) for i in range(1000000)]
np_lst1 = np.array(lst1)
np_lst2 = np.array(lst2)

t_start = time.perf_counter()
np.multiply(lst1, lst2)
time_lst = time.perf_counter() - t_start
print(time_lst)

t_start = time.perf_counter()
np.multiply(np_lst1, np_lst2)
time_np = time.perf_counter() - t_start
print(time_np)


data = np.genfromtxt('data1.csv', delimiter=';')
fourth = []
fifth = []
for row in data:
    try:
        fourth.append(int(row[3]))
        fifth.append(int(row[4]))
    except:
        continue
t = np.arange(0, len(fifth))

slope, intercept, r, p, stderr = scipy.stats.linregress(fourth, fifth)

plt.subplot(311)
plt.plot(t, fourth, 'g', t, fifth, 'r', t, intercept + slope * t, 'b')
plt.legend(["Положение дроссельной заслонки (%)", "Обороты двигателя (об/мин)", 'График корреляции'])
plt.xlabel('Время, сек.') 
plt.title('Все вместе', fontweight="bold")

plt.subplot(312)
plt.plot(t, fourth)
plt.xlabel('Время, сек.') 
plt.ylabel('%') 
plt.title('Положение дроссельной заслонки', fontweight="bold")

plt.subplot(313)
plt.plot(t, fifth)
plt.xlabel('Время, сек.') 
plt.ylabel('об/мин') 
plt.title('Обороты двигателя', fontweight="bold")

plt.tight_layout()
plt.show()


fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')
x = np.linspace(-pi, pi)
y = x
z = np.tan(x)
ax_3d.plot(x, y, z)
plt.show()