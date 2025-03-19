from functools import cache 

@cache
def blink(stone : int, depth : int = 75) -> int:

    s = str(stone)
    l = len(s)

    if depth == 0:
        return 1
     
    elif stone == 0:
        return blink(1, depth - 1)

    elif l % 2 == 0:
        return (blink(int(s[:(l//2)]), depth - 1) + blink(int(s[(l//2):]), depth - 1))

    else:
        return blink(stone * 2024, depth - 1)

two = sum(map(blink, map(int, open('in.txt').read().split())))
print(f"answer to part two is {two}")

