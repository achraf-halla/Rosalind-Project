# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:46:26 2024

@author: user
"""


from itertools import permutations, product

def signed_permutations(n):
    perms = permutations(range(1, n + 1))
    signed_perms = []
    for perm in perms:

        sign_combinations = product([-1, 1], repeat=n)
        for signs in sign_combinations:
            signed_perm = [sign * num for sign, num in zip(signs, perm)]
            signed_perms.append(signed_perm)
    
    count = len(signed_perms)

    with open("permutations_n.txt", "w") as f:
            f.write(f"{count}\n")
            for perm in signed_perms:
                f.write(" ".join(map(str, perm)) + "\n")
n = 6 
signed_permutations(n)

