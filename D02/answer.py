from typing import List

def safe(report : List[int]) -> int:

    POS = {  1,  2,  3 }
    NEG = { -1, -2, -3 }

    for i in range(1, len(report)):

        POS.add(report[i] - report[i - 1])
        NEG.add(report[i] - report[i - 1])

    return int(len(POS) == 3 or len(NEG) == 3)

def safe_lenient(report : List[int]) -> int:

    for i in range(len(report)):
        if safe(report[: i] + report[i + 1 :]):
            return int(True)
    
    return int(False)

reports = [*map(lambda line : [*map(int, line.split())], open('in.txt').readlines())]

one     = sum(map(safe, reports))
two     = sum(map(safe_lenient, reports))

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")