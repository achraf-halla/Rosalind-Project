# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:41:26 2024

@author: user
"""
from Helper_Functions import read_fasta
from math import factorial

string =  read_fasta("ina.txt")[0]



def max_matching(string):
     A, U = string.count("A"),  string.count("U")
     C, G =  string.count("C"),  string.count("G")

     return  factorial(max(A,U)) // factorial(max(A,U)- min(A,U)) * factorial(max(C,G)) // factorial(max(C,G)-min(C,G)) 
max_matching(string)
