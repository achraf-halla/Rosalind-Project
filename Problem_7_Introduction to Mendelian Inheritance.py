# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:00:03 2024

@author: user
"""

def dominant_allele_probability(k, m, n):
    """
    Calculates the probability of an offspring having a dominant allele in a randomly selected pair
    from a population consisting of organisms with three genotypes: homozygous dominant (AA),
    heterozygous (Aa), and homozygous recessive (aa).

    Parameters:
    -----------
    k : int
        The number of homozygous dominant (AA) individuals in the population.
    m : int
        The number of heterozygous (Aa) individuals in the population.
    n : int
        The number of homozygous recessive (aa) individuals in the population.

    Returns:
    --------
    float
        The probability that a randomly chosen pair from the population will produce an offspring 
        with at least one dominant allele (AA or Aa genotype)."""
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
