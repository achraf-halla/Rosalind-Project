# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:58:52 2024

@author: user
"""

from Helper_Functions import read_fasta
import numpy as np
s, t = read_fasta("problem.txt")

def lcs(s, t):
    m, n = len(s), len(t)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]: 
            lcs_result.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:  
            j -= 1

    return ''.join(reversed(lcs_result))

print(lcs(s, t))