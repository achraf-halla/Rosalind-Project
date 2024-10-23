# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:38:45 2024

@author: user
"""

def readfile(filepath):
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
    
def gc_content(seq):
    
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100,6)

FASTAFile = readfile("inp.txt")

FASTadic = {}
FASTAlabel = ""

for line in FASTAFile :
    if ">" in line :
        FASTAlabel = line
        FASTadic[FASTAlabel] = ""
    else :
        FASTadic[FASTAlabel] += line
        
FASTADIC = {key : gc_content(value) for (key, value) in FASTadic.items()}
max_cg = max(FASTADIC , key = FASTADIC.get )

print(f"{max_cg[1:]}\n{FASTADIC[max_cg]}")
