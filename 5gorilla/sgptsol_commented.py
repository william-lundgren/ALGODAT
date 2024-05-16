# Function to parse the input and create a cost matrix and a list of queries
def parse_input():
    # Read the first line of input and split it into characters
    characters = input().split()
    # Initialize a dictionary to hold the cost matrix
    cost_matrix = {c: {} for c in characters}
    # Fill the cost matrix with the costs of aligning each pair of characters
    for c in characters:
        costs = list(map(int, input().split()))
        for i, cost in enumerate(costs):
            cost_matrix[c][characters[i]] = cost
    # Read the number of queries
    Q = int(input())
    # Read each query and store them in a list
    queries = [input().split() for _ in range(Q)]
    # Return the cost matrix and the list of queries
    return cost_matrix, queries

# Function to align two strings s1 and s2 using the given cost matrix
def align_strings(s1, s2, cost_matrix):
    # Get the lengths of the two strings
    len_s1, len_s2 = len(s1), len(s2)
    # Initialize the DP table with zeros
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    # Initialize the first column of the DP table
    for i in range(len_s1 + 1):
        dp[i][0] = -4 * i
    # Initialize the first row of the DP table
    for j in range(len_s2 + 1):
        dp[0][j] = -4 * j
    # Fill the DP table
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            # Calculate the cost of a match
            match = dp[i-1][j-1] + cost_matrix[s1[i-1]][s2[j-1]]
            # Calculate the cost of deleting from s1
            delete_s1 = dp[i-1][j] - 4
            # Calculate the cost of deleting from s2
            delete_s2 = dp[i][j-1] - 4
            # Choose the maximum cost
            dp[i][j] = max(match, delete_s1, delete_s2)
    # Initialize the aligned strings
    aligned_s1, aligned_s2 = '', ''
    # Backtrack to find the alignment
    i, j = len_s1, len_s2
    while i > 0 and j > 0:
        # Check if the current cell was a match
        if dp[i][j] == dp[i-1][j-1] + cost_matrix[s1[i-1]][s2[j-1]]:
            aligned_s1 = s1[i-1] + aligned_s1
            aligned_s2 = s2[j-1] + aligned_s2
            i -= 1
            j -= 1
        # Check if the current cell was a deletion from s1
        elif dp[i][j] == dp[i-1][j] - 4:
            aligned_s1 = s1[i-1] + aligned_s1
            aligned_s2 = '*' + aligned_s2
            i -= 1
        # Otherwise, it was a deletion from s2
        else:
            aligned_s1 = '*' + aligned_s1
            aligned_s2 = s2[j-1] + aligned_s2
            j -= 1
    # Fill in the remaining characters if one string is longer than the other
    while i > 0:
        aligned_s1 = s1[i-1] + aligned_s1
        aligned_s2 = '*' + aligned_s2
        i -= 1
    while j > 0:
        aligned_s1 = '*' + aligned_s1
        aligned_s2 = s2[j-1] + aligned_s2
        j -= 1
    # Return the aligned strings
    return aligned_s1, aligned_s2

# Main function to run the alignment algorithm
def main():
    # Parse the input to get the cost matrix and queries
    cost_matrix, queries = parse_input()
    # Process each query
    for s1, s2 in queries:
        # Align the strings
        aligned_s1, aligned_s2 = align_strings(s1, s2, cost_matrix)
        # Print the aligned strings
        print(aligned_s1, aligned_s2)

# Standard Python boilerplate to run the main function
if __name__ == "__main__":
    main()
