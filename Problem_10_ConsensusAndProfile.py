# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:38:45 2024

@author: user
"""

def readfile(filepath):
    """
    Reads a file and returns each line as an element in a list, stripped of any 
    leading or trailing whitespace.

    Parameters:
    -----------
    filepath : str
        Path to the file to be read.
    
    Returns:
    --------
    list of str
        A list containing each line from the file as a separate string.
    """
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
    """
    Constructs a profile matrix representing the nucleotide frequencies at each position 
    across multiple DNA sequences.

    Parameters:
    -----------
    sequences : list of str
        A list of DNA sequences to build the profile matrix from.
    
    Returns:
    --------
    dict of list of int
        A dictionary with keys 'A', 'C', 'G', and 'T', where each value is a list of counts 
        for the respective nucleotide at each position across the sequences.
    """
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
    """
    Generates a consensus string from a profile matrix by selecting the most frequent 
    nucleotide at each position.

    Parameters:
    -----------
    profile : dict of list of int
        The profile matrix containing nucleotide counts at each position.
    
    Returns:
    --------
    str
        The consensus string, representing the most common nucleotide at each position.
    """
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
    """
    Computes both the consensus string and the profile matrix for a set of DNA sequences.

    Parameters:
    -----------
    sequences : list of str
        A list of DNA sequences to analyze.
    
    Returns:
    --------
    tuple
        A tuple containing:
        - consensus (str): The consensus sequence.
        - profile (dict): The profile matrix with nucleotide frequencies per position.
    """
    profile = build_profile_matrix(sequences)
    consensus = build_consensus_string(profile)
    return consensus, profile

consensus, profile = consensus_and_profile(sequences)
print(consensus)
for nucleotide in "ACGT":
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
