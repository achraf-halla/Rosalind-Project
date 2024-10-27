# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:04:34 2024

@author: user
"""

from structures import *
def dna_to_rna(dna):
    """Converts a DNA sequence to an RNA sequence by replacing 'T' with 'U'."""
    return dna.replace('T', 'U')

def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    mapp = str.maketrans("ATCG", "TAGC")
    return dna.translate(mapp)[::-1]

def translate_dna(dna):
    """Translates a DNA sequence into an amino acid sequence using DNA codons."""
    protein = []
    
    for i in range(0, len(dna) - 2, 3): 
        codon = dna[i:i+3]
        amino_acid = DNA_Codons[codon]
        protein.append(amino_acid)
    return ''.join(protein)

def translate_rna(rna):
    """Translates an RNA sequence into an amino acid sequence using RNA codons."""
    protein = []
    
    for i in range(0, len(rna) - 2, 3):  
        codon = rna[i:i+3]
        amino_acid = RNA_Codons[codon]
        protein.append(amino_acid)
    return ''.join(protein)

def parse_fasta(fasta_data):
    """Parses a FASTA formatted string and returns the DNA sequence without headers."""
    lines = fasta_data.strip().splitlines()
    dna_sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return dna_sequence
