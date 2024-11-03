# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:18:59 2024

@author: user
"""



from math import factorial
string = "ACCCUGUGUGUAAGCUAAGCCUGGGAGCUGACUUCGAUAAGCUUCUAGUCUGAACCAUUUAACACCCGGAGUGUGACA"




def perfect_matching(string):
    AU = 0
    CG = 0
    for n in string :
        if n == "A":
            AU += 1
        elif n == "C":
            CG += 1
    return factorial(AU) * factorial(CG)

perfect_matching(string)
