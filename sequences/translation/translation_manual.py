"""
Problem: Given an RNA sequence, determine the resulting protein sequence. 

Data Source: https://www.ncbi.nlm.nih.gov/nuccore/D63412.1?report=fasta
"""

# Allow script to execute directly from VS Code
if __name__ == "__main__" and __package__ is None: 
    import sys 
    from pathlib import Path 
    sys.path.append(str(Path(__file__).resolve().parents[2]))
import os
from sequences.translation.codon_to_aa_table import codon_to_aa_table

# Path script to input file
script_directory = os.path.dirname(__file__)
test_file_path = os.path.join(script_directory, "test_file_translation.fasta")

# Parser function to extract DNA from Nucleotide FASTA files
def file_parser(file_path):

    fasta_lines = []
    with open(file_path) as file:

        for line in file:
            if line.startswith(">"):
                continue

            fasta_lines.append(line.strip())

    dna = "".join(fasta_lines)
    return dna


# Function to map DNA codons to amino acids 
# DIRECTION TRANSLATION FOR NOW, MUST INCORPORATE ORF DETECTION
def translate_manual(dna):

    protein = []

    for i in range(0, len(dna), 3):

        codon = dna[i:i+3]  # Scan DNA indices in groups of 3

        # Skip any incomplete codons at the end
        if len(codon) < 3:
            break

        amino_acid = codon_to_aa_table.get(codon)   
        protein.append(amino_acid)
    
    protein_final = "".join(protein)
    return protein_final


# Test statements
dna = file_parser(test_file_path)
protein = translate_manual(dna)
print(protein)