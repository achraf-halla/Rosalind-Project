# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:27:20 2024

@author: user
"""

from  math import factorial


n = 91
k = 8


def partial_permuate(n,k):
    """
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

    """
    return int((factorial(n) / factorial(n-k)) % 1000000)

partial_permuate(n,k)
