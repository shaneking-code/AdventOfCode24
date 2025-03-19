"""
In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

Calculate the result of multiplying the secret number by 64 = 2 ** 6.
Then, mix this result into the secret number. 
Finally, prune the secret number.

Calculate the result of dividing the secret number by 32 = 2 ** 5.
Round the result down to the nearest integer. Then, mix this result into the secret number.
Finally, prune the secret number.

Calculate the result of multiplying the secret number by 2048 = 2 ** 11.
Then, mix this result into the secret number.
Finally, prune the secret number.
Each step of the above process involves mixing and pruning:

To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number.
To prune the secret number, calculate the value of the secret number modulo 16777216 = 2 ** 24.
"""

from functools import cache, reduce
from math import floor
from typing import Any, Callable

steps = { 0 : 2 ** 6, 1 : 1 / (2 ** 5), 2 : 2 ** 11 }

def apply(n: int, f: Callable[..., Any], arg: Any, *args: Any) -> Any:

    if not args:
        return reduce(lambda x, _: f(x), range(n), arg)
    
    return reduce(lambda x, _: f(*x), range(n), (arg, *args))

@cache
def pm(secret: int, step: int = 0) -> tuple[int, int]:
    return (floor(secret * steps[step]) ^ secret) & 16777215, (step + 1) % 3

@cache
def t(secret: int) -> int:
    out, _ = apply(3, pm, secret, 0)
    return out

seeds = map(int, open('in.txt').readlines())
seeds = list(map(lambda seed: apply(2000, t, seed), seeds))

print(sum(seeds))