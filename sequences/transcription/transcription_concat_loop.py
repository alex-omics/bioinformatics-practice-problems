"""
Problem: Given a DNA sequence with canonical nucleic acids (e.g. A, T, C, G), output the correcponding RNA transcript
Data Source: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1

Solution Time Complexity: O(n^2)
    Given that the input string is broken into substrings and each substring concatenation costs O(n) time, the total time 
    cost is 1 + 2 + 3 ... len(input_sequence) --> O(n^2)

Solution Space Complexity: O(n)
    Major contributing variables are dna and rna which vary in space by a factor of n; 2n -> O(n)
"""


# Transcription method 1: Brute-force looped string concatenation 
def transcribe_string_concat(dna):

    rna = ""

    # Iterate through nts in DNA
    for nt in dna:

        # If T encountered, add U instead
        if nt == "T":
            rna += "U"

        # Tack non-thymine nts onto nascent RNA strand
        else:
            rna += nt

    return rna


# Example DNA sequence
dna = "TAAATCAGAACGGCAGTAAGGTAAGAGCCCCCAGGGATTCCAGGCCCCCTCCACTGGGCAGCCCACGGGGGGGGGCACCATGGGCGTCTCGCATTCTTCCAAGGAGGCGTGGGAACGCGAGAGCAGGAGCGACTTCTGGTGGACGCAGATCCAGGAGGGGTTCCGGAGCCAGAGCGACTTCAACTGGGACCAGATCAAGCAGCTGCACCAGAGGTTCCGGCTGCTGAGCGGAGACCAGCCCACCATCCGGCCCGAGAACTTCGACTACGTCCTGGACCTGGAGTTCAACCCGATCCGCTCCAGGATCGTCCGCGCCTTCTTCGACAACCGGAACCTGGGCAAGGGGACCAGCGGCCTGGCGGAGGAGATTGGCTTCGAGGACTTCCTGACCATCATCTCCTACTTCAAGCCGCTGCGCTCGCACTTCAGCAAGGAGGAGGCGGAGCTGTACCGTCGGGAGAAGCTGCGCTTCCTCTTCCACATGTACGACGAGGACGGCGACGGGGTCATCACGCTGCAGGAGTACCGCAGGGTGGTGGAGGACCTGCTGTCGGCGAACCCGCAGGTGGAGCGCGCCTGGGTGCGCTCCATCGCCAACTCCATCGCGTGCCGCGCCTTGAAGGAGGCGGCCAGGGTGTCCGGCCATCCGCGGCAGGAGGACCAGCCCTACCAGGCCATCACCTTCGAGGACTTCGTCAAGACCTGGCAGGGCATCGACTTGGAGGTCAAGATGCGAGTCAACTTCCTGAACCAAGAAGCCGCGGCCTTGTGACAGTGACCCGCGGGGCCGTGCCCACCCCCAGCCCCACGGGAGAACGCCGTGAGCCCGGCAGCAGCTACCGGGTACGTGGGACTTGGTGACTTTTATCTCTGAGAATAAAGACAAATCAAAA"

# Generate RNA transcript from input sequence
rna = transcribe_string_concat(dna)

# Test statements
print("\nOriginal DNA strand: " + dna + "\n")
print("Resulting RNA strand: " + rna + "\n")
