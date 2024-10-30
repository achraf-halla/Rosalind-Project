# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:50:21 2024

@author: user
"""

def find_substring_brute(s, t):
    """
    Checks if two sequences, `s` and `t`, are identical.

    Parameters:
    -----------
    s : str
        The first sequence to compare.
    t : str
        The second sequence to compare.
    
    Returns:
    --------
    bool
        True if `s` and `t` are identical, otherwise False.
    """
        if s == t: 
           return True



def readfile(filepath):
    """
    Reads a file and returns each line as an element in a list, stripped of any 
    leading or trailing whitespace.

    Parameters:
    -----------
    filepath : str
        Path to the file to be read.
    
    Returns:
    --------
    list of str
        A list containing each line from the file as a separate string.
    """
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
    
FASTAFile = readfile("problem 12 input text.txt")

FASTadic = {}
FASTAlabel = ""

for line in FASTAFile :
    if ">" in line :
        FASTAlabel = line[1:]
        FASTadic[FASTAlabel] = ""
    else :
        FASTadic[FASTAlabel] += line
def overlap_graph(dic, k):
    """
    Constructs an overlap graph from a dictionary of DNA sequences, where an edge 
    exists between sequences if the suffix of length `k` in one sequence matches the 
    prefix of length `k` in another.

    Parameters:
    -----------
    dic : dict of {str : str}
        A dictionary where keys are sequence labels and values are DNA sequences.
    k : int
        The length of the matching prefix and suffix required for an overlap.

    Returns:
    --------
    None
        Prints pairs of labels representing overlaps of `k` nucleotides.
    """
    lis = []
    for key, v in dic.items():
        for s, m in dic.items() :
            if s != key :

                if find_substring_brute(v[-k:], m[:k]) :
                       print(key,s)
overlap_graph(FASTadic, 3)

            
            
