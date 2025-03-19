from functools import cache

def read_input():
    with open('in.txt') as f:
        lines = f.readlines()
        # Sort by length in descending order during initial read
        alpha = tuple(sorted((x.strip() for x in lines[0].split(',')), key=len, reverse=True))
        # Skip empty line and get remaining words
        words = [x.strip() for x in lines[2:]]
    return alpha, words

def is_valid_word(word, alpha_set, alpha):
    if not word:
        return False
        
    i = 0
    word_len = len(word)
    while i < word_len:
        found = False
        # Try each possible letter from longest to shortest
        for letter in alpha:
            if word.startswith(letter, i):
                i += len(letter)
                found = True
                break
        if not found:
            return False
    return i == word_len

@cache
def count_ways(word, alpha):
    if not word:
        return 1
    
    total = 0
    for letter in alpha:
        if word.startswith(letter):
            total += count_ways(word[len(letter):], alpha)
    return total

def main():
    # Read and process input
    alpha, words = read_input()
    alpha_set = frozenset(alpha)
    
    # Part 1: Filter valid words
    valid_words = [word for word in words if is_valid_word(word, alpha_set, alpha)]
    part_one = len(valid_words)
    
    # Part 2: Count ways for valid words
    part_two = sum(count_ways(word, alpha) for word in valid_words)
    
    print(f"answer to part one is {part_one}")
    print(f"answer to part two is {part_two}")

if __name__ == '__main__':
    main()