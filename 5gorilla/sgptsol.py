def parse_input():
    characters = input().split()
    cost_matrix = {c: {} for c in characters}
    for c in characters:
        costs = list(map(int, input().split()))
        for i, cost in enumerate(costs):
            cost_matrix[c][characters[i]] = cost
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    return cost_matrix, queries

def align_strings(s1, s2, cost_matrix):
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(len_s1 + 1):
        dp[i][0] = -4 * i
    for j in range(len_s2 + 1):
        dp[0][j] = -4 * j
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            match = dp[i-1][j-1] + cost_matrix[s1[i-1]][s2[j-1]]
            delete_s1 = dp[i-1][j] - 4
            delete_s2 = dp[i][j-1] - 4
            dp[i][j] = max(match, delete_s1, delete_s2)
    aligned_s1, aligned_s2 = '', ''
    i, j = len_s1, len_s2
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + cost_matrix[s1[i-1]][s2[j-1]]:
            aligned_s1 = s1[i-1] + aligned_s1
            aligned_s2 = s2[j-1] + aligned_s2
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j] - 4:
            aligned_s1 = s1[i-1] + aligned_s1
            aligned_s2 = '*' + aligned_s2
            i -= 1
        else:
            aligned_s1 = '*' + aligned_s1
            aligned_s2 = s2[j-1] + aligned_s2
            j -= 1
    while i > 0:
        aligned_s1 = s1[i-1] + aligned_s1
        aligned_s2 = '*' + aligned_s2
        i -= 1
    while j > 0:
        aligned_s1 = '*' + aligned_s1
        aligned_s2 = s2[j-1] + aligned_s2
        j -= 1
    return aligned_s1, aligned_s2

def main():
    cost_matrix, queries = parse_input()
    for s1, s2 in queries:
        aligned_s1, aligned_s2 = align_strings(s1, s2, cost_matrix)
        print(aligned_s1, aligned_s2)

if __name__ == "__main__":
    main()
