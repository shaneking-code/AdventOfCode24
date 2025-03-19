from parse import Move, grid, moves, start, move2str
from pprint import pprint
y, x = start
for i, move in enumerate(moves):
    print("move #", i + 1)
    print("move = ", move2str[move])
    pprint(["".join(row) for row in grid])
    print()
    if grid[y + move.dy][x + move.dx] == '#':
        continue
    elif grid[y + move.dy][x + move.dx] == 'O':
        chain = ['@']
        n = 1
        while grid[y + n * move.dy][x + n * move.dx] == 'O':
            chain.append(grid[y + n * move.dy][x + n * move.dx])
            n += 1
        if grid[y + n * move.dy][x + n * move.dx] == '#':
            continue
        else:
            chain.insert(0, grid[y + n * move.dy][x + n * move.dx])
            if move.dy == 0:
                print("CHAIN = ", chain)
                if move.dx > 0:
                    grid[y][x : x + len(chain)] = chain
                else:
                    grid[y][x - len(chain) + 1 : x + 1] = chain[::-1]
            else:
                print("CHAIN = ", chain)
                if move.dy > 0:
                    for i in range(0, len(chain)):
                        grid[y + i][x] = chain[i]
                else:
                    for i in range(0, len(chain)):
                        grid[y - i][x] = chain[i]

        y += move.dy
        x += move.dx
    else:
        old_y, old_x = y, x
        y += move.dy
        x += move.dx
        grid[old_y][old_x], grid[y][x] = grid[y][x], grid[old_y][old_x]

print("at the end")
pprint(["".join(row) for row in grid])

t = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'O':
            t += (100 * y + x)

print(t)

    