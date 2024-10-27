# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:55:03 2024

@author: user
"""
def count_pt_Mutation(s, t):
    """
    Counts the number of point mutations between two sequences.

    A point mutation is defined as a difference at a corresponding position 
    between two sequences of the same length.

    Args:
        s (str): The first sequence (reference).
        t (str): The second sequence (variant).

    Returns:
        int: The number of point mutations (positions where the sequences differ).
        
    Raises:
        ValueError: If the input sequences are not of the same length.
    """
    if len(s) != len(t):
        raise ValueError("The sequences must be of the same length.")

    return len([x for i, x in enumerate(s) if x != t[i]])

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
result = count_pt_Mutation(s,t) 
print(result)
