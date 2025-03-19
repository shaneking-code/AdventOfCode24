from re           import findall
from numpy        import log, zeros, printoptions, inf, uint8
from typing       import List
from scipy.linalg import svdvals
from heapq        import heappush, heappop
from operator     import mul, truth
from functools    import reduce
from pprint       import pprint
from PIL          import Image as im
class Grid:
    def __init__(self, width : int, height : int) -> None:

        self.cells  = zeros((height, width), dtype=int)
        self.width  = width
        self.height = height

    def quadproduct(self):

        w, h = self.width // 2, self.height // 2
        quads = [0] * 4

        quads[0] = self.cells[:h, :w].sum()
        quads[1] = self.cells[:h, (w + 1):].sum()
        quads[2] = self.cells[(h + 1):, :w].sum()
        quads[3] = self.cells[(h + 1):, (w + 1):].sum()

        return reduce(mul, quads)
    
class Robot:
    def __init__(self, specs : tuple[int, int, int, int], grid : Grid) -> None:

        self.px, self.py, self.vx, self.vy = specs
        grid.cells[self.py, self.px] += 1

    def move(self, grid : Grid, steps : int = 1) -> None:

        grid.cells[self.py, self.px] -= 1
        self.px = (self.px + steps * self.vx) % grid.width
        self.py = (self.py + steps * self.vy) % grid.height
        grid.cells[self.py, self.px] += 1

def parse(input : str) -> List[List[int]]:
        
        specs = [
            [ int(n) for n in findall(r'-?\d+', line) ]
            for line in open(input).readlines()
        ]

        return specs

WIDTH, HEIGHT  = 101, 103
grid   = Grid(WIDTH, HEIGHT)
robots = [ *map(lambda spec : Robot(spec, grid), parse('in.txt')) ]

entropies = []

# part one

for robot in robots:
    robot.move(grid, 100)

one = grid.quadproduct()

# part two

for i in range(100, 7790):
    for robot in robots:
        robot.move(grid)
    
    vals = filter(truth, svdvals(grid.cells))
    vne  = sum(map(lambda v : v * log(v), vals))
    heappush(entropies, (vne, i + 1))

_, two = heappop(entropies)

# Convert the grid.cells to uint8
grid.cells *= 254
image_array = grid.cells.astype(uint8)
pic = im.fromarray(image_array)
pic.save('out.png')

#print(f"answer to part one is {one}")
#print(f"answer to part two is {two}")