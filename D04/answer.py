GRID = [*map(str.strip, open('in.txt').readlines())]
DIRS = {"e": (1, 0), "w": (-1, 0), "n": (0, 1), "s": (0, -1), "ne": (1, 1), "nw": (-1, 1), "se": (1, -1), "sw": (-1, -1)}
EXES =(a:=("S", "S", "M", "M"), b:=("S", "M", "S", "M"), a[::-1], b[::-1])

one  = sum((dfs := lambda x, y, i, d : i == len("XMAS") or (0 <= x < len(GRID) and 0 <= y < len(GRID[0]) and GRID[x][y] == "XMAS"[i] and dfs(x + DIRS[d][0], y + DIRS[d][1], i + 1, d)))(r, c, 0, d) for r in range(len(GRID)) for c in range(len(GRID[0])) if GRID[r][c] == "X" for d in DIRS)
two  = sum((lambda r, c : (0 < r <= len(GRID) - 2 and 0 < c <= len(GRID[0]) - 2) and ((GRID[r-1][c+1], GRID[r-1][c-1], GRID[r+1][c+1], GRID[r+1][c-1]) in VALID))(r, c) for r in range(len(GRID)) for c in range(len(GRID[0])) if GRID[r][c]=="A")

print(f"answer to part one is {one}")  
print(f"answer to part two is {two}")
    
        
