import sys
import time

def has_edge(u, v):
    v = list(v)
    u = list(u[1:])
    strike = False

    for i, vlet in enumerate(v):
        for j, ulet in enumerate(u):
            if vlet != ulet:
                if strike:
                    return False
                else:
                    strike = True
            else:
                u.pop(j)
                break

    return True


def BFS(start, end, edges):
    if start == end:
        return 0

    visited = {key: False for key in list(edges.keys())}
    visited[start] = True
    pred = {key: None for key in list(edges.keys())}
    q = [start]
    finished = False

    while len(q) > 0 and not finished:
        v = q.pop(0)

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
        node = end
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

    t_start = time.time()

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

    print(time.time()-t_start)

    # BFS TIME
    for query in queries:
        start, end = query[0], query[1]
        (BFS(start, end, edges))

    print(time.time()-t_start)


if __name__ == "__main__":
    main()
