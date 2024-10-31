# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:50:05 2024

@author: user
"""
from itertools import product

def organize_strings(alphabet, n):
       """
    Generate all lexicographic strings of a given length from a specified alphabet and save them to a file.

    Args:
        alphabet (str): A string of characters representing the alphabet to use for generating strings.
        n (int): The desired length of the generated strings.

    Saves:
        A file named "lexicographic_list.txt" containing all possible lexicographic strings of length `n` formed from the alphabet.
        The file also includes the total number of generated strings.
    
    """
    combinations = list(product(alphabet, repeat=n))
    lexicographic_list = [''.join(comb) for comb in combinations]
    
    with open("lexicographic_list.txt", "w") as f:
        f.write(f"All strings of length {n}that can be formed from the alphabet is: \n")
        for string in lexicographic_list:
            f.write(f"{string} \n")
    


alphabet = ['A', 'B', 'C', 'D']  
n = 4
organize_strings(alphabet, n)

