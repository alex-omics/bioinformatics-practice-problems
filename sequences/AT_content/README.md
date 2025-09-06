# %AT Problem 
Given one or more DNA strings with canonical nucleotides (A, T, C, G), determine what percentage of the sequence is composed of adenine (A) and thymine nucleotides (singular) or which has the highest percentage (multiple).

## Task
From an input DNA sequence, return the %AT content, or if multiple FASTA sequences are provided, return the sequence with the highest %AT content.

## How I Solved It
Simply counting percentage AT only requires a counting loop and some mathematical statements. Should the user input a FASTA file with multiple DNA sequences, a parser function will extract however many sequences exist in the file and evaluate them. The main loop computes percentage AT of all parsed sequences iteratively, tracking the running top score. By the end, sequence's FASTA header plus its %AT are output. 

## Input / Output
- **Input:** FASTA file with one or more DNA sequences.
- **Output:** Percentage AT content (single sequence), or sequence with highest percentage AT content (multiple).

## Time Complexity
The *parse_seqs* function will grow linearly in time cost based on the number of lines in the input file, O(n). The *max_at_content* time cost depends on two factors: the number of sequences (s), and the average length of these sequences (l). The function will iterate through each s sequence an average of l times for a final cost of O(s * l). In practice, this means that the runtime grows linearly based on the number of nucleotides in the file, which simplifies to O(n).

**Cost: O(n)**

## Space Complexity
The main space cost comes from the dictionary that stores the header:sequence pairs. If there are s sequences of average length l, the dictionary holds roughly s * l nucleotides. Since the total number of nucleotides is s * l, the overall space complexity linearly with input size, O(n).

**Cost: O(n)**

## Lessons Learned
The real challenge for this problem was not in computing percentage AT, but in parsing header:sequence pairs from a FASTA file. Appropriate selection Python's *open()* methods (*read()*, *readlines()*, etc.) is key to handling input correctly. Dictionaries make it straightforward to store header:sequence pairs and retrieve them later. Make sure to empty out temp variables after each loop iteration!

## Planned Improvements
- **Add a CLI wrapper with error checking**

## References
- **XM_040734646.1**: https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1
- **XR_005872670.1**: https://www.ncbi.nlm.nih.gov/nuccore/XR_005872670.1
- **XR_005872671.1**: https://www.ncbi.nlm.nih.gov/nuccore/2025801349
