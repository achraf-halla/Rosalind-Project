# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:50:05 2024

@author: user
"""
from itertools import product

def organize_strings(alphabet, n):
    combinations = list(product(alphabet, repeat=n))
    lexicographic_list = [''.join(comb) for comb in combinations]
    
    with open("lexicographic_list.txt", "w") as f:
        f.write(f"All strings of length {n}that can be formed from the alphabet is: \n")
        for string in lexicographic_list:
            f.write(f"{string} \n")
    


alphabet = ['A', 'B', 'C', 'D']  
n = 4
organize_strings(alphabet, n)

