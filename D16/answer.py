from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import Callable, List
from pprint import pprint
from functools import cache
def maze(input : str):

    start, end = complex(0, 0), complex(0, 0)
    grid = {}

    for i, row in enumerate(open(input).readlines()):
        for j, cell in enumerate(row.strip()):
            if cell == "S":
                start = complex(i, j)
            if cell == "E":
                end = complex(i, j)
            grid[complex(i, j)] = cell
    
    return grid, start, end
def dist(u : complex, v : complex) -> int:
    return abs(v.real - u.real) + abs(v.imag - u.imag)
def path(prevs : dict, curr : complex, curr_dir : complex):
    p = [curr]
    while (curr, curr_dir) in prevs:
        curr, curr_dir = prevs[(curr, curr_dir)]
        p.append(curr)
    return p[::-1]
def A_star(grid : dict, start : complex, start_dir : complex, end : complex) -> tuple[List[complex], int]:

    start_state = (start, start_dir)

    openSet = [(0, 0, start_state)]
    seen    = set([start_state])
    prevs   = {}

    gScore  = defaultdict(lambda : float('inf'))
    gScore[start_state] = 0

    timestamp = 1
    while openSet:
        _, _, (curr, curr_dir) = heappop(openSet)

        if curr == end:
            return path(prevs, curr, curr_dir), gScore[(curr, curr_dir)]

        forward_neighbor = curr + curr_dir
        if grid.get(forward_neighbor, "#") != "#":
            forward_state = (forward_neighbor, curr_dir)
            est_forward_score = gScore[(curr, curr_dir)] + 1
            if est_forward_score < gScore[forward_state]:
                prevs[forward_state] = (curr, curr_dir)
                gScore[forward_state] = est_forward_score

                if forward_state not in seen:
                    f_score = est_forward_score + dist(forward_neighbor, end)
                    heappush(openSet, (f_score, timestamp, forward_state))
                    seen.add(forward_state)
                    timestamp += 1

        for rotation in [-1j, 1j]:
            new_dir = curr_dir * rotation
            new_state = (curr, new_dir)

            est_rotate_score = gScore[(curr, curr_dir)] + 1000
            if est_rotate_score < gScore[new_state]:
                prevs[new_state] = (curr, curr_dir)
                gScore[new_state] = est_rotate_score

                if new_state not in seen:
                    f_score = est_rotate_score + dist(curr, end)
                    heappush(openSet, (f_score, timestamp, new_state))
                    seen.add(new_state)
                    timestamp += 1

    return [], 0

grid, start, end = maze('in.txt')
"""
p, score = A_star(grid, start, 0 + 1j, end)
seats = set(p)
for direction in [ -1j ** n for n in range(4) ]:
    if grid.get(end + direction, '#') != '#':
        p_, new_score = A_star(grid, end, direction, start)
        if new_score == score:
            seats.union(set(p_))
"""


