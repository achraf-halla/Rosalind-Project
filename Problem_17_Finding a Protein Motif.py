# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:39:50 2024

@author: user
"""

import re
import requests

def fetch_protein_sequence(uniprot_id):
    """
    Fetches the protein sequence for a given UniProt ID from the UniProt database.
    """
    accession_id = uniprot_id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{accession_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.splitlines()
        sequence = ''.join(lines[1:])  
        return sequence
    return None

def find_motif_locations(sequence, motif_regex):
    """
    Finds the starting positions of motifs in the given protein sequence matching the specified regex pattern.
    """

    locations = []
    for i in range(len(sequence) - 3):  
        if re.match(motif_regex, sequence[i:i+4]):
            locations.append(i + 1) 
    return locations

def main(uniprot_ids):
    """
    Processes a list of UniProt IDs, retrieves their protein sequences, finds motif locations, and prints results.
    """

    motif_regex = r'N[^P][ST][^P]'  
    results = []

    for uniprot_id in uniprot_ids:
        try:
            sequence = fetch_protein_sequence(uniprot_id)
            if sequence:
                locations = find_motif_locations(sequence, motif_regex)
                if locations:
                    results.append((uniprot_id, locations))
        except Exception as e:
            print(f"Error processing {uniprot_id}: {e}")

    for uniprot_id, locations in results:
        print(uniprot_id)
        print(' '.join(map(str, locations)))




uniprot_ids =  """A4TEW1
P01047_KNL2_BOVIN
Q3B391
A8F2D7
Q3ATP6
A6LJ74
P01189_COLI_HUMAN
P00304_ARA3_AMBEL
P10646_TFPI_HUMAN
P01045_KNH2_BOVIN
Q03745
B8GYE3
P0C5G9
P0AEI6""".split("\n")
main(uniprot_ids)
    
