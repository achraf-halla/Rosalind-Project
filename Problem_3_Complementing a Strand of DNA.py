# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:39:13 2024

@author: user
"""

def Reverse_complement(seq):
    
    """ DNA -> reverse DNA Complement by replacing thymine with Adenine and cytosine with guanine (vice versa) then reversing it """
    mapp = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapp)[::-1]

string = "AAAACCCGGT"
result = Reverse_complement(string)
print(result == "ACCGGGTTTT")
