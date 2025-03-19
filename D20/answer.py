from collections import defaultdict
from heapq       import heappush, heappop
from itertools   import product

grid  = {
    complex(i, j) : cel for i, row in enumerate(open('in.txt').readlines())
                        for j, cel in enumerate(row.strip())
}

start = [c for c in grid if grid[c] == 'S'][0]
end   = [c for c in grid if grid[c] == 'E'][0]
walls = {c for c in grid if grid[c] == '#'}

def dijkstras(root: complex) -> dict:

    dist = defaultdict(lambda: float('inf'))
    dist[root] = 0

    seen = set()
    heap = [(0, t:=0, root)]

    while heap:

        _, _, u = heappop(heap)
        if u in seen:
            continue
        seen.add(u)

        for v in [u + 1j ** n for n in range(4)]:
            if grid.get(v, '#') != '#':
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                heappush(heap, (dist[v], t:=t+1, v))

    return dist

d2s, d2e = dijkstras(start), dijkstras(end)

def ball(i: int, j: int, radius: int) -> set:
    return set(map(lambda t: complex(*t), product(range(i - radius, i + radius + 1), range(j - radius, j + radius + 1))))
                
def d(u: complex, v: complex) -> int:
    z = u - v
    return abs(z.real) + abs(z.imag)

def optimal_cheats(cheat_length: int) -> int:

    d_naive = d2e[start]
    cheats  = set()

    for cheat_start in grid.keys() - walls:
        i_0, j_0 = int(cheat_start.real), int(cheat_start.imag)
        search_space = ball(i_0, j_0, cheat_length)

        for cheat_end in search_space - walls:
            d_skipped = d(cheat_start, cheat_end)
            if d_skipped <= cheat_length:
                d_cheat = d2s[cheat_start] + d_skipped + d2e[cheat_end]
                if d_naive - d_cheat >= 100:
                    cheats.add((cheat_start, cheat_end))

    return len(cheats)

one = optimal_cheats(2)
two = optimal_cheats(20)

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")