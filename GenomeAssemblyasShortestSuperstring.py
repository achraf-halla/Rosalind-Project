# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:53:36 2024

@author: user
"""

from Helper_Functions import *

def find_overlap(s1, s2, min_overlap):
    start = 0
    while True:
        start = s1.find(s2[:min_overlap], start)  
        if start == -1:
            return 0
        if s1[start:] == s2[:len(s1) - start]:
            return len(s1) - start
        start += 1

def shortest_superstring(strings):
    min_overlap = len(strings[0]) // 2  

    while len(strings) > 1:
        max_len = -1
        best_pair = (0, 0)
        merged_string = ""

        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    overlap_len = find_overlap(strings[i], strings[j], min_overlap)
                    if overlap_len > max_len:
                        max_len = overlap_len
                        best_pair = (i, j)
                        merged_string = strings[i] + strings[j][overlap_len:]

        i, j = best_pair
        strings[i] = merged_string
        strings.pop(j)
    with open("longstring.txt", "w") as file:
        file.write(strings[0])





filename = "rosalind_long.txt" 
strings = read_fasta(filename)
