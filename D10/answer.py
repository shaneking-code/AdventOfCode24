from collections import defaultdict
from typing      import List

grid  = {
    complex(i, j) : int(cell) for i, row  in enumerate(open('in.txt'))
                              for j, cell in enumerate(row.strip())
}
heads = [ key for key in grid if grid[key] == 0 ]

def traverse(head : complex) -> tuple[int, int]:

    routes = defaultdict(set)
    def dfs(node : complex, prev : complex = None, path : List = []) -> None:

        if node not in grid or not grid.get(node) == grid.get(prev, -1) + 1:
            return
        if grid.get(node) == 9:
            routes[node].add(tuple(path))
            return
        
        for neighbor in [node + 1j ** n for n in range(4)]:
            dfs(neighbor, node, path + [node])

    dfs(head)
    return len(routes), sum(map(len, routes.values()))

one, two = map(sum, zip(*map(traverse, heads)))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")
        
