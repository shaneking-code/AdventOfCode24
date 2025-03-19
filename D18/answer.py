from collections import defaultdict
from heapq       import heappush, heappop

input = list(map(lambda line : list(map(int, line.split(','))), open('in.txt').readlines()))
ROWS = COLS = 71
grid = {
    complex(i, j) : '.' for i in range(ROWS)
                        for j in range(COLS)
}

def bfs(grid, start, end):

    dist = defaultdict(lambda: float('inf'))
    seen = set()

    dist[start] = 0
    pq = [(0, t:=0, start)]
    while pq:
        _, _, u = heappop(pq)
        if u == end:
            return dist[u]
        if u in seen:
            continue
        seen.add(u)

        for v in [u + 1j ** n for n in range(4)]:
            if grid.get(v, '#') != '#':
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                heappush(pq, (dist[v], t, v))
                t += 1
    return -1

for i, j in input[:1024]:
    grid[complex(i, j)] = '#'

start, end = complex(0, 0), complex(ROWS - 1, COLS - 1)
one = bfs(grid, start, end)

byte = 1024
while bfs(grid, start, end) > 0:
    i, j = input[byte]
    grid[complex(i, j)] = '#'
    byte += 1

two = input[byte - 1]

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")
    
