# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:55:03 2024

@author: user
"""
def count_pt_Mutation(s,t) :
    return len([x for i, x in enumerate(s) if x != t[i]])


s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
result = count_pt_Mutation(s,t) 
print(result)
