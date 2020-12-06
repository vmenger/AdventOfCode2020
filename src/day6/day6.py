from typing import List


def run_part1(groups: List[List[str]]):
    return sum(len(set.union(*map(set, group))) for group in groups)


def run_part2(groups: List[List[str]]):
    return sum(len(set.intersection(*map(set, group))) for group in groups)


if __name__ == '__main__':

    with open('input.txt') as file:
        groups = [line.split("\n") for line in file.read().split("\n\n")]

    print(f"THe solution to part 1 = {run_part1(groups)}")
    print(f"THe solution to part 2 = {run_part2(groups)}")
