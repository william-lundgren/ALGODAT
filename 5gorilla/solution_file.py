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
    pass

def main():
    cost_matrix, queries = parse_input()
    for s1, s2 in queries:
        aligned_s1, aligned_s2 = align_strings(s1, s2, cost_matrix)
        print(aligned_s1, aligned_s2)

if __name__ == "__main__":
    main()