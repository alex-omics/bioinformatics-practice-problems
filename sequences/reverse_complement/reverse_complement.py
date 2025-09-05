"""
Problem: Given a DNA sequence with canonical nucleic acids (eg. A, T, C, G), output the reverse-complement strand.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


# Brute force string concatenation function; will optimize later
def reverse_complement(input_sequence):

    comp = ""

    # nt complement mapping logic
    for nt in input_sequence:
        if nt == "A":
            comp += ("T")
        elif nt == "T":
            comp += ("A")
        elif nt == "C":
            comp += ("G")
        elif nt == "G":
            comp += ("C")
    
    # Reverse the complement for final answer
    return comp[::-1]

# Check for algorithm correctness
def passes_check(input_sequence):
    
    return input_sequence == reverse_complement(reverse_complement(input_sequence))


# Hardcoded input; will add I/O later
dna = "TAAATCAGAACGGCAGTAAGGTAAGAGCCCCCAGGGATTCCAGGCCCCCTCCACTGGGCAGCCCACGGGGGGGGGCACCATGGGCGTCTCGCATTCTTCCAAGGAGGCGTGGGAACGCGAGAGCAGGAGCGACTTCTGGTGGACGCAGATCCAGGAGGGGTTCCGGAGCCAGAGCGACTTCAACTGGGACCAGATCAAGCAGCTGCACCAGAGGTTCCGGCTGCTGAGCGGAGACCAGCCCACCATCCGGCCCGAGAACTTCGACTACGTCCTGGACCTGGAGTTCAACCCGATCCGCTCCAGGATCGTCCGCGCCTTCTTCGACAACCGGAACCTGGGCAAGGGGACCAGCGGCCTGGCGGAGGAGATTGGCTTCGAGGACTTCCTGACCATCATCTCCTACTTCAAGCCGCTGCGCTCGCACTTCAGCAAGGAGGAGGCGGAGCTGTACCGTCGGGAGAAGCTGCGCTTCCTCTTCCACATGTACGACGAGGACGGCGACGGGGTCATCACGCTGCAGGAGTACCGCAGGGTGGTGGAGGACCTGCTGTCGGCGAACCCGCAGGTGGAGCGCGCCTGGGTGCGCTCCATCGCCAACTCCATCGCGTGCCGCGCCTTGAAGGAGGCGGCCAGGGTGTCCGGCCATCCGCGGCAGGAGGACCAGCCCTACCAGGCCATCACCTTCGAGGACTTCGTCAAGACCTGGCAGGGCATCGACTTGGAGGTCAAGATGCGAGTCAACTTCCTGAACCAAGAAGCCGCGGCCTTGTGACAGTGACCCGCGGGGCCGTGCCCACCCCCAGCCCCACGGGAGAACGCCGTGAGCCCGGCAGCAGCTACCGGGTACGTGGGACTTGGTGACTTTTATCTCTGAGAATAAAGACAAATCAAAA"

# Test statements
rev_comp = reverse_complement(dna)
result = passes_check(dna)
print("\nInput Sequence:\n" + dna + "\n")
print("Reverse-Complement:\n" + rev_comp + "\n")
print("Correct Output?:", result, "\n")
