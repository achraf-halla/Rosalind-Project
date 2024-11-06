# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:03:47 2024

@author: user
"""

MOD = 1_000_000

memo = {}

def r_complem(base1, base2):
    return     (base1, base2) in {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}


def count_non_crossing_matchings(s):
    if s in memo:
        return memo[s]
    
    if len(s) == 0 or len(s) == 1:
        return 1
    
    count = 0
    
    for k in range(1, len(s), 2):
        if r_complem(s[0], s[k]):
            left_part = s[1:k]
            right_part = s[k+1:]
            count_left = count_non_crossing_matchings(left_part)
            count_right = count_non_crossing_matchings(right_part)
            count = (count + count_left * count_right) % MOD
    
    memo[s] = count
    return count

rna_string = "CGGCCGUAGGCGACGUCGCGCGCGGCGCCCAUCACGGCUUCGCGCGACGGAAGGGCAUGCUUCGAAAAUAUAUAUUACGUUAGCUUAACAAAGCUAUCACGUGUUUGCACGCCCCGUAGUUAUCGAAUUCGCCAUGGAGCUCGAAUACGCCGGGGGACAAUUGCCGGCGUUACAUCCGGCCCCGGAUGCGUAUAAUAUCGCGUAUUAUAUAUAUCCGGCGCGACGCGCGUUAAUAUGCAAUUCGAUACGCGCGCGUUUUAAAGCGCAU"
result = count_non_crossing_matchings(rna_string)
print(result)
