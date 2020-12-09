from itertools import combinations
from typing import List


def run_part1(input: List[int], window=25):

    return next(
        input[i+window]
        for i in range(len(input))
        if not any(input[i+window]-val in input[i:i+window] for val in input[i:i+window])
    )


def run_part2(input: List[int]):

    return next(
        min(sublist) + max(sublist)
        for start, end in combinations(range(len(input)), 2)
        if sum(sublist := input[start:end]) == 22477624
    )


if __name__ == '__main__':

    with open('input.txt') as file:
        input = [int(x) for x in file.read().splitlines()]

    print(f"The solution to part 1 = {run_part1(input)}")
    print(f"The solution to part 2 = {run_part2(input)}")




