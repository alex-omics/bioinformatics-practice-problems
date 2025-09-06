# Hamming Distance Problem 
Given two DNA sequences of equal length, calculate the Hamming Distance, dH(s, t), or the number of nucleotides at which one sequence (the reference) differs from the second sequence (the query).

## Task
Count and return the number of characters that are different between two input strings. 

## How I Solved It
My first solution, *hamming_direct* uses iterates from i = 0 to i = len(seq), comparing nucleotides at respective indices between the two sequences. If a mismatch is found, it's counted as a mutation. I then made a zip object by zipping up the sequences and iterating directly through that object, as shown in *hamming_zip*.

## Input / Output
- **Input:** Two DNA sequences of equal length
- **Output:** 

## Time Complexity
For both solutions, the function loops through the input sequences index by index, only comparing nts of i1 to nts of i2. The timecost will grow linearly with respect to the length of either sequence. 

**Cost: O(n)**

## Space Complexity
 No new data structures are generated, only simple computation statements and counters were needed.

**Cost: O(1)**

## Lessons Learned
There are many ways to code the exact same functionality. Some methods are superior to others in space or time efficiency. Others may simply be more elegant, intuitive, or "Pythonic" / "idiomatic".

## Planned Improvements
- **Add a CLI wrapper with error checking**
- **Handle user-specified input/output**
- **Print results in a friendlier CLI format**
- **Enable file printing in BLAST format**
