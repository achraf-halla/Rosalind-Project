# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:55:52 2024

@author: user
"""

import math
from itertools import permutations

n = 7



def permuate(n):
    """
    Generate all permutations of numbers from 1 to n and save them to a file.

    Args:
        n (int): The length of the permutation, where permutations are generated from numbers 1 to n.

    Saves:
        A file named "permutations_k.txt" containing all permutations of length `n` and the total number of permutations.
    """
    perma = list(permutations(range(1, n + 1)))
    with open("permutations_k.txt", "w") as f:
        f.write(f"The total number of permutations of length {n} is: \n{len(perma)}\n")
        for perm in perma:
            f.write(" ".join(map(str, perm)) + "\n")
    


     
permuate(n)
        