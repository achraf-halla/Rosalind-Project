# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:49:04 2024

@author: user
"""

import networkx as nx

def construct_Graph(filepath):
    """
    Constructs a directed graph (suffix tree) from a file.
    """
    with open(filepath, "r") as f:
        liste = [l.strip() for l in f.readlines() if l.strip()]
        string = liste[0]
        k = int(liste[1])
        G = nx.DiGraph()

        for i in range(2, len(liste)):
            edge_info = liste[i].split(" ")
            parent, child = edge_info[0], edge_info[1]
            start, length = int(edge_info[2]), int(edge_info[3])

            if parent not in G:
                G.add_node(parent)
            if child not in G:
                G.add_node(child)

            G.add_edge(parent, child, substring=string[start:start + length])

        return G, string, k

def count_leaves_and_depth(G, node, k):
    """
    Performs a post-order traversal to count leaves and find the longest substring.
    """
    if len(list(G.successors(node))) == 0:
        return 1, ""

    total_leaves = 0
    longest_substring = ""
    max_depth = 0

    for child in G.successors(node):
        edge_label = G.edges[node, child]["substring"]
        leaves, substring = count_leaves_and_depth(G, child, k)

        total_leaves += leaves

        if leaves >= k:
            depth = len(edge_label) + len(substring)
            if depth > max_depth:
                max_depth = depth
                longest_substring = edge_label + substring

    return total_leaves, longest_substring

def analyze_tree(A, string, k):
    """
    Analyzes the suffix tree to find the longest repeated substring.
    """
    _, longest_substring = count_leaves_and_depth(A, "node1", k)
    return longest_substring

filepath = "rosalind_lrep.txt"  
G, string, k = construct_Graph(filepath)
result = analyze_tree(G, string, k)
print("Longest substring repeated at least", k, "times:", result)
