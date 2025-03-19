import heapq
from typing import List, Tuple, Set

class ReindeerMazeSolver:
    def __init__(self, maze: List[str]):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.start = self.find_start()
        self.end = self.find_end()
        
        # Directions: East (0), North (1), West (2), South (3)
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    def find_start(self) -> Tuple[int, int]:
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return (y, x)
        raise ValueError("No start position found")
    
    def find_end(self) -> Tuple[int, int]:
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'E':
                    return (y, x)
        raise ValueError("No end position found")
    
    def is_valid_move(self, y: int, x: int) -> bool:
        return 0 <= y < self.height and 0 <= x < self.width and self.maze[y][x] != '#'
    
    def is_movable_tile(self, y: int, x: int) -> bool:
        return self.maze[y][x] in '.SE'
    
    def find_optimal_path_nodes(self) -> Set[Tuple[int, int]]:
        # State tracking for optimal paths
        best_score = float('inf')
        optimal_path_nodes = set()
        
        # State to explore: (total_score, current_score, path_nodes, y, x, direction)
        start_state = (0, 0, {self.start}, self.start[0], self.start[1], 0)  # Initially facing East
        states_to_explore = [start_state]
        
        # Track visited states to manage exploration efficiently
        visited = set()
        best_solution_paths = []
        
        while states_to_explore:
            total_score, current_score, path_nodes, y, x, direction = heapq.heappop(states_to_explore)
            
            # Pruning: stop exploring if exceeding best score
            if total_score > best_score:
                continue
            
            # Reached the end
            if (y, x) == self.end:
                if total_score < best_score:
                    best_score = total_score
                    best_solution_paths = [path_nodes]
                elif total_score == best_score:
                    best_solution_paths.append(path_nodes)
                continue
            
            # State tracking to avoid redundant explorations
            state_key = (y, x, direction)
            if state_key in visited:
                continue
            visited.add(state_key)
            
            # Try moving forward
            ny, nx = y + self.directions[direction][0], x + self.directions[direction][1]
            if self.is_valid_move(ny, nx):
                new_path_nodes = path_nodes.copy()
                new_path_nodes.add((ny, nx))
                new_state = (
                    total_score + 1, 
                    current_score + 1, 
                    new_path_nodes, 
                    ny, nx, 
                    direction
                )
                heapq.heappush(states_to_explore, new_state)
            
            # Try rotating clockwise
            clockwise_dir = (direction + 1) % 4
            clockwise_state = (
                total_score + 1000, 
                current_score + 1000, 
                path_nodes.copy(), 
                y, x, 
                clockwise_dir
            )
            heapq.heappush(states_to_explore, clockwise_state)
            
            # Try rotating counterclockwise
            counterclockwise_dir = (direction - 1 + 4) % 4
            counterclockwise_state = (
                total_score + 1000, 
                current_score + 1000, 
                path_nodes.copy(), 
                y, x, 
                counterclockwise_dir
            )
            heapq.heappush(states_to_explore, counterclockwise_state)
        
        # Combine all optimal path nodes
        optimal_nodes = set()
        for path in best_solution_paths:
            optimal_nodes.update(path)
        
        return optimal_nodes

def solve_reindeer_maze(maze: List[str]) -> int:
    solver = ReindeerMazeSolver(maze)
    optimal_nodes = solver.find_optimal_path_nodes()
    
    # Additional validation to match problem description
    valid_count = sum(
        1 for y in range(len(maze)) 
        for x in range(len(maze[0])) 
        if (y, x) in optimal_nodes and solver.is_movable_tile(y, x)
    )
    
    return valid_count

# Example mazes from the problem description
maze1 = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]

maze2 = [
    "#################",
    "#...#...#...#..E#",
    "#.#.#.#.#.#.#.#.#",
    "#.#.#.#...#...#.#",
    "#.#.#.#.###.#.#.#",
    "#...#.#.#.....#.#",
    "#.#.#.#.#.#####.#",
    "#.#...#.#.#.....#",
    "#.#.#####.#.###.#",
    "#.#.#.......#...#",
    "#.#.###.#####.###",
    "#.#.#...#.....#.#",
    "#.#.#.#####.###.#",
    "#.#.#.........#.#",
    "#.#.#.#########.#",
    "#S#.............#",
    "#################"
]

# Run solutions for example mazes
for i, maze in enumerate([maze1, maze2], 1):
    result = solve_reindeer_maze(maze)
    print(f"Maze {i} - Best Path Tiles: {result}")