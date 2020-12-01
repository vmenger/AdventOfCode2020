from common.utils import timeit
from typing import List


def find_double_sum(elems: List[int], target: int):

    for e in elems:
        if(target-e) in elems:
            return e, (target-e)

    return 0, 0


def find_triple_sum(elems: List[int], target: int):

    for i, e in enumerate(elems):
        val1, val2 = find_double_sum(elems[i:], target-e)

        if (val1+val2) > 0:
            return val1, val2, e

    return 0, 0, 0


@timeit
def run_part_1():

    with open("input.txt") as file:
        expenses = [int(x) for x in file.readlines()]

    val1, val2 = find_double_sum(expenses, 2020)

    print(f"The solution to part 1: {val1}*{val2}={val1*val2}")


@timeit
def run_part_2():

    with open("input.txt") as file:
        expenses = [int(x) for x in file.readlines()]

    val1, val2, val3 = find_triple_sum(expenses, 2020)

    print(f"The solution to part 1: {val1}*{val2}*{val3}={val1*val2*val3}")


if __name__ == '__main__':
    run_part_1()
    run_part_2()
