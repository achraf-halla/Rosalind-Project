# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:38:45 2024

@author: user
"""

def analyze_fasta(filepath):
    """
    Reads a FASTA file, calculates the GC content for each sequence, 
    and identifies the sequence with the highest GC content.
    
    Args:
        filepath (str): The path to the FASTA file.
        
    Returns:
        tuple: A tuple containing the label of the sequence with the highest GC content 
               (excluding the '>' character) and its GC content percentage.
    """
    def readfile(filepath):
        with open(filepath, "r") as f:
            return [l.strip() for l in f.readlines()]

    def gc_content(seq):
        return round((seq.count("C") + seq.count("G")) / len(seq) * 100, 6)

    FASTAFile = readfile(filepath)
    FASTadic = {}
    FASTAlabel = ""

    for line in FASTAFile:
        if ">" in line:
            FASTAlabel = line
            FASTadic[FASTAlabel] = ""
        else:
            FASTadic[FASTAlabel] += line
            
    FASTADIC = {key: gc_content(value) for (key, value) in FASTadic.items()}
    max_cg = max(FASTADIC, key=FASTADIC.get)

    return (max_cg[1:], FASTADIC[max_cg])

# Example usage
result = analyze_fasta("inp.txt")
print(f"{result[0]}\n{result[1]}")
