import sys
import time


def has_edge(u, v):
    v = list(v)

    for letter in u[1:]:
        try:
            v.remove(letter)
        except ValueError:
            continue

    return len(v) == 1


def get_children(word, edges, words):
    #print(edges)
    if word in edges:
        return edges[word]
    else:
        key_word = word #words.pop()
        edges[key_word] = []
        for value_word in words:
            if has_edge(key_word, value_word):
                edges[key_word].append(value_word)
        return edges[key_word]


def BFS(start, end, edges, words):
    if start == end:
        return 0

    visited = {word: False for word in words}
    visited[start] = True
    pred = {word: None for word in words}
    q = [start]
    finished = False

    while len(q) > 0 and not finished:
        v = q.pop(0)

        # Neighbors
        for w in get_children(v,edges, words):
            
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

    #t_start = time.time()

    # CREATE TREE TIME
    edges = {
    }

    # # initialize the edges dict
    # for word in words:
    #     edges[word] = []
        

    #print(time.time()-t_start)

    # BFS TIME
    for query in queries:
        start, end = query[0], query[1]
        print(BFS(start, end, edges, words))

    #print(time.time()-t_start)
    #print(len(edges))


if __name__ == "__main__":
    main()
