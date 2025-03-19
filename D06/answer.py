M = {
    complex(i, j) : cell for i, row in enumerate(open('in.txt')) for j, cell in enumerate(row.strip()) 
}

start, *_ = [ p for p in M if M[p] == '^' ]

def path(M):

    pos  = start
    dir  = -1
    seen = set()

    while pos in M and (pos, dir) not in seen:

        seen.add((pos, dir))

        if M.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir

    return { p for p, _ in seen }, (pos, dir) in seen 

walk, _ = path(M) 

one = len(walk)
two = sum(map(lambda M : path(M)[1], map(lambda p : M | { p : "#" }, walk)))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")