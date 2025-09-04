"""
Problem: Given a DNA sequence with canonical nucleic acids (eg. A, T, C, G), output the reverse-complement strand.
Data Source: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1

Solution Time Complexity: O(n^2)
    Reading the input sequence costs O(n), and the reverse slice operation costs O(n). Both of these are subordinate to the string
    concatenation procedure, which involves repeatedly copying over n strings of n chars for the length of the input sequence.
    That operation costs O(n^2).

Solution Space Complexity: O(n)
    The input sequence, comp, and rev_comp variables all cost O(n) space, but they are additive: 3n --> O(n)
"""


# Reverse complement solution 1: Brute force string concatenation
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

# Check to computationally validate algorithm correctness
def passes_check(input_sequence):

    return input_sequence == reverse_complement(reverse_complement(input_sequence))


# Example DNA sequence
dna = "TAAATCAGAACGGCAGTAAGGTAAGAGCCCCCAGGGATTCCAGGCCCCCTCCACTGGGCAGCCCACGGGGGGGGGCACCATGGGCGTCTCGCATTCTTCCAAGGAGGCGTGGGAACGCGAGAGCAGGAGCGACTTCTGGTGGACGCAGATCCAGGAGGGGTTCCGGAGCCAGAGCGACTTCAACTGGGACCAGATCAAGCAGCTGCACCAGAGGTTCCGGCTGCTGAGCGGAGACCAGCCCACCATCCGGCCCGAGAACTTCGACTACGTCCTGGACCTGGAGTTCAACCCGATCCGCTCCAGGATCGTCCGCGCCTTCTTCGACAACCGGAACCTGGGCAAGGGGACCAGCGGCCTGGCGGAGGAGATTGGCTTCGAGGACTTCCTGACCATCATCTCCTACTTCAAGCCGCTGCGCTCGCACTTCAGCAAGGAGGAGGCGGAGCTGTACCGTCGGGAGAAGCTGCGCTTCCTCTTCCACATGTACGACGAGGACGGCGACGGGGTCATCACGCTGCAGGAGTACCGCAGGGTGGTGGAGGACCTGCTGTCGGCGAACCCGCAGGTGGAGCGCGCCTGGGTGCGCTCCATCGCCAACTCCATCGCGTGCCGCGCCTTGAAGGAGGCGGCCAGGGTGTCCGGCCATCCGCGGCAGGAGGACCAGCCCTACCAGGCCATCACCTTCGAGGACTTCGTCAAGACCTGGCAGGGCATCGACTTGGAGGTCAAGATGCGAGTCAACTTCCTGAACCAAGAAGCCGCGGCCTTGTGACAGTGACCCGCGGGGCCGTGCCCACCCCCAGCCCCACGGGAGAACGCCGTGAGCCCGGCAGCAGCTACCGGGTACGTGGGACTTGGTGACTTTTATCTCTGAGAATAAAGACAAATCAAAA"

# Generate reverse-complement
rev_comp = reverse_complement(dna)

# Conduct algorithm check
result = passes_check(dna)

# Test statements
print("\nInput Sequence:\n" + dna + "\n")
print("Reverse-Complement:\n" + rev_comp + "\n")
print("Correct Output?:", result, "\n")
