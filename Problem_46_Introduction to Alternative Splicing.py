# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:42:26 2024

@author: user
"""

from math import factorial

def sum_combinations(n, m):
    """
Given: Positive integers n and m with 0≤ m≤ n≤2000.
Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000.
    """
    result = 0
    MOD = 10**6 
    while m <= n:
        result += factorial(n) // (factorial(m) * factorial(n - m)) % MOD
        result %= MOD  
        m += 1
    return result

n = 1967 
m = 1036
print(sum_combinations(n, m))
