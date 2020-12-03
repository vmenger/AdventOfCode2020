from typing import List


def count_trees(rows: List[str], right: int, down: int):

    num_trees = 0

    x, y = 0, 0

    while (x < len(rows)):
        if rows[x][y] == "#":
            num_trees += 1

        x = x + down
        y = (y+right) % len(rows[0])

    return num_trees


def run_part1(input: List[str]):
    return count_trees(input, 3, 1)


def run_part2(input: List[str]):

    return count_trees(input, 1, 1) * \
           count_trees(input, 3, 1) * \
           count_trees(input, 5, 1) * \
           count_trees(input, 7, 1) * \
           count_trees(input, 1, 2)


if __name__ == '__main__':

    with open("input.txt") as file:
        input = file.read().splitlines()

    print(f"The answer to part 1 = {run_part1(input)}")
    print(f"The answer to part 2 = {run_part2(input)}")



