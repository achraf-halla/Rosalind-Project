# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:34:06 2024

@author: user
"""

def Transcription(seq):
    """ DNA -> DNA Transcription by replacing thymine with uracyl """
    return seq.replace("T" , "U")


string = "GATGGAACTTGACTACGTAAATT"
result = Transcription(string)
print(result=="GAUGGAACUUGACUACGUAAAUU")