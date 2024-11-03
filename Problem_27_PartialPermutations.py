# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:27:20 2024

@author: user
"""

from  math import factorial


n = 91
k = 8


def partial_permuate(n,k):
    return int((factorial(n) / factorial(n-k)) % 1000000)

partial_permuate(n,k)
