# Transcription Problem 
Given a DNA string with canonical nucleotides (A, T, C, G), compute its corresponding RNA sequence, the sequence that would result from the DNA being transcribed by RNA polymerase enzymes.

## Task
From an input DNA sequence, transform the DNA strand into the equivalent RNA strand.

## How I Solved It
We don't need to change the input's orientation; the thymine nucleotides (T) simply need to be swapped out for uracil (U) nucleotides. The initial string concatenation algorithm I implemented cost O(n^2) time, which was optimized to O(n) by implementing a *DNA.replace('T', 'U')* scheme that reduces runtime to O(n).

## Input / Output
- **Input:** String of A/T/C/G (uppercase only supported for now)
- **Output:** Corresponding RNA string with A/U/C/G nucleotides
- **Assumptions:** Input is currently hardcoded; user-specified I/O not yet supported (see *Planned Improvements*).

## Time Complexity
Given that the input string is broken into substrings and each substring concatenation costs O(n) time, the total time cost is 1 + 2 + 3 ... len(input_sequence), or O(n^2). The .replace() method scans the input sequence's n chars, resulting in O(n) read time and constant O(1) char check times. Since there is no copying as with the string concatenation procedure, the resulting time complexity is O(n).

**Concat Algorithm: O(n^2)**,
**Replace Algorithm: O(n)**

## Space Complexity
Major contributing variables are DNA and RNA strings, which vary in space by a factor of n, summing to 2n, which reduces to O(n). No difference in space cost between the *concat* and *replace* algorithms.

**Concat Algorithm: O(n)**,
**Replace Algorithm: O(n)**

## Lessons Learned
In programming languages in which strings are immutable, string concatenation results in quadratic times. For disciplines like bioinformatics where manipulating strings is common, we should consider alternatives, particularly builtin methods like .replace().

## Planned Improvements
- **Handle user-specified input/output**
- **Add a CLI wrapper with error checking**
- **Support FASTA files**
- **Print results in a friendlier CLI format**

## References
- **XM_040734646.1**: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1
