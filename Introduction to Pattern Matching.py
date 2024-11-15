# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:22:06 2024

@author: user
"""



def read_file (filepath):
    with open(filepath, "r") as f :
        return [l.strip() for l in f.readlines() if l.strip()]



def create_trie(patterns):
    """Creates a trie from a list of strings and returns its adjacency list."""
    trie = {}
    node_id = 1 
    
    trie[1] = {}
    
    for pattern in patterns:
        current_node = 1  
        for char in pattern:
            if char not in trie[current_node]:
                node_id += 1  
                trie[current_node][char] = node_id
                trie[node_id] = {}  
            current_node = trie[current_node][char]
    
    adjacency_list = []
    for parent_node, edges in trie.items():
        for char, child_node in edges.items():
            adjacency_list.append((parent_node, child_node, char))
    with open("ergebnis.txt" , "w") as f:
        for edge in adjacency_list:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
        

patterns = read_file("rosalind_trie.txt")
create_trie(patterns)


