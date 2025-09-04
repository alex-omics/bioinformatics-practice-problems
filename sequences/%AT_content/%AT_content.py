"""
Problem: Given a DNA sequence with canonical nucleic acids (eg. A, T, C, G), determine the percent AT content.
Data Source: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1

Solution Time Complexity: O(n)
    The main loop iterates through each char in the input sequence, counting A and T sequence. This costs O(1) per check for n chars 
    in the sequence for a total cost of O(n). All other mathematical statements cost constant time, O(1).

Solution Space Complexity: O(n)
    The only major contributing factor to space growth complexity is the input string itself, which scales linearly.
"""


# AT content solution 1: Straightforward nt counting
def at_content(input_sequence):

    # Length of input sequence
    seq_length = len(input_sequence)

    # Counter to track A and T nts
    at_count = 0

    for nt in input_sequence:

        # Count As and Ts
        if nt == "A" or nt == "T":

            at_count += 1

    # Compute respective percent AT and GC contents
    pct_at = round(((at_count / seq_length) * 100), 2)

    return pct_at
    
    
# Example DNA sequence
dna = "TAAATCAGAACGGCAGTAAGGTAAGAGCCCCCAGGGATTCCAGGCCCCCTCCACTGGGCAGCCCACGGGGGGGGGCACCATGGGCGTCTCGCATTCTTCCAAGGAGGCGTGGGAACGCGAGAGCAGGAGCGACTTCTGGTGGACGCAGATCCAGGAGGGGTTCCGGAGCCAGAGCGACTTCAACTGGGACCAGATCAAGCAGCTGCACCAGAGGTTCCGGCTGCTGAGCGGAGACCAGCCCACCATCCGGCCCGAGAACTTCGACTACGTCCTGGACCTGGAGTTCAACCCGATCCGCTCCAGGATCGTCCGCGCCTTCTTCGACAACCGGAACCTGGGCAAGGGGACCAGCGGCCTGGCGGAGGAGATTGGCTTCGAGGACTTCCTGACCATCATCTCCTACTTCAAGCCGCTGCGCTCGCACTTCAGCAAGGAGGAGGCGGAGCTGTACCGTCGGGAGAAGCTGCGCTTCCTCTTCCACATGTACGACGAGGACGGCGACGGGGTCATCACGCTGCAGGAGTACCGCAGGGTGGTGGAGGACCTGCTGTCGGCGAACCCGCAGGTGGAGCGCGCCTGGGTGCGCTCCATCGCCAACTCCATCGCGTGCCGCGCCTTGAAGGAGGCGGCCAGGGTGTCCGGCCATCCGCGGCAGGAGGACCAGCCCTACCAGGCCATCACCTTCGAGGACTTCGTCAAGACCTGGCAGGGCATCGACTTGGAGGTCAAGATGCGAGTCAACTTCCTGAACCAAGAAGCCGCGGCCTTGTGACAGTGACCCGCGGGGCCGTGCCCACCCCCAGCCCCACGGGAGAACGCCGTGAGCCCGGCAGCAGCTACCGGGTACGTGGGACTTGGTGACTTTTATCTCTGAGAATAAAGACAAATCAAAA"

# Compute AT content
pct_at_content = at_content(dna)

# Test statements
print("\nOriginal DNA Sequence:\n" + dna)
print("\nThe input sequence has " + str(pct_at_content) + "% AT content.\n")
