from common.utils import timeit
from typing import List


def find_double_sum(elems: List[int], target: int):

    for e in elems:
        if(target-e) in elems:
            return e*(target-e)

    return 0


def find_triple_sum(elems: List[int], target: int):

    for i, e in enumerate(elems):
        prod = find_double_sum(elems[i:], target-e)

        if prod > 0:
            return prod * e

    return 0


@timeit
def run_part_1(expenses: List[int]):
    return find_double_sum(expenses, 2020)


@timeit
def run_part_2(expenses: List[int]):
    return find_triple_sum(expenses, 2020)


if __name__ == '__main__':

    with open("input.txt") as file:
        expenses = [int(x) for x in file.read().splitlines()]

    print(f"The solution to part 1: {run_part_1(expenses)}")
    print(f"The solution to part 2: {run_part_2(expenses)}")
