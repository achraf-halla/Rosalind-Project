# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:50:21 2024

@author: user
"""

def find_substring_brute(s, t):

        if s == t: 
           return True



def readfile(filepath):
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
    
FASTAFile = readfile("problem 12 input text.txt")

FASTadic = {}
FASTAlabel = ""

for line in FASTAFile :
    if ">" in line :
        FASTAlabel = line[1:]
        FASTadic[FASTAlabel] = ""
    else :
        FASTadic[FASTAlabel] += line
def overlap_graph(dic, k):
    lis = []
    for key, v in dic.items():
        for s, m in dic.items() :
            if s != key :

                if find_substring_brute(v[-k:], m[:k]) :
                       print(key,s)
overlap_graph(FASTadic, 3)

            
            