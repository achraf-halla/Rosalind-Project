# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:44:02 2024

@author: user
"""

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    
    F1, F2 = 1, 1
    
    for i in range(3, n + 1):
        Fn = F2 + k * F1
        F1, F2 = F2, Fn
    
    return F2

n = 5
k = 3
print(rabbit_pairs(n, k))  