# -*- coding: cp1251 -*-
from itertools import *
import numpy as np


def knapsack(C, weight, cost, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(cost[i - 1] + K[i - 1][j - weight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K


items = ['в', 'п', 'б', 'а', 'и', 'н', 'т', 'о', 'ф', 'д', 'к', 'р']
values = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
weights = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]
capacity = 8
minus = 0
ans_value = 0
ans = []
init_points = 15
count = len(values)

K = knapsack(capacity, weights, values, count)

i, j, total = count, capacity, 0
res = K[count][capacity]
while i > 0 and res > 0:
    if res != K[i - 1][j]:
        for w in range(weights[i - 1]):
            ans.append(items[i - 1])
        total += weights[i - 1]
        res -= values[i - 1]
        j -= weights[i - 1]
    i -= 1
for i in range(count):
    if items[i] not in ans:
        minus += values[i]
    else:
        ans_value += values[i]
ans = np.array([ans])
print(np.reshape(ans, (2, 4)))
print("final survival points: ", ans_value + init_points - minus)