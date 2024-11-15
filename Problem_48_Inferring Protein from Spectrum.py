# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:37:09 2024

@author: user
"""

from structures import MonoisoMass_Table
MonoisoMass_Table = {k:round(v,2) for (k,v) in MonoisoMass_Table.items()}
def read_mass(file):
    with open(file,"r") as f :
        lines = f.readlines()
    return [float(line.strip()) for line in lines if line.strip()]
        
def get_key(val):
  
    for key, value in MonoisoMass_Table.items():
        if val == value:
            return key

    return False

def infer_protein(L):
    protein = ""
    for i in range(len(L)-1):
        
        amino =  get_key(round(abs(L[i]-L[i+1]),2))
        if amino :
            protein += amino
        
    return protein

ex = read_mass("rosalind_spec.txt") 

infer_protein(ex)
