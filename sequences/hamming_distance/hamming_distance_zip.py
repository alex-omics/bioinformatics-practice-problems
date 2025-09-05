"""
Problem: Given two DNA sequences of equal length, compute the number of dissimilar bases between the two 
    (also known as the Hamming Distance, dH(s, t). This solution features a more elegant algorithm that
    uses the built-in zip() function.

Solution Time Complexity: O(n)
    We loop through the input sequences index by index, only comparing nts of i1 to nts of i2. 

Solution Space Complexity: O(1)
    No new data structures are generated, we just needed simple computation statements and counters.
"""

def hamming_zip(seq1, seq2):

    mutations = 0  # Counter to track point mutations

    # Iterate through result of zip(seq1, seq2)
    for nt1, nt2 in zip(seq1, seq2):
    
        # Compare nts at corresponding indices
        if nt1 != nt2:

            mutations += 1

    return mutations

# Arbitrary sequences of equal length
seq1 = "ATTGTATGTCGTA"
seq2 = "ACTGTATGCCGAA"

# Grab length of input for output statements
length = len(seq1)
mutations = hamming_zip(seq1, seq2)

# Test statements
print("\nSequence 1: {}".format(seq1))
print("Sequence 2: {}".format(seq2) + "\n")
print("The input sequences both have length " + str(length) + ", of which " + str(length - mutations) + " are conserved.")
print("The Hamming distance between input sequences is " + str(mutations) + "\n")
