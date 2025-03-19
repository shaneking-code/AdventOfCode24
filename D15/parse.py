grid, moves = open('in.txt').read().split('\n\n')

grid = [*map(list, grid.split('\n'))]

class Move:
    def __init__(self, y, x):
        self.dy = y
        self.dx = x

moves = [move for move in moves if move != '\n']

# y, x
str2move = {
    'v' : Move(1, 0),
    '^' : Move(-1, 0),
    '>' : Move(0, 1),
    '<' : Move(0, -1)
}
move2str = {
    value : key for key, value in str2move.items()
}
moves = [*map(lambda move : str2move[move], moves)]

start = ()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '@':
            start = (y, x)
