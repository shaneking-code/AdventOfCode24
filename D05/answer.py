from functools import cmp_to_key

rules = [*map(lambda rule : [*map(int, rule.split("|"))], (a:=[*map(lambda chunk : chunk.split("\n"), open('in.txt').read().split("\n\n"))])[0])]
pages = [*map(lambda page : [*map(int, page.split(','))], a[1])]

one = sum(map(mid:=lambda page : page[len(page)//2], filter(checkpage:=lambda page : not any([[page[i + 1], page[i]] in rules for i in range(len(page) - 1)]), pages)))
two = sum(map(mid, map(lambda page : sorted(page, key=cmp_to_key(lambda a, b : -1 if [a, b] in rules else (1 if [b, a] in rules else 0))), filter(lambda page : not checkpage(page), pages))))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")






