# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:55:52 2024

@author: user
"""

from structures import *
from Helper_Functions import *
from Bio.Seq import Seq

def find_orfs(dna_seq):
        """
    Identify and return all open reading frames (ORFs) in a given DNA sequence.

    Args:
        dna_seq (Bio.Seq.Seq): A DNA sequence object (from the BioPython library) for which to find ORFs.

    Returns:
        set: A set of unique protein sequences (as strings) translated from all ORFs found in the DNA sequence.

       """
    proteins = set() 
    reverse_complement = dna_seq.reverse_complement()
    for strand in [dna_seq, dna_seq[1:], dna_seq[2:], reverse_complement, reverse_complement[1:],reverse_complement[2:]]:
            translated_seq = strand.translate(to_stop=False)
            protein_seq = ""
            inside_orf = False
            for i, aa in enumerate(translated_seq):
                if aa == 'M':
                    protein_seq = ""
                    for j in translated_seq[i:]:
                        if j == '*':
                            proteins.add(protein_seq)
                            break
                        protein_seq += j

    return proteins







fasta_input = """>Rosalind_8263
TATTGCGGATACCGGGTTGTGTGAGTTGTATTGTAATTGCCTGTATTCGAGGCAGGGAAC
AGAGAAATCGCGCCCCGGCGGTTGTAAGGTCAGATCAACCCGTTATGACCGGGAAACGCC
CTATTGTGGTAGACTTATATTTTGAAACAGAAATCGTTTCGTGAGAGTGACGACGAGGGA
CAACCATGGTCAGCGGTAAGCAATCCACCTATAGCGAGAGCTTACCTTAATTAACTTCAA
GTCAAGATGACTATTACATCTGTGTGCGTTCTACTTCTCGAGAGAGACCTAGGATACCTA
GGTAATGCATGCAGCACAGTGTTAACCTCGGAATTGGCACCGTAGTCTTCCTCTAGGGGC
GTACATAAGGAGTGTTAGTCGCAAAGCAATGCATAGCTCGCGTCGTGATGGCGTAGCGGC
GATGTTGCCACAATATGAGCCCCTGCCATAACTATGGCAACTGTTGAGAGAATGCAAAGG
GCCTAGCTAGGCCCTTTGCATTCTCTCAACAGTTGCCATCAACAGGGACAGACAAGGGGG
CCCCCTAATTTCGAAACGAGATGCTGTAGGCCAAGTACAGCTAATAGGCATTGCTCTTAT
TGGCCTTCTAGCGTCAGCAGGGCCCATCGTCGGACAGTTCATCCACCCCTGGACTCAACA
TACAATGCCAAGATACGCGCGACAGAGTACTGCAGACTGTCACTATGGGCATCGGGTAAT
GTCCAGGTCGGTCTCTCAAATGTTTCTAACAACGCAAGGATACATCAAAATTGCTCCATC
GTTAGGAGCAGTGAGGATTCGGGCGCCCCATGAACACCTAGCAGGGGTTTGCACCCAGGT
TGACTAGAGGGCCTCCGATGATGAGCTTTCTGATCGGGTACGAAGCACGAACTGGTTCCG
CACAATATAAAGTATGCCCGGCTAGCCGCAGCCCGAGGAACTCTCTCACAACGGATGCTT
CCTGCTTAATTC
"""
dna_sequence = Seq(parse_fasta(fasta_input))
distinct_proteins = find_orfs(dna_sequence)

for protein in distinct_proteins:
    print(protein)
    
