# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:36:28 2024

@author: user
"""
n = 956304
s = "GCTATCTAAT"
A = [float(x) for x in "0.000 0.110 0.134 0.226 0.290 0.328 0.394 0.415 0.492 0.541 0.593 0.693 0.720 0.815 0.877 0.904 1.000".split(" ")]
def expected_occurrences(n, s, A):
    """
    Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
    Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, 
            where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
    """
    m = len(s)  
    B = []
    
    for gc_content in A:

        prob_s = 1.0
        for char in s:
            if char in "GC":
                prob_s *= gc_content / 2
            else: 
                prob_s *= (1 - gc_content) / 2
        
        if n >= m:
            expected_count = (n - m + 1) * prob_s
        else:
            expected_count = 0
        
        B.append(expected_count)
    
    return B


result = expected_occurrences(n, s, A)

print(" ".join(f"{x:.3f}" for x in result))
