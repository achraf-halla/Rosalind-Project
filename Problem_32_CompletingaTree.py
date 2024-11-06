# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:29:57 2024

@author: user
"""

import networkx as nx


def read_file (filepath):
    with open(filepath, "r") as f :
        liste = [l.strip() for l in f.readlines()]
        n = int(liste[0])
        liste = [x.split(" ") for x in  liste[1:]] 
        return n,  [(int(x[0]), int(x[1]) ) for x in liste] 
n, liste = read_file("rosalind_tree.txt")   


def complete_a_tree(n,edges):
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    G.add_edges_from(liste)
    return len(list(nx.connected_components(G))) -1

complete_a_tree(n, liste)
