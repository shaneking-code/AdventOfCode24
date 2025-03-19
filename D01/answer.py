one    = sum(map(lambda l, r : abs(l - r), left:=sorted((list:=[*map(int, open('in.txt').read().split())])[0::2]), right:=sorted(list[1::2])))
two    = sum(map(lambda l : l * right.count(l), left))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")
