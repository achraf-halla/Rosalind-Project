# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:59:21 2024

@author: user
"""

n = None
A = set()
B = set()

with open("ina.txt", "r") as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    A = set(map(int, lines[1].strip('{}\n').split(', ')))
    B = set(map(int, lines[2].strip('{}\n').split(', ')))

def return_sets(n, A, B):
    """
    Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
    Return: Six sets: Union of A and B, Intersection of and B, A difference B, B difference A, set complement of A, and set complement of B (where set complements are taken w.r.t {1,2,…,n}).
    """
    with open("result2.txt", "w") as f:
        
        f.write(str(A.union(B)) + "\n")        
        f.write(str(A.intersection(B)) + "\n")       
        f.write(str(A.difference(B)) + "\n")
        f.write(str(B.difference(A)) + "\n")
        f.write(str(set(range(1, n+1)).difference(A)) + "\n")
        f.write(str(set(range(1, n+1)).difference(B)) + "\n")

return_sets(n, A, B)


