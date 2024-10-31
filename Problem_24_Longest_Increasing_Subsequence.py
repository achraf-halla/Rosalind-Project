# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:00:12 2024

@author: user
"""

from bisect import bisect_left

""""You can watch the video in this link for clarification: https://www.youtube.com/watch?v=22s1xxRvy28"""

def patience_lis(sequence):
    piles = []          
    parent = [-1] * len(sequence) 
    pile_tops = []      

    for i, num in enumerate(sequence):
        pos = bisect_left(piles, num)  

        if pos == len(piles):
            piles.append(num)
            pile_tops.append(i)
        else:
            piles[pos] = num  
            pile_tops[pos] = i

        if pos > 0:
            parent[i] = pile_tops[pos - 1]
    lis = []
    k = pile_tops[-1]  
    while k != -1:
        lis.append(sequence[k])
        k = parent[k]

    return lis[::-1]

def patience_lds(sequence):
    neg_sequence = [-num for num in sequence]
    lds = patience_lis(neg_sequence)
    return [-num for num in lds]

with open("ina.txt", "r") as file:
    sequence = list(map(int, file.readline().strip().split()))  

lis = patience_lis(sequence)
lds = patience_lds(sequence)

with open("ordered_sub_sequence.txt", "w") as file:
    file.write(" ".join(map(str, lis)) + "\n")
    file.write(" ".join(map(str, lds)))

