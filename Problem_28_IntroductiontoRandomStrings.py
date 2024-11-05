# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:13:00 2024

@author: user
"""

from math import log10

def calculate_gc_content_probabilities(s, A):
    count_A = s.count('A')
    count_T = s.count('T')
    count_C = s.count('C')
    count_G = s.count('G')
    
    results = []
    
    for x in A:
        P_C = P_G = x / 2
        P_A = P_T = (1 - x) / 2
        P_s = (P_A ** count_A) * (P_T ** count_T) * (P_C ** count_C) * (P_G ** count_G)
        
        if P_s > 0:
            log_probability = log10(P_s)
        else:
            log_probability = float('-inf') 
        
        results.append(log_probability)
    
    return " ".join(str(x) for x in results)

dna_string = "CACGGGCAAGACCCCTTGCCTGTTAGCATTCATCCGTATACTATGCGGTAAAGTAAGGGGACATGACGATTGCCCTGATCTAGAAGATCGAAGCTAT"
A = [float(x) for x in ("0.103 0.119 0.169 0.226 0.330 0.363 0.443 0.456 0.502 0.591 0.628 0.707 0.756 0.829 0.873 0.942".split(" "))]
result = calculate_gc_content_probabilities(dna_string, A)

print(result)
