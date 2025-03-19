from __future__  import annotations
from collections import deque
from itertools   import product
from typing      import List

DIRS = set([ 1j ** n for n in range(4) ])

class BoundaryNode:

    def __init__(self, pos : complex, dir : complex) -> None:

        self.pos = pos
        self.dir = dir

    def __eq__(self, other : BoundaryNode) -> bool:

        return self.pos == other.pos and self.dir == other.dir
    
    def __key(self) -> tuple[complex, complex]:

        return (self.pos, self.dir)
    
    def __hash__(self) -> int:

        return hash(self.__key())

class DisjointSet:

    def __init__(self, nodes : List[BoundaryNode]) -> None:

        self.parent = { node : node for node in nodes }
        self.rank   = { node : 0 for node in nodes }

    def find(self, node : BoundaryNode) -> BoundaryNode:

        while self.parent[node] != node:
            node, self.parent[node] = self.parent[node], self.parent[self.parent[node]]

        return self.parent[node]
    
    def union(self, u : BoundaryNode, v : BoundaryNode) -> bool:

        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu

        self.parent[pv] = pu

        if self.rank[pu] == self.rank[pv]:
            self.rank[pu] += 1

        return True

def count_sides(boundary : List[BoundaryNode]) -> int:

    dju = DisjointSet(boundary)

    for u, v in product(boundary, repeat=2):
        if u != v and u in { BoundaryNode(v.pos + dir, v.dir) for dir in DIRS - set([v.dir]) }:
            dju.union(u, v)
    
    sides = set(dju.find(node) for node in boundary)

    return len(sides)

def bfs(grid : dict, root : complex) -> tuple[int, int, int, set]:

    plant    = grid[root]
    region   = set([root])
    queue    = deque([root])
    boundary = []

    while queue:
        node = queue.pop()
        for neighbor, dir in [ (node + dir, dir) for dir in DIRS ]:
            if not grid.get(neighbor) == plant:
                boundary.append(BoundaryNode(neighbor, dir))
            if grid.get(neighbor) == plant and neighbor not in region:
                region.add(neighbor)
                queue.appendleft(neighbor)

    perim = len(boundary)
    sides = count_sides(boundary)
    area  = len(region)

    return perim, sides, area, region

grid = {
    complex(i, j) : cell for i, row in enumerate(open('in.txt').readlines())
                         for j, cell in enumerate(row.strip())
}

plots = set(grid.keys())
one   = 0
two   = 0

while plots:

    pos = plots.pop()
    perim, sides, area, region = bfs(grid, pos)

    one   += perim * area
    two   += sides * area
    plots -= region

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")

