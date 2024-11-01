# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:58:53 2024

@author: user
"""

def expected_dom_offs(couples):
    """
    Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    
    exp_val = 2 * sum(couples[i] * probabilities[i] for i in range(6))
    
    return exp_val

couples = [19804 ,19513 ,18882 ,17918 ,19330 ,19932]

result = expected_dom_offs(couples)
print(result)
