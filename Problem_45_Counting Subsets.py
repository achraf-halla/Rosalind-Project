# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:38:42 2024

@author: user
"""

def count_subsets(n):
"""
    Given: A positive integer n (n≤1000).
    Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""
    return 2**n  % 1000000 

n= 878
count_subsets(n)
    
