from collections import defaultdict
from heapq import heappush, heappop
from itertools import product

grid = {
        complex(i, j) : cel for i, row in enumerate(open('in.txt').readlines())
                            for j, cel in enumerate(row.strip())
    }
start = [c for c in grid if grid[c] == 'S'][0]
end   = [c for c in grid if grid[c] == 'E'][0]
def find_optimal_cheats(grid, start, end, max_cheat_duration):
    # Get base distances using Dijkstra's
    base_distances = dijkstra(grid, start)
    reverse_distances = dijkstra(grid, end)
    
    cheats = set()
    height = max(int(pos.real) for pos in grid) + 1
    width = max(int(pos.imag) for pos in grid) + 1
    
    # For each possible cheat start position
    for start_row, start_col in product(range(height), range(width)):
        start_pos = complex(start_row, start_col)
        if grid.get(start_pos, '#') == '#':
            continue
            
        # For each possible end position within cheat range
        for end_row, end_col in product(range(height), range(width)):
            end_pos = complex(end_row, end_col)
            if grid.get(end_pos, '#') == '#':
                continue
                
            # Check if positions are within cheat range
            if manhattan_dist(start_pos, end_pos) <= max_cheat_duration:
                # Calculate total path length with cheat
                path_with_cheat = (base_distances[start_pos] + 
                                 manhattan_dist(start_pos, end_pos) +
                                 reverse_distances[end_pos])
                
                # Calculate original path length
                original_path = base_distances[end]
                
                time_saved = original_path - path_with_cheat
                if time_saved >= 100:
                    cheats.add((start_pos, end_pos))
                    
    return len(cheats)

def manhattan_dist(pos1, pos2):
    return int(abs(pos1.real - pos2.real) + abs(pos1.imag - pos2.imag))

def dijkstra(grid, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = [(0, start)]
    seen = set()
    
    while queue:
        dist, current = heappop(queue)
        if current in seen:
            continue
        seen.add(current)
        
        for direction in [1, -1, 1j, -1j]:
            next_pos = current + direction
            if grid.get(next_pos, '#') != '#':
                new_dist = dist + 1
                if new_dist < distances[next_pos]:
                    distances[next_pos] = new_dist
                    heappush(queue, (new_dist, next_pos))
    
    return distances

print(find_optimal_cheats(grid, start, end, 2))
print(find_optimal_cheats(grid, start, end, 20))