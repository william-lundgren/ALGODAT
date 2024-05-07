import sys
import time


class Graph:
    def __init__(self, N, edges):
        self.N = N
        self.edges = sorted(edges, key=lambda x: x[2])
        self.parent = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
   
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if self.rank[x] < self.rank[y]:
            x, y = (y,x)
        
        self.parent[y] = x
        if self.rank[x]== self.rank[y]:
            self.rank[x] += 1
        

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
            self.parent[x] = self.find(self.parent[x])
        return self.parent


    def kruskal(self):
        startt = time.time()
        mst = []
        for e in self.edges:
            u = e[0]-1
            v = e[1]-1
            if self.find(v) != self.find(u):
                self.union(u,v)
                mst.append(e)
        return mst


def main():

    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N, M = [int(i) for i in input_lines.pop(0).split()]
    edges = [[int(e) for e in line.split()] for line in input_lines]
    g = Graph(N, edges)
    mst = g.kruskal()
    # print(mst)
    s = sum([edge[2] for edge in mst])
    print(s)

if __name__ == "__main__":
    main()
