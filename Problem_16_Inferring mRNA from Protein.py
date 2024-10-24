# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:26:15 2024

@author: user
"""




from structures import *
def count_rna_strings(protein):
    total_combinations = 1
    modulo = 1000000
    
    for amino_acid in protein:
        total_combinations *= codon_table[amino_acid]
        total_combinations %= modulo  
    total_combinations *= codon_table['Stop']
    total_combinations %= modulo
    
    return total_combinations

protein_string = "MRPQASIWPEEPAQDWMWLNSDVQYIKHMMNDIWQPMDKVHENPEGWKMWHYHAHLWQDNMAHVMGTHYQYSTEYKVQTFCFGDHFGQYGCAVKTTPPSRMGDSHIVYLVCLSIPFIGGHSDCFMKESTSVKFYHMHVVATMLHRYGRQGSPDGWRMDPATTRQMANGFGEAENMRKHFCHTAYHFFSYRVWQRKYISLCMETACYQLIPCVDSYWNKYHQKFNDPQPFGPGQYIGTKRMCLDYAYTPNISAHHIHNDNRLWKMECCWLEWFHLKGGTIVMQLYAFWHIPEWHNLGVGFQREFTNADRRATKQNMRFYYSWEFEEDVVMHGMFINSEKCFVERDAVGPLNTDWTDQLATHCMLDCSDYRLLYPVHFNFMNLYFEGKRVLDGHVHIIFTYICLSLRYEMYSNTDNTHQDDQKPSKPFAEKCYKQLDDRYPHDYMYYIMFIFMRIARTAPWMHGRCQTVMGQSNINTAKAFKGDKIGAMPQDQWAHNKSHRESCEGKFCVPCIWSDTESNWQVCWFDSIVTSLNNQYPIGFQMPGSHTQAPLDYIIIYIKFQSNWPFYAPYASSGFHRTQWEPYPPWCDIGLMRLIFDWCMKVHSTNDEMYEEFFIDKCIHDDIYDEHRTYTLEQFECYDKQQHKLTHQQPTGAIMILSQGPMTFGEQVRVCWQVWKCGKFHEILDGTNNCIYFFSVFVSDKDWFHIGCNCMGAQAHQFETAQLNLSRNQKWNTFWNSTITRPPCCALSVPSYDTIQDEDPGTNKEGPREGFWIAGRVFDQAFEIFTHIQIPCDWFNGIDMFKTRPRIDQFYSGNAELKGCYPENQHFMPHFHQSLPFIEMGSSWIIAFPIIQHWWDMQVCAESCQMPNYRHMVMDPDQDILMEMEMCWPQVLSGCVSKNIMENKVAFGQTIVWPIYFWADRECKQWTYKFWYGRYGSDSLRVCFQFTFFDSSPDAEVFEHTTNRRTRLQSNMPPWPCDENYIPSDYLIAPQPWSMAWTAD"
result = count_rna_strings(protein_string)
print(result)
