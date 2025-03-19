from heapq import heappop, heappush

grid = {i+j*1j: c for i,r in enumerate(open('in.txt'))
                  for j,c in enumerate(r) if c != '#'}

start, = (p for p in grid if grid[p] == 'S')

good = set()
seen = set()
todo = [(0, t:=0, start, 1j, [start])]

while todo:
    val, _, pos, dir, path = heappop(todo)
    seen.add((pos, dir))

    if grid[pos] == 'E':
        print(val)
        best = val
        good.update(path)

    for r, v in (1, 1), (+1j, 1001), (-1j, 1001):
        v, t, p, d = val+v, t+1, pos + dir*r, dir*r
        if p not in grid or (p,d) in seen: continue
        heappush(todo, (v, t, p, d, path + [p]))

print(best, len(good))