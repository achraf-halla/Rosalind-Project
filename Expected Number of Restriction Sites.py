# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:36:28 2024

@author: user
"""
n = 956304
s = "GCTATCTAAT"
A = [float(x) for x in "0.000 0.110 0.134 0.226 0.290 0.328 0.394 0.415 0.492 0.541 0.593 0.693 0.720 0.815 0.877 0.904 1.000".split(" ")]
def expected_occurrences(n, s, A):
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
