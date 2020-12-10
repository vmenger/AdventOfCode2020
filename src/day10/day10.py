from typing import List
import numpy as np


def run_part1(input: List[int]):
    return sum(np.diff(input) == 1) * sum(np.diff(input) == 3)


def run_part2(input: List[int]):

    num_paths = [0] * len(input)
    num_paths[0] = 1

    for i in range(len(input)):
        for j in range(1, 4):
            if ((i+j) < len(num_paths)) and (abs(input[i]-input[i+j]) <= 3):
                num_paths[i+j] += num_paths[i]

    return num_paths[-1]


if __name__ == '__main__':

    with open('input.txt') as file:
        input = [int(x) for x in file.read().splitlines()]

    input = sorted([0] + input + [max(input)+3])

    print(f"The solution to part 1 = {run_part1(input)}")
    print(f"The solution to part 2 = {run_part2(input)}")
