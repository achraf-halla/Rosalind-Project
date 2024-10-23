# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:00:03 2024

@author: user
"""

def dominant_allele_probability(k, m, n):
    total = k + m + n
    
   
    P_AA_AA = (k / total) * ((k - 1) / (total - 1))
    P_AA_Aa = (k / total) * (m / (total - 1)) * 2
    P_AA_aa = (k / total) * (n / (total - 1)) * 2
    P_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.75
    P_Aa_aa = (m / total) * (n / (total - 1)) * 0.5 * 2
    
    probability = P_AA_AA + P_AA_Aa + P_AA_aa + P_Aa_Aa + P_Aa_aa
    
    return probability


k = 2 
m = 2
n = 2
print(dominant_allele_probability(k, m, n))
