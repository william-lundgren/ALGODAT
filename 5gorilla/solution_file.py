def parse_input():
    characters = input().split()
    gain_map = {c: {} for c in characters}
    for c in characters:
        costs = list(map(int, input().split()))
        for i, cost in enumerate(costs):
            gain_map[c][characters[i]] = cost
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    return gain_map, queries


def align_strings(s1, s2, gain_map):
    m, n = len(s1), len(s2)
    delta = -4

    # Initiate a zero-filled OPT-matrix (m-1)x(n-1)
    OPT = [[0] * (n + 1) for _ in range(m + 1)]

    # Initiate a zero-filled pred matrix
    # 1 = we came from left
    # 2 = we came from bottom
    # 3 = we came from diagonal
    pred = [[0] * (n + 1) for _ in range(m + 1)]

    # Initiate first row and first column
    for i in range(m + 1):
        pred[i][0] = 2
        OPT[i][0] = delta * i
    for i in range(n + 1):
        pred[0][i] = 1
        OPT[0][i] = delta * i

    # Fill OPT matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = OPT[i - 1][j - 1] + gain_map[s1[i-1]][s2[j-1]]
            left = OPT[i][j - 1] + delta
            bottom = OPT[i - 1][j] + delta
            optval, optpath = max((left, 1), (bottom, 2), (diag, 3))
            OPT[i][j] = optval
            pred[i][j] = optpath

    # construct strings from opt matrix
    s1_aligned = ''
    s2_aligned = ''
    i, j = m, n
    while (i > 0) or (j > 0):
        if pred[i][j] == 1:  # came from left
            s1_aligned = '*' + s1_aligned
            s2_aligned = s2[j-1] + s2_aligned  # CONSUME!
            j -= 1
        elif pred[i][j] == 2:  # came from bottom
            s1_aligned = s1[i-1] + s1_aligned  # CONSUME!
            s2_aligned = '*' + s2_aligned
            i -= 1
        elif pred[i][j] == 3:  # came from diag
            s1_aligned = s1[i-1] + s1_aligned  # CONSUME!
            s2_aligned = s2[j-1] + s2_aligned  # CONSUME!
            i -= 1
            j -= 1
        else:
            print(m, n)
            raise ValueError((i, j))

    return s1_aligned, s2_aligned


def main():
    gain_map, queries = parse_input()
    for s1, s2 in queries:
        aligned_s1, aligned_s2 = align_strings(s1, s2, gain_map)
        print(aligned_s1, aligned_s2)


if __name__ == "__main__":
    main()
