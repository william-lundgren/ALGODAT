import sys


class UnionFind:
    def __init__(self):
        self.parent = self
        self.root = None

    def union(self, other):
        other.find().parent = self

    def find(self):
        if self.parent == self:
            return self
        if self.root is None:
            self.root = self.parent.find()
        return self.root


def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))


if __name__ == "__main__":
    main()
