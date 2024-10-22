# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:58:51 2024

@author: user
"""
def cal_rabbits(n, m):
    seq_rab = [1, 1]
    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            new_num = seq_rab[i] + seq_rab[i + 1]
        else:
            for j in range(m - 1):
                new_num += seq_rab[i - j]
        seq_rab.append(new_num)
    return seq_rab[-1]
cal_rabbits(100, 16)
