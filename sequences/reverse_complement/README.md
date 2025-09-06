# Reverse Complement Problem 
Given a DNA string with canonical nucleotides (A, T, C, G), compute its reverse complement, the sequence that would form the opposite strand in DNA's double helix structure.

## Task
From an input DNA sequence, return the reverse complement strand.

## How I Solved It
I used an if-else control flow to determine the complementary nucleotides, concatenated them to a *comp* string, then reverse-sliced (`[::-1]`) *comp* to get *rev_comp*.

## Input / Output
- **Input:** String of A/T/C/G (uppercase only supported for now)
- **Output:** Reverse complement string
- **Assumptions:** Input is currently hardcoded; user-specified I/O not yet supported (see *Planned Improvements*).

## Time Complexity
Reading the input sequence costs O(n), and the reverse slice operation costs O(n). Both of these are subordinate to the string concatenation procedure, which involves repeatedly copying over n strings of n chars for the length of the input sequence. That operation costs O(n^2).

**Cost: (n^2)**

## Space Complexity
The input sequence, comp, and rev_comp variables all cost O(n) space. They are additive: 3(n) = 3n, which reduces to O(n).

**Cost: (n)**

## Lessons Learned
I first attempted using *.append()*, but realized that method doesn't apply to strings. I came up with a string concatenation scheme, but acknowledge that it isn't particularly efficient given all the string copying.

## Planned Improvements
- **Brainstorm/implement improved nucleotide-mapping algorithm**
- **Handle user-specified input/output**
- **Add a CLI wrapper with error checking**
- **Support FASTA files**
- **Print results in a friendlier CLI format**

## References
- **XM_040734646.1**: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1
