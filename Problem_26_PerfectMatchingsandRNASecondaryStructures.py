# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:18:59 2024

@author: user
"""



from math import factorial
string = "ACCCUGUGUGUAAGCUAAGCCUGGGAGCUGACUUCGAUAAGCUUCUAGUCUGAACCAUUUAACACCCGGAGUGUGACA"




def perfect_matching(string):
    """
Given: An RNA string s
 of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

    """
    AU = 0
    CG = 0
    for n in string :
        if n == "A":
            AU += 1
        elif n == "C":
            CG += 1
    return factorial(AU) * factorial(CG)

perfect_matching(string)
