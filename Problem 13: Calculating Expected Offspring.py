# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:58:53 2024

@author: user
"""

def expected_dom_offs(couples):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    
    exp_val = 2 * sum(couples[i] * probabilities[i] for i in range(6))
    
    return exp_val

couples = [19804 ,19513 ,18882 ,17918 ,19330 ,19932]

result = expected_dom_offs(couples)
print(result)
