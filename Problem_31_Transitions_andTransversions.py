# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:28:29 2024

@author: user
"""

from Helper_Functions import *

s, t = read_fasta("rosalind_tran.txt")

def transition_transversion_ratio(s, t):
    
    transitions = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    transversions = {('A', 'C'), ('A', 'T'), ('G', 'C'), ('G', 'T'),
                     ('C', 'A'), ('C', 'G'), ('T', 'A'), ('T', 'G')}
    transition_count = 0
    transversion_count = 0
    for base1, base2 in zip(s, t):
        if base1 != base2:
            if (base1, base2) in transitions:
                transition_count += 1
            elif (base1, base2) in transversions:
                transversion_count += 1


    return transition_count / transversion_count if transversion_count != 0 else float('inf')
    
transition_transversion_ratio(s, t)
