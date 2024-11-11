# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:41:26 2024

@author: user
"""
from Helper_Functions import read_fasta
from math import factorial

string =  read_fasta("ina.txt")[0]



def max_matching(string):
     """
     Given: An RNA string s of length at most 100.

     Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
     """
     A, U = string.count("A"),  string.count("U")
     C, G =  string.count("C"),  string.count("G")

     return  factorial(max(A,U)) // factorial(max(A,U)- min(A,U)) * factorial(max(C,G)) // factorial(max(C,G)-min(C,G)) 
max_matching(string)
