"""
Problem: Given a DNA sequence with canonical nucleic acids (eg. A, T, C, G), generate the reverse-complement strand.
Data Source: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1

Solution Time Complexity: O(n)
Solution Space Complexity: O(n)
"""

def reverse_complement(input_sequence):

    # Empty string to hold nascent complementary strand
    comp = ""

    # Substitution logic to generate complement from input strand
    for nt in input_sequence:
        if nt == "A":
            comp += ("T")
        elif nt == "T":
            comp += ("A")
        elif nt == "C":
            comp += ("G")
        elif nt == "G":
            comp += ("C")
    
    # Reverse complement strand for final answer
    return comp[::-1]

# Check to computationally validate correct results
def passes_check(DNA, rev_comp):

    return DNA == reverse_complement(reverse_complement(DNA))

# Example DNA sequence
DNA = "TAAATCAGAACGGCAGTAAGGTAAGAGCCCCCAGGGATTCCAGGCCCCCTCCACTGGGCAGCCCACGGGGGGGGGCACCATGGGCGTCTCGCATTCTTCCAAGGAGGCGTGGGAACGCGAGAGCAGGAGCGACTTCTGGTGGACGCAGATCCAGGAGGGGTTCCGGAGCCAGAGCGACTTCAACTGGGACCAGATCAAGCAGCTGCACCAGAGGTTCCGGCTGCTGAGCGGAGACCAGCCCACCATCCGGCCCGAGAACTTCGACTACGTCCTGGACCTGGAGTTCAACCCGATCCGCTCCAGGATCGTCCGCGCCTTCTTCGACAACCGGAACCTGGGCAAGGGGACCAGCGGCCTGGCGGAGGAGATTGGCTTCGAGGACTTCCTGACCATCATCTCCTACTTCAAGCCGCTGCGCTCGCACTTCAGCAAGGAGGAGGCGGAGCTGTACCGTCGGGAGAAGCTGCGCTTCCTCTTCCACATGTACGACGAGGACGGCGACGGGGTCATCACGCTGCAGGAGTACCGCAGGGTGGTGGAGGACCTGCTGTCGGCGAACCCGCAGGTGGAGCGCGCCTGGGTGCGCTCCATCGCCAACTCCATCGCGTGCCGCGCCTTGAAGGAGGCGGCCAGGGTGTCCGGCCATCCGCGGCAGGAGGACCAGCCCTACCAGGCCATCACCTTCGAGGACTTCGTCAAGACCTGGCAGGGCATCGACTTGGAGGTCAAGATGCGAGTCAACTTCCTGAACCAAGAAGCCGCGGCCTTGTGACAGTGACCCGCGGGGCCGTGCCCACCCCCAGCCCCACGGGAGAACGCCGTGAGCCCGGCAGCAGCTACCGGGTACGTGGGACTTGGTGACTTTTATCTCTGAGAATAAAGACAAATCAAAA"

# Generate reverse-complement
rev_comp = reverse_complement(DNA)

# Conduct check
result = passes_check(DNA, rev_comp)

# Test statements
print("\nInput Sequence: " + DNA + "\n")
print("Reverse-Complement: " + rev_comp + "\n")
print("Correct Output?:", result, "\n")