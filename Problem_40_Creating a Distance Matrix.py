# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:47:19 2024

@author: user
"""

from Helper_Functions import *

sequences = read_fasta("rosalind_pdst.txt")

def Create_Dist_Matrix(sequences):
    def hamming_distance(chaine1, chaine2):
        return "{:.4f}".format(float(sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))/len(chaine1)))
    matrix = []
    for seq in sequences :
        a = []
        for com in sequences :
            a.append(str(hamming_distance(seq, com)))
            
        matrix.append(a)
            
    print(matrix)
    with open("rosa_result.txt", "w") as f:
        for x in matrix :
            f.write(" ".join(x) +"\n")
            
            
Create_Dist_Matrix(sequences)            
