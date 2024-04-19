import sys


def has_edge(u, v):
    v = list(v)

    for letter in u[1:]:
        try:
            v.remove(letter)
        except ValueError:
            continue

    return len(v) == 1


def BFS(start, end, edges):
    if start == end:
        return 0

    visited = {key: False for key in list(edges.keys())}
    visited[start] = True
    pred = {key: None for key in list(edges.keys())}
    q = [start]
    finished = False

    while len(q) > 0 and not finished:
        v = q.pop()

        # Neighbors
        for w in edges[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                pred[w] = v
                if w == end:
                    finished = True
                    break

    if finished:
        count = 0
        node = w
        while node != start:
            node = pred[node]
            count += 1
        return count
    else:
        return "Impossible"


def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N, Q = input_lines[0].split()
    N, Q = int(N), int(Q)

    words = input_lines[1: N + 1]
    queries = [s.split() for s in input_lines[N + 1:]]

    # CREATE TREE TIME
    edges = {
    }

    # initialize the edges dict
    for word in words:
        edges[word] = []


    while len(words) > 0:
        key_word = words.pop()
        for value_word in words:
            if has_edge(key_word, value_word):
                edges[key_word].append(value_word)

            if has_edge(value_word, key_word):
                edges[value_word].append(key_word)

    # BFS TIME
    for query in queries:
        start, end = query[0], query[1]
        print(BFS(start, end, edges))


if __name__ == "__main__":
    main()
