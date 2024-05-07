import sys


class UnionFindElement:
    def __init__(self, index):
        self.index = index
        self.parent = self
        self.root = None #"cache"

    def __eq__(self, other):
        if not isinstance(other, UnionFindElement):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.index == other.index
    
    def __str__(self):
        return str(self.index)

    def find(self):
        if self.parent == self:
            return self
        if self.root is None:
            self.root = self.parent.find()
        # is not the root anymore
        if self.root.root is not None and self.root != self.root.root:
            self.root = self.root.find()
        return self.root
    
    def union(self, other):
        '''Join two sets together. Assuming they are disjoint.'''
        oldroot = self.find()
        newroot = other.find()
        oldroot.parent = newroot
        oldroot.root = newroot
        self.root = newroot


def kruskal(edges, N):
    remainingEdges = edges.copy()
    remainingEdges = sorted(remainingEdges, key=lambda x : x[2]) #Sort on weight
    nodes = [UnionFindElement(i+1) for i in range(N)]
    mst = []
    while remainingEdges:
        edge = remainingEdges.pop(0)
        u = nodes[edge[0]-1]
        v = nodes[edge[1]-1]
        if v.find() != u.find():
            u.union(v)
            mst.append(edge)
        # print(["parent: "+str(e.parent.index)+" root: "+str(e.root) for e in nodes])
    return mst


def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N, M = [int(i) for i in input_lines.pop(0).split()]
    edges = [[int(e) for e in line.split()] for line in input_lines]
    mst = kruskal(edges, N)
    # print(mst)
    s = sum([edge[2] for edge in mst])
    print(s)


if __name__ == "__main__":
    main()
    
    