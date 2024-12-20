# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:19:31 2024

@author: user
"""

from itertools import product

symbols = ("C W U X I H D J G E A S").split(" ")


def ord_var_strings(symbols, n):
    """
Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n <= 4

Return: All strings of length at most n formed from A, ordered lexicographically. 
       (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

    """
    store = []
    rank = {symbol: i for i, symbol in enumerate(symbols)}
    def sort_key(t):
        return [rank[symbol] for symbol in t]
    while 0 < n:
        perm = list(product(symbols, repeat = n))
        store.extend(perm)
        n -= 1
    with open("order_str.txt","w") as f:
        for x in sorted(store,key = sort_key):
            f.write("".join(x) + "\n")
n = 3
ord_var_strings(symbols, n)
