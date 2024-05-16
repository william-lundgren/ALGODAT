import time
import sys
from timing import *


def parse_input():
    # Input() takes line by line

    # The range of characters
    characters = input().split()

    # 2D map of cost between two letters signified by key one and key two. gain_map[d][c]=gain_map[c][d] as described
    gain_map = {c: {} for c in characters}

    # For every letter we get a list of the cost to every other letter, loop through all of them
    for c in characters:
        # Convert the costs to int and add to list
        costs = [int(val) for val in input().split()]

        # Add the cost between current character and every other character
        for i, cost in enumerate(costs):
            gain_map[c][characters[i]] = cost
    # Next we get the query amount
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    # Return 2D array and comparisons we want to do
    return gain_map, queries


def align_strings(s1, s2, gain_map):
    # Make som helpful constants
    m, n = len(s1), len(s2)
    delta = -4

    # Initiate a zero-filled OPT-matrix (m-1)x(n-1)
    OPT = [[0] * (n + 1) for _ in range(m + 1)]

    # Initiate a zero-filled prev matrix
    # 1 = we came from left
    # 2 = we came from bottom
    # 3 = we came from diagonal
    prev = [[0] * (n + 1) for _ in range(m + 1)]

    # Initiate first row and first column, since only lateral moment is allowed along 0th elements
    # the prev must be from below or to the left respectively and always move through delta

    tstart = time.time()
    for i in range(m + 1):
        prev[i][0] = 2
        OPT[i][0] = delta * i
    for i in range(n + 1):
        prev[0][i] = 1
        OPT[0][i] = delta * i
    Timer0.timer += time.time() - tstart

    tstart = time.time()
    # Fill OPT matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Loop through everything in OPT starting from 1,1, since we already gave the edges values above

            # Get the cost between the 3 possibilities
            diag = OPT[i - 1][j - 1] + gain_map[s1[i-1]][s2[j-1]]
            left = OPT[i][j - 1] + delta
            bottom = OPT[i - 1][j] + delta

            # Pick the largest between the 3 and remember the path we took. max sorts based on first val in tuple
            optval, optpath = max((left, 1), (bottom, 2), (diag, 3))
            OPT[i][j] = optval
            prev[i][j] = optpath
    TimerOpt.timer += time.time() - tstart

    # construct strings from opt matrix
    s1_aligned = ''
    s2_aligned = ''
    i, j = m, n


    tstart = time.time()
    # While not both i and j are 0 we can still move backwards
    while (i > 0) or (j > 0):
        # Lateral moves means we had to add a character
        if prev[i][j] == 1:  # came from left
            s1_aligned = '*' + s1_aligned
            s2_aligned = s2[j-1] + s2_aligned  # CONSUME!
            j -= 1
        elif prev[i][j] == 2:  # came from bottom
            s1_aligned = s1[i-1] + s1_aligned  # CONSUME!
            s2_aligned = '*' + s2_aligned
            i -= 1

        # diagonal no adding is done so move both
        elif prev[i][j] == 3:  # came from diag
            s1_aligned = s1[i-1] + s1_aligned  # CONSUME!
            s2_aligned = s2[j-1] + s2_aligned  # CONSUME!
            i -= 1
            j -= 1
        else:
            raise ValueError("Incorrect prev matrix")

    TimerAlgo.timer += time.time() - tstart

    return s1_aligned, s2_aligned


def main():
    tstart = time.time()
    gain_map, queries = parse_input()
    sys.stderr.write(f"Parse input: {time.time() - tstart}\n")

    for s1, s2 in queries:
        aligned_s1, aligned_s2 = align_strings(s1, s2, gain_map)
        print(aligned_s1, aligned_s2)
    sys.stderr.write(f"Initialize 0s: {Timer0.timer}\n")
    sys.stderr.write(f"Fill opt: {TimerOpt.timer}\n")
    sys.stderr.write(f"Algorithm thing haha leo: {TimerAlgo.timer}\n")
    sys.stderr.write(f"Time: {time.time()-tstart}\n")



if __name__ == "__main__":
    main()
