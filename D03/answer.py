from re        import findall, DOTALL
from functools import reduce
from operator  import mul, concat

one = sum(map(eval, findall(r'mul\(\d+,\d+\)', open('in.txt').read())))
two = sum(map(eval, reduce(concat, map(lambda m : findall(r'mul\(\d+,\d+\)', m), findall(r'do\(\)(.*?)don\'t\(\)', "do()" + open("in.txt").read(), DOTALL)))))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")