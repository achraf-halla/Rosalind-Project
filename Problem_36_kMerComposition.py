# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:32:04 2024

@author: user
"""
from Bio import SeqIO
from Bio.Seq import Seq
def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences[0]
import re
from itertools import product
def k_mer_composition(s,k):
    """
    Given: A DNA string s in FASTA format (having length at most 100 kbp).
    Return: The 4-mer composition of s.
    """
    k_mers_count = {x:int(0) for x in sorted(["".join(x) for x in product("ACGT", repeat = 4)])}

    for i in range(len(s)-k+1):
        
        if s[i:i+k] in k_mers_count.keys() :
            kmer =  s[i:i+k]
            k_mers_count[kmer] += 1
            print(k_mers_count[kmer])
            
    with open("k_mer_result.txt", "w") as f :
        f.write(" ".join([str(v) for k,v in  sorted(k_mers_count.items(), key=lambda x: x[0])]))


s = read_fasta("rosalind_kmer.txt")
k = 4
k_mer_composition(s, k)
