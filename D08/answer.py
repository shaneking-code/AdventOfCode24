from collections import defaultdict
from itertools   import product

iterator = [(i, row, j, cell) for i, row in enumerate(open('in.txt')) for j, cell in enumerate(row.strip())]
input    = { complex(i, j) : cell for i, _, j, cell in iterator }
freqs    = defaultdict(set)
for i, _, j, cell in iterator: 
    if cell != '.': freqs[cell] |= { complex(i, j)}

ones, twos = set(), set()
for freq in freqs:
    for a, b in product(freqs[freq], repeat=2):
        delta = b - a
        if delta == 0:
            continue
        def trace(start, delta):
            global ones, twos
            k = 1
            while input.get(start + k * delta, '!') != '!':
                twos |= { start + k * delta }
                if k == 2:
                    ones |= { start + k * delta }
                k += 1
            while input.get(start - k * delta, '!') != '!':
                twos |= { start - k * delta }
                if k == 1:
                    ones |= { start - k * delta }
                k += 1
        trace(a, delta)

one = len(ones)
two = len(twos)

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")

