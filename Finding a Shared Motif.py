# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:52:01 2024

@author: user
"""

def readfile(filepath):
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
    
FASTAFile = readfile("dna_strands.txt")


def create_Fasta_Dic(FASTAFile):
    FASTadic = {}
    FASTAlabel = ""
    
    for line in FASTAFile :
        if ">" in line :
            FASTAlabel = line[1:]
            FASTadic[FASTAlabel] = ""
        else :
            FASTadic[FASTAlabel] += line
    return [x for k,x in FASTadic.items()]



def longest_common_substring(dna_strings):
    def is_common_substring(substr, dna_strings):
        return all(substr in s for s in dna_strings)

    def binary_search_lcs(dna_strings):
        min_len = min(len(s) for s in dna_strings)
        
        low, high = 0, min_len
        longest_substr = ""

        while low <= high:
            mid = (low + high) // 2
            found_common = False

            first_str_subs = set(dna_strings[0][i:i+mid] for i in range(len(dna_strings[0]) - mid + 1))

            for substr in first_str_subs:
                if is_common_substring(substr, dna_strings):
                    longest_substr = substr
                    found_common = True
                    break
            
            if found_common:
                low = mid + 1  
            else:
                high = mid - 1  

        return longest_substr

    return binary_search_lcs(dna_strings)

dna_strings = create_Fasta_Dic(FASTAFile)

result = longest_common_substring(dna_strings)
print(f"Longest common substring: {result}")
