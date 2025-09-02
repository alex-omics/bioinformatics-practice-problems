# Reverse Complement Problem

**Task:** Given a DNA string, return the reverse complement strand.

My approach was to use if-else control flow to determine the complementary nucleotide of the input strand, and concatenate them to an empty **"comp"** string. 
Then, I simply reverse-sliced the comp to get the final answer, **"rev_comp"**.

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Data Note:** example sequence sourced from GenBank: [XM_040734646.1](https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1)
