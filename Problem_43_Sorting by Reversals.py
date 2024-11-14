# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:03:13 2024

@author: user
"""

def read_permutations(file_path):
    """
    Reads pairs of permutations from a file, returning them as a list of tuples.
    Each tuple contains two lists of integers representing a pair of permutations.
    """
    permutation_pairs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    
    for i in range(0, len(lines), 2): 
        tuple1 = list(map(int, lines[i].split()))
        tuple2 = list(map(int, lines[i + 1].split()))
        permutation_pairs.append((tuple1, tuple2))
    
    return permutation_pairs


def calculate_reversal_distances(file_path):
    """
    Reads permutation pairs from a file, calculates the reversal distance for each pair,
    and prints the distances and sequences of reversals.
    """
    permutation_pairs = read_permutations(file_path)
    for s, t in permutation_pairs:
        combined_reversal_distance(s, t)


def reversal_distance_single_direction(a, b):
    """
    Calculate the reversal distance (minimum reversals) between two permutations in one direction.
    """
    n = len(b)
    p = [0] * n
    for i, val in enumerate(b):
        p[val - 1] = i + 1
    a = [p[val - 1] for val in a]

    reversals = 0
    reversals_col = []
    
    def count_breakpoints(perm):
        """Counts the number of breakpoints in the permutation."""
        perm = [0] + perm + [len(perm) + 1]  
        breakpoints = sum(1 for i in range(len(perm) - 1) if abs(perm[i + 1] - perm[i]) != 1)
        return breakpoints

    def find_best_reversal(perm):
        """Finds the best reversal to minimize breakpoints."""
        max_breakpoint_reduction = 0
        best_reversal = None

        for i in range(n):
            for j in range(i + 1, n):
                new_perm = perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]
                bp_reduction = count_breakpoints(perm) - count_breakpoints(new_perm)

                if bp_reduction > max_breakpoint_reduction:
                    max_breakpoint_reduction = bp_reduction
                    best_reversal = (i, j)
        return best_reversal

    while count_breakpoints(a) > 0:
        best_reversal = find_best_reversal(a)
        if best_reversal:
            i, j = best_reversal
            reversals_col.append([i + 1, j + 1]) 

            a[i:j + 1] = reversed(a[i:j + 1])
            reversals += 1

    reversals_col.insert(0, reversals)  
    return reversals_col


def combined_reversal_distance(a, b):
    """
    Calculate the minimum reversal distance by considering both directions (a to b and b to a),
    then print the result without returning None.
    """
    distance_a_to_b = reversal_distance_single_direction(a, b)
    distance_b_to_a = reversal_distance_single_direction(b, a)
    
    if distance_a_to_b[0] < distance_b_to_a[0]:
        print(distance_a_to_b[0])
        for pair in distance_a_to_b[1:]:
            print(" ".join(map(str, pair)))
    else:
        print(distance_b_to_a[0])
        for pair in distance_b_to_a[1:]:
            print(" ".join(map(str, pair)))



calculate_reversal_distances("ina.txt")
