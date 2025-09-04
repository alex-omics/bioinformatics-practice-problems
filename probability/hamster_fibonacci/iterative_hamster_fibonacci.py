"""
Problem: We start with one pair of breeding hamsters. They produce (litter_size) babies each month. After 
    (months), how many pairs of hamsters will there be?

Stipulations:
    - In this problem, adult hamsters do not die
    - A generation is considered to be one month
    - Hamsters just born take one month to reach sexual maturity
    - The number of pairs born in any given generation equals the number of adult pairs two gens ago

Solution Time Complexity: O(months)
    The loop iterates slightly fewer times than the total number of input months, whichh averages to 
    O(months).

Solution Space Complexity: O(1)
    Here, only simple integers and counters are used to store input information and compute the resulting
    number of hamsters. All of them require a constant amount of space, O(1).
"""

# Hamster Fibonacci solution 1: Iterative
def make_iterative_hams(months, litter_size):

    # Base cases: One or two hamster pairs
    if months <= 2:
        return 1
    
    # Set ham pair values for base cases
    h_i_2 = 1                                   # Pairs of two generations ago
    h_i_1 = 1                                   # Pairs of one generations ago
    
    # Represent the recurrence relation 
    for i in range (3, months + 1):             # Months + 1 to figure out how many pairs in current gen

        adult_pairs = h_i_1                     # All surviving adult hams
        newborn_pairs = litter_size * h_i_2     # Equal to adult pairs from two months ago, times m
        h_i = adult_pairs + newborn_pairs       # H(i) = H(i - 1) + litter_size * H(i - 2)

        # Move index down one 
        h_i_2 = h_i_1                           # H(n - 2) becomes H(n - 1)
        h_i_1 = h_i                             # H(n - 1) becomes H(n), current gen, next iteration begins

    return h_i_1                                # After final iteration of loop, h_i_1 == H(months)


# Create a few test scenarios
colony_1 = make_iterative_hams(4, 12)           # Litters of 12, 4 months
colony_2 = make_iterative_hams(10, 3)           # Litters of 3, 10 months
colony_3 = make_iterative_hams(13, 2)           # Litters of 2, 13 months
colony_4 = make_iterative_hams(29, 3)           # Litters of 3, 29 months

# Test statements
print("\nWith a litter size of 12, after 4 months Colony 1 has " + str(colony_1) + " pairs.")
print("\nWith a litter size of 3, after 10 months Colony 2 has " + str(colony_2) + " pairs.")
print("\nWith a litter size of 2, after 13 months Colony 3 has " + str(colony_3) + " pairs.")
print("\nWith a litter size of 3, after 29 months Colony 3 has " + str(colony_4) + " pairs.\n")
