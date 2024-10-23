# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:16:05 2024

@author: user
"""

from math import comb

def prob_at_least_N_AaBb(k, N):

    total_offspring = 2 ** k
    p_AaBb = 1 / 4
    cumulative_prob = 0
    for x in range(N):
        prob = comb(total_offspring, x) * (p_AaBb ** x) * ((1 - p_AaBb) ** (total_offspring - x))
        cumulative_prob += prob
    
    result_prob = 1 - cumulative_prob
    return result_prob


k = 6 
N = 17  
result = prob_at_least_N_AaBb(k, N)
print(f"Probability of having at least {N} Aa Bb organisms in the {k}-th generation: {result:.6f}")
