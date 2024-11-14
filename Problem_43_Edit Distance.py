# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:03:38 2024

@author: user
"""
from Bio import SeqIO
from Bio.Seq import Seq
def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

def edit_distance(seq1, seq2):
    """
    Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
    Return: The edit distance dE(s,t).
    """
    m = len(seq1) + 1
    n = len(seq2) + 1

    tbl = {}
    for i in range(m):
        tbl[i, 0] = i
    for j in range(n):
        tbl[0, j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if seq1[i - 1] == seq2[j - 1] else 1
            tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost)

    return tbl[m - 1, n - 1]

s ,t = read_fasta("ina.txt")
print(edit_distance(s,t))

