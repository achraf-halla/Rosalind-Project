# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:28:00 2024

@author: user
"""

from Helper_Functions import *
sequences = read_fasta("rosalind_corr.txt")
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
def correct_reads(sequences):
    """
    Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s
             in the dataset, one of the following applies:

             *** s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
             *** s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).

             
    Return: A list of all corrections in the form "[old read]->[new read]". 
    """
    
    correct_seq = [x for x in sequences if sequences.count(x) > 1 or Seq(x).reverse_complement()  in sequences]
    incorrect_seq = [x for x in sequences if x not in correct_seq]
        
    corrections = []
    for read in incorrect_seq:
        for correct in correct_seq:
            if hamming_distance(read, correct) == 1:
                corrections.append(f"{read}->{correct}")
                break
            elif hamming_distance(read, reverse_complement(correct)) == 1:
                corrections.append(f"{read}->{reverse_complement(correct)}")
                break

    with open("correction.txt", "w") as f:
        for x in corrections :
            f.write(f"{x}\n")
correct_reads(sequences)

