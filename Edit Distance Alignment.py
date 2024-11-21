# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:04:33 2024

@author: user
"""
from Bio import SeqIO

def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

def edit_distance_with_alignment(s, t):
    m, n = len(s), len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i 
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost) 

    i, j = m, n
    s_aligned, t_aligned = [], []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (0 if s[i - 1] == t[j - 1] else 1):
            s_aligned.append(s[i - 1])
            t_aligned.append(t[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            s_aligned.append(s[i - 1])
            t_aligned.append('-')
            i -= 1
        else:
            s_aligned.append('-')
            t_aligned.append(t[j - 1])
            j -= 1

    s_aligned = ''.join(reversed(s_aligned))
    t_aligned = ''.join(reversed(t_aligned))

    return dp[m][n], s_aligned, t_aligned

def compute_alignment_from_fasta(filename):
    sequences = read_fasta(filename)
    s, t = sequences[0], sequences[1]
    edit_dist, s_aligned, t_aligned = edit_distance_with_alignment(s, t)
    with open("result.txt", "w") as f:
        f.write(f"{edit_dist}\n")
        f.write(f"{s_aligned}\n")
        f.write(f"{t_aligned}\n")

        

compute_alignment_from_fasta("rosalind_edta.txt")
