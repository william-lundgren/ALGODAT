import sys
import time


class Graph:
    #Contains main graph data (edges, nodes), aswell as our new MST-forest data (parent, rank)
    def __init__(self, N, edges):
        self.N = N
        self.edges = sorted(edges, key=lambda x: x[2])
        self.parent = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
   
    #combine the trees of which x and y belongs. Assuming they are disjoint
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        #Union by rank (see union-find on wikipedia). Essentially we want to keep track of the height of each tree.
        #The lowest rank tree is added to the higher tree, in order to keep the trees as flat as possible (and avoid long recursive stuff)
        if self.rank[x] < self.rank[y]:
            x, y = (y,x)
        
        self.parent[y] = x
        if self.rank[x]== self.rank[y]:
            self.rank[x] += 1
        
    #Find the root of a node x
    def find(self, x):
        if self.parent[x] == x: #Basfall
            return x
        else:
            self.parent[x] = self.find(self.parent[x]) #attempt at "path compression"?. Should flatten the tree.
        return self.parent[x]


    def kruskal(self): #Kruskals algorithm. Assumes the edges are sorted in descending order
        mst = []
        for e in self.edges:
            u = e[0]-1
            v = e[1]-1
            if self.find(v) != self.find(u): #Any edge between two disjoint trees is safe. Add it.
                self.union(u,v)
                mst.append(e)
        return mst


def main():
    tstart = time.time()

    #Parse
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N, M = [int(i) for i in input_lines.pop(0).split()]
    sys.stderr.write(f"Setup time: {time.time()-tstart}\n") # ugly way of displaying time stats while not rendering checksolution.sh unusuable
    edges = [[int(e) for e in line.split()] for line in input_lines]
    
    g = Graph(N, edges)
    sys.stderr.write(f"Total time before kruskal: {time.time()-tstart}\n")
    mst = g.kruskal()
    s = sum([edge[2] for edge in mst]) #MST total wheight
    sys.stderr.write(f"Total time: {time.time()-tstart}\n") 
    print(s)

if __name__ == "__main__":
    main()
