# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:01:54 2024

@author: user
"""

s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
from structures import *
def translate_to_protein(seq) :
    """
    Translates an RNA or DNA nucleotide sequence into a protein sequence by converting 
    each codon (group of three nucleotides) into its corresponding amino acid.

    Parameters:
    -----------
    seq : str
        The RNA or DNA sequence to translate, where "U" in RNA is converted to "T" for DNA.
    
    Returns:
    --------
    str
        The translated protein sequence as a string of amino acids.
    """
        seq = seq.replace("U" , "T")
        return "".join([DNA_Codons[seq[k:k +3]] for k in range(0,len(seq)-1, 3)])
translate_to_protein(s)
