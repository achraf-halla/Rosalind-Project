# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:06:01 2024

@author: user
"""

from math import exp

def motif_probability(N, x, s):
    AT = 0 
    GC = 0  
    for nt in s:
        if nt in 'AT':
            AT += 1
        elif nt in 'GC':
            GC += 1
    
    s_prob = (((1 - x) / 2) ** AT) * ((x / 2) ** GC)
    
    prob = 1 - exp(-s_prob * N)
    return prob

N = 86725 
x = 0.504875
s = "CTTACCCG"

result = motif_probability(N, x, s)
print(round(result, 3))
