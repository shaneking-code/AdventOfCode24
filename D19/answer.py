import re
from functools import cache

input = open('in.txt').readlines()
alpha = tuple(sorted(map(str.strip, input[0].split(',')), key = lambda letter : len(letter), reverse=True))
regex = f'^({"|".join(alpha)})+$'
words = map(str.strip, input[2:])
words = list(filter(lambda word : re.match(regex, word), words))

@cache
def ways(word, alpha): 

    if len(word) == 1:
        return word in alpha
    
    res = 0
    for letter in alpha:
        regex = f'^({letter})'
        if re.match(regex, word):
            if len(letter) < len(word):
                res += ways(word[len(letter):], alpha)
            elif len(letter) == len(word):
                res += 1

    return res
            
one = len(words)
two = sum([ways(word, alpha) for word in words])

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")
