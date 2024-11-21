# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:05:12 2024

@author: user
"""

from Bio import SeqIO

MOD = 134_217_727

def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

def count_optimal_alignments(s, t):
    """
    Given: Two protein strings s and t in FASTA format, each of length at most 1000 aa.

    Return: The total number of optimal alignments of s and t with respect to edit alignment score, modulo 134,217,727
    """
    m, n = len(s), len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    count = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
        count[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = j
        count[0][j] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,  dp[i - 1][j - 1] + cost)  

            count[i][j] = 0
            if dp[i][j] == dp[i - 1][j] + 1:
                count[i][j] += count[i - 1][j]
            if dp[i][j] == dp[i][j - 1] + 1:
                count[i][j] += count[i][j - 1]
            if dp[i][j] == dp[i - 1][j - 1] + cost:
                count[i][j] += count[i - 1][j - 1]

            count[i][j] %= MOD

    return count[m][n]

def compute_optimal_alignment_count_from_fasta(filename):
    sequences = read_fasta(filename)


    s, t = sequences[0], sequences[1]
    return count_optimal_alignments(s, t)


result = compute_optimal_alignment_count_from_fasta("rosalind_edta.txt")
print(f"{result}")
