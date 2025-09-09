"""
Problem: Given an RNA sequence, determine the resulting protein sequence. 

Data Source: https://www.ncbi.nlm.nih.gov/nuccore/D63412.1?report=fasta
"""

import os
import sys
from sequences.transcription.transcription_string_replace import transcribe_replace

# Get absolute paths from script to codon table an dinput file
script_directory = os.path.dirname(__file__)
codon_table_path = os.path.join(script_directory, "codon_table_hardcoded.py")
test_file_path = os.path.join(script_directory, "test_file_translation.fasta")
# print("table path: " + codon_table_path)
# print("fasta path: " + test_file_path)


# Parser function to extract DNA from Nucleotide FASTA files
def file_parser_lines(file_path):

    fasta_lines = []
    with open(file_path) as file:

        for line in file:
            if line.startswith(">"):
                continue

            fasta_lines.append(line.strip())

    dna = "".join(fasta_lines)
    return dna

# Test statements
dna = file_parser_lines(test_file_path)
print(dna)
rna = transcribe_replace(dna)
print(rna)