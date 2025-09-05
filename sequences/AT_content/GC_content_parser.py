"""
Problem: Given a file with multiple FASTA-formatted DNA sequences, return the sequence with the highest 
    % GC content, and output the quantity.

Data Sources: 
    Sequence 1. https://www.ncbi.nlm.nih.gov/nuccore/XM_040734646.1
    Sequence 2. https://www.ncbi.nlm.nih.gov/nuccore/XR_005872670.1
    Sequence 3. https://www.ncbi.nlm.nih.gov/nuccore/XR_005872671.1

Solution Time Complexity: O(n)
    The first function will grow linearly in time cost based on the length of the input file. The second merely works off of the 
    number of header:sequence pairs in the dictionary, parsing as many as len(parsed_seqs) pairs for a final cost of O(n).

Solution Space Complexity: O(n)
    The space-intensive component of these algorithms is the dictionary creation, which costs O(n) space depending on the number
    of header:sequence pairs parsed from the input file.
"""

# Function to parse sequences from the input file
def parse_input(file):

    # Open the specified input file (must be in same directory as this script)
    with open(file, 'r') as input_file:

        # Empty structures for parsing the file
        parsed_seqs = {}                        # Dictionary for parsed header:sequence (key:value) pairs
        header = None                           # Variable track current FASTA header
        sequence = []                           # List to hold DNA lines following header

        # Read input file line by line
        for line in input_file:

            # Identify FASTA headers by the right carat symbol
            if line.startswith(">"):

                # If header variable is filled (finished parsing a previous sequence)
                if header is not None:
                    
                    # Create header:sequence pair, add to parsed sequences dictionary
                    parsed_seqs[header] = "".join(sequence)

                # Now with header empty, 
                header = line[1:]               # Slice off header carat 
                sequence = []                   # Empty out sequence temp list

            # For non-carat lines
            else:

                # Collect and append to sequences list
                sequence.append(line.strip())   # Remove newline

        # If no more carats in file, you parsedthe last sequence
        if header is not None:

            # Dump the last header:value pair
            parsed_seqs[header] = "".join(sequence)

    return parsed_seqs


# Function to identify the highest % GC content sequence
def GC_content(parsed_seqs):

    top_header = None                              # Variable to running best sequence 
    top_score = 0                                  # Variable to running high-score

    # Test each sequence in the dictionary
    for header, sequence in parsed_seqs.items():

        GC_count = 0                               # Counter to track GC nts per sequence, resets each loop
        length = len(sequence)                     # Get sequence length to compute % GC

        # Count up Gs and Cs
        for nt in sequence:
            if nt == "G" or nt == "C":
                GC_count += 1

        # Compute and store % GC
        score = (GC_count / length) * 100
        
        # If new high score, store score plus associated header
        if score > top_score:
            top_score = score
            top_header = header

    # Return the high-score pair from zip
    return top_header, top_score


# Parse sequences from test input file
test_sequences = parse_input('/Users/alex/bioinformatics-practice-problems/sequences/AT_content/test_input.fasta')

# Test GC content hi-score caluclator function
top_header, top_score = GC_content(test_sequences)
print("\nHighest GC Content Sequence:")
print(top_header + str(top_score) + "\n")

