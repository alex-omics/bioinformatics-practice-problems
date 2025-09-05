"""
Problem: Given two DNA sequences of equal length, compute the number of dissimilar bases between the two 
    (also known as the Hamming Distance, dH(s, t).

Solution Time Complexity: O(n)
    The function loops through the input sequences index by index, only comparing nts of i1 to nts of i2. 

Solution Space Complexity: O(1)
    No new data structures are generated, we just needed simple computation statements and counters.
"""

def hamming(seq1, seq2):

    length = len(seq1)  # Grab the length of one sequence

    mutations = 0  # Counter to track point mutations

    # Iterate through both sequences up to length - 1
    for i in range(0, length - 1):
    
        # Compare nts at corresponding indices
        if seq1[i] != seq2[i]:

            mutations += 1

    return mutations

# Arbitrary sequences of equal length
seq1 = "ATTGTATGTCGTA"
seq2 = "ACTGTATGCCGAA"

# Grab length of input for output statements
length = len(seq1)
mutations = hamming(seq1, seq2)

# Test statements
print("\nSequence 1: {}".format(seq1))
print("Sequence 2: {}".format(seq2) + "\n")
print("The input sequences both have length " + str(length) + ", of which " + str(length - mutations) + " are conserved.")
print("The Hamming distance between input sequences is " + str(mutations) + "\n")
