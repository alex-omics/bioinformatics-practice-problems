"""
Problem: Given two DNA sequences of equal length, compute the number of dissimilar bases between the two 
    (also known as the Hamming Distance, dH(s, t).

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Hamming distance solution 1: Direct index comparisons
def hamming_direct(seq1, seq2):

    mutations = 0 

    for i in range(0, len(seq1)):
    
        # Compare nts at corresponding indices for mismatches
        if seq1[i] != seq2[i]:

            mutations += 1

    return mutations


def main():

    # Hardcoded input; will add I/O later
    seq1 = "ATTGTATGTCGTA"
    seq2 = "ACTGTATGCCGAA"

    # Test statements
    length = len(seq1)
    mutations = hamming_direct(seq1, seq2)
    print("\nSequence 1: {}".format(seq1))
    print("Sequence 2: {}".format(seq2) + "\n")
    print("The input sequences both have length " + str(length) + ", of which " + str(length - mutations) + " are conserved.")
    print("The Hamming distance between input sequences is " + str(mutations) + ".\n")


if __name__ == "__main__":

    main()
