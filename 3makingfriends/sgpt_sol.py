import sys

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    # graph is in the form: [(weight, node1, node2), ...]
    mst = []
    uf = UnionFind(len(graph))
    graph.sort()  # Sort edges by weight

    for weight, node1, node2 in graph:
        if uf.find(node1) != uf.find(node2):
            uf.union(node1, node2)
            mst.append((weight, node1, node2))

    return mst



def main():

    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N, M = [int(i) for i in input_lines.pop(0).split()]
    edges = [[int(e) for e in line.split()] for line in input_lines]
    edges = [[e[2], e[1]-1, e[0]-1] for e in edges]
    mst = kruskal(edges)
    # print(mst)
    s = sum([edge[0] for edge in mst])
    print(s)

if __name__ == "__main__":
    main()
    
    