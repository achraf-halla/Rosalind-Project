# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:59:41 2024

@author: user
"""

from structures import *
from Helper_Functions import *

def reverse_palindrome(fasta_data):
    """
    Finds all reverse palindromic substrings of lengths 4-12 in a DNA sequence.
    
    Parameters:
    fasta_data (str): A DNA string of length at most 1 kbp in FASTA format..
    
    Returns:
    None: Writes output of start position and length to "output_palind.txt".
    """
    string = parse_fasta(fasta_data)
    
    result = []
    low = 4
    while low <= 12:
         for i in range(len(string) - low + 1):
            substring = string[i:i + low]
            if substring == reverse_complement(substring):
                result.append((i + 1, low))
                 # Store 1-based index and length

         low += 1
    with open("output_palind.txt", "w") as f:
        for x in result :
            f.write(f"{x[0]} {x[1]}\n")
    
        



    
    
    
fasta_data = """>Rosalind_4479
GCGCTCCATAGAAGATGAAGTAGATAACCTTTCCTCTACATAACGACTTCTCTCCTTTTT
GAGACGTATTCAGCATTGACAGACCCCCAACTACTCGTGACGCCAAAGGGAGACTATGTG
GTCAAGGCACGTGACCTGGGTTTCCTGTTGAACGGCGAGTCTGGTCGTTTACCGGAGGTT
TCCAACCTTGGTTTAAAACAACACGAACGTGCGTCGGGTATTAGAGGATGGATTACATGA
TCCGGGGGTCCAATAACATACCCATCATGGCTATTACTCACGAACGTGTGTATTATCTCC
CTACCCTTTAATGAGGCTCATATCATGTGACACGGCCTCGGCCGGAGATGTGTACGTACA
TTTGCCTCAACACGAGTGTGACCGCGATCAATATTGACCTGGCAGGAACTTGTCTCGTCC
AATCATATGCACCGCTTCCTTTACGTCTAACCATCTATGAGCATGTACGTACATATCCAG
ATTCCGTCTCAGCACATAGACGAGCTAAAAAGAAGCAATAACACGGCAGCTGACTTTCAG
TTCATATCAACTCAGGATAGGAATTCTGGTAGCCCGCCACCAGCCGTTGATGATGTCCTG
GCATGGATCATTCCGTGGGGTGTAGACCTACTCATACGGAGTTCTAATAGAAGTGTTCTC
TTCTATCTTGGAGTACTTAGCGTGAGATTATATAAAGCCTGCGCGAGTGTCCTTGGATTC
CCCCCACTCCCAGTCTCGAAAGGCGATGAACTTGTATTCTGTCTTTTTCGGACACCTGTC
ATATCTATGGTCTCATGGTCGTACTCGACATGTGCATACGTACATTGCTTAGCAGCTAAA
GTCGATAGGCTCGCTCTTATTCGAACATGGAACGTTCCGAACCCTTAGGCGAGTGGCGTT
TTATTCTTTAAACCCTTGAAAGTCCCTAATATTATA"""

reverse_palindrome(fasta_data)