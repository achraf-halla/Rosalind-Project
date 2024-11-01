# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:04:34 2024

@author: user
"""
from Bio import SeqIO
from Bio.Seq import Seq
from structures import *
def dna_to_rna(dna):
    return dna.replace('T', 'U')

def reverse_complement(dna):
    mapp = str.maketrans("ATCG", "TAGC")
    return dna.translate(mapp)[::-1]

def translate_dna(dna):
    """Translates a DNA sequence into an amino acid sequence until a stop codon is reached."""
    protein = []
    
    for i in range(0, len(dna) - 2, 3): 
        codon = dna[i:i+3]

        amino_acid = DNA_Codons[codon]

        protein.append(amino_acid)
    return ''.join(protein)

def translate_rna(rna):
    """Translates a DNA sequence into an amino acid sequence until a stop codon is reached."""
    protein = []
    
    for i in range(0, len(rna) - 2, 3):  
        codon = rna[i:i+3]

        amino_acid = RNA_Codons[codon]

        protein.append(amino_acid)
    return ''.join(protein)

def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences
