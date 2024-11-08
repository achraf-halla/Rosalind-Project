# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:38:00 2024

@author: user
"""

from Helper_Functions import read_fasta

s = read_fasta("rosalind_kmp.txt")[0]

def shorten_motif_search(s):
	"""
	Given: A DNA string s (of length at most 100 kbp) in FASTA format.
	Return: The failure array of s.
	 """
	A = [0] * len(s)
	
	index = 1
	length = 0
	
	while index < len(s):
		if s[index] == s[length]:
			length += 1
			A[index] = length
			index += 1
		else:
			if length == 0:
				A[index] = 0
				index += 1
			else:
				length = A[length - 1]
	with open("resulo.txt", "w") as f :
            f.write(" ".join([str(x) for x in A]))

shorten_motif_search(s)

            
