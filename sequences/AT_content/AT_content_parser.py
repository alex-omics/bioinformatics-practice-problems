"""
Problem: Given a file with multiple FASTA-formatted DNA sequences, return the sequence with the highest % AT content, 
    and output the quantity.

Solution Time Complexity: O(n)
Solution Space Complexity: O(n)
"""


# Function to parse sequences from the input file
def parse_input(file):

    with open(file, 'r') as input_file:

        # Empty structures for parsing the file
        parsed_seqs = {}
        header = None
        sequence = []

        for line in input_file:

            # Identify FASTA headers by the right carat symbol
            if line.startswith(">"):

                # If header variable is filled (finished parsing a previous sequence)
                if header is not None:
                    
                    # Create header:sequence pair, add to parsed sequences dictionary
                    parsed_seqs[header] = "".join(sequence)

                header = line[1:]   # Slice off header carat 
                sequence = []       # Empty out sequence temp list

            else:

                # Collect and append to sequences list
                sequence.append(line.strip())

        # If no more carats found, last sequence has been parsed
        if header is not None:

            # Dump the last header:value pair
            parsed_seqs[header] = "".join(sequence)

    return parsed_seqs


# Function to identify the highest % AT content sequence
def max_at_content(parsed_seqs):

    top_header = None
    top_score = 0

    # Test each sequence in the dictionary
    for header, sequence in parsed_seqs.items():

        AT_count = 0
        length = len(sequence)

        # Count up adenines (A) and thymines (T)
        for nt in sequence:
            if nt == "A" or nt == "T":
                AT_count += 1

        score = (AT_count / length) * 100
        
        # If new high score, store score plus associated header
        if score > top_score:
            top_score = score
            top_header = header

    return top_header, top_score


def main():

    # Parse sequences from test input file
    test_sequences = parse_input('sequences/AT_content/test_input.fasta')

    # Test statements
    top_header, top_score = max_at_content(test_sequences)
    print("\nHighest AT Content Sequence: " + top_header + str(round(top_score, 2)) + "%\n")


if __name__ == "__main__":

    main()
