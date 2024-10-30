# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:44:12 2024

@author: user
"""

from structures import *
from Helper_Functions import *

from Bio import SeqIO
from Bio.Seq import Seq

def remove_introns_and_translate(filename):
    sequences = list(SeqIO.parse(filename, "fasta"))

    main_dna = str(sequences[0].seq)    
    introns = [str(seq.seq) for seq in sequences[1:]]
    
    for intron in introns:
        main_dna = main_dna.replace(intron, "") 
    
    exon_only_rna = Seq(main_dna).transcribe()
    protein = exon_only_rna.translate(to_stop=True)  
    
    return str(protein)


filename = "dna_strands.txt"  
protein_sequence = remove_introns_and_translate(filename)
print(protein_sequence)
