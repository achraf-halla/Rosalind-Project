# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:38:45 2024

@author: user
"""

def readfile(filepath):
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
    
from collections import defaultdict


FASTAFile = readfile("dna_strands.txt")

sequences = []
current_seq = ""
import pandas as pd
for line in FASTAFile :
        if line.startswith(">"):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ""
        else:
            current_seq += line
if current_seq:
    sequences.append(current_seq)
def build_profile_matrix(sequences):
    length = len(sequences[0])
    profile = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length
    }
    
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
    return profile

def build_consensus_string(profile):
    consensus = []
    for i in range(len(profile['A'])):
        max_count = 0
        max_nucleotide = ""
        for nucleotide in "ACGT":
            if profile[nucleotide][i] > max_count:
                max_count = profile[nucleotide][i]
                max_nucleotide = nucleotide
        consensus.append(max_nucleotide)
    return "".join(consensus)

def consensus_and_profile(sequences):
    profile = build_profile_matrix(sequences)
    consensus = build_consensus_string(profile)
    return consensus, profile

consensus, profile = consensus_and_profile(sequences)
print(consensus)
for nucleotide in "ACGT":
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
