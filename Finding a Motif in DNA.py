# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:23:32 2024

@author: user
"""

def find_substring_brute(s, t):
    positions = []
    for i in range(len(s) - len(t) + 1):  
        if s[i:i + len(t)] == t: 
            positions.append(str(i + 1))  
    return positions

s = "TAAGCTAGTAGCTAGTAGCTAGTCTCAGCTAGTTTAGCTAGTGAAGCTAGTAGCTAGTTCGATCAAGCTAGTAGCTAGTGAGAGCTAGTGTAGCTAGTAGCTAGTAATCACAGCTAGTCGAAGCTAGTTTGCCTAGCTAGTCGAAATCCGCAGCTAGTAGCTAGTAGCTAGTAAAGAAGCTAGTTTGAAGCTAGTAGCTAGTGAACCTAGCTAGTAGCTAGTAGCTAGTAGCTAGTAGCTAGTAAGCTAGTAGCTAGTAGCTAGTAAGCTAGTAGCTAGTTAGCTAGTCGCGAGCTAGTGAGCGAGCTAGTAGCTAGTAGCTAGTATCCGATCCCAGATAGCTAGTAACGAAAGATAGCTAGTCAGCTAGTCTATATAGCTAGTGCTCCTAGCTAGTCAGCTAGTTGAGCTAGTAGTAGCTAGTTACTTAGCTAGTAAGCTAGTAGCTAGTGAGCTAGTCCAGCTAGTAGAGCTAGTAGCTAGTCCGAAGCTAGTGAGCTAGTAGCTAGTGGCGTTAGCTAGTTTATAGCTAGTATAGCTAGTGCCCAGCTAGTAGCTAGTACTAGAAGCTAGTAGCTAGTTGAGCTAGTAAGCTAGTAAGCTAGTTTAGCTAGTAGCTAGCTAGTTAGCTAGTTAGCAAGCTAGTCAGCTAGTTAGCTAGTCGAATAGCGAGCTAGTAAGCTAGTTGTAGCTAGTAGCTAGTGCCAGCTAGTCCTGAAGCTAGTCCAGCTAGTAGAGCTAGTCTCTAGCTAGTGAGCTAGTCAATAAGCTAGTAAAAAGCTAGTAGCTAGTGGCAGCTAGTAGCTAGTAAGCTAGTAAGCTAGTTGATGGAATTGAAAGGTCAGCTAGTTCGGTGCTAGCTAGTAATCGAGCTAGTCTAAGAAGCTAGTAGCTAGT"
t = "AGCTAGTAG"
result = find_substring_brute(s, t)
print(" ".join(result))
