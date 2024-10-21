# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:01:54 2024

@author: user
"""

s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
from structures import *
def translate_to_protein(seq) :
        seq = seq.replace("U" , "T")
        return "".join([DNA_Codons[seq[k:k +3]] for k in range(0,len(seq)-1, 3)])
translate_to_protein(s)
