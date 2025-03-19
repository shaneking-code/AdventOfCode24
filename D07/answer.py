from operator  import add, mul
from functools import reduce

eqs = [*map(lambda equation : [int(equation[0]), [*map(int, equation[1].split())]], [*map(lambda line : line.split(":"), open("in.txt").read().splitlines())])]
cat = lambda x, y : int(str(x) + str(y))

def test(answer, values, ops):
    def dfs(acc=(values[0] if len(ops)==3 else 0), i=(1 if len(ops)==3 else 0)):
        if i == len(values):
            return acc == answer
        return any([dfs((op(acc, values[i])), i + 1) for op in ops])
    return dfs()

one = reduce(add, (e[0] for e in filter(lambda e : test(*e, [add, mul]), eqs)))
two = reduce(add, (e[0] for e in filter(lambda e : test(*e, [add, mul, cat]), eqs)))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")


