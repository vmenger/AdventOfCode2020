import re
import numpy as np
from math import prod

from typing import List


def is_valid(val: int, condition: List[int]):
    min1, max1, min2, max2 = condition
    return (min1 <= val <= max1) or (min2 <= val <= max2)


def total_never_valid_values(values: List[int], conditions: List[List[int]]):
    return sum(v for v in values if not any(is_valid(v, condition) for condition in conditions))


def all_valid(values: List[int], condition: List[int]):
    return all(is_valid(v, condition) for v in values)


def run_part1(nearby_tickets: List[List[int]], conditions: List[List[int]]):
    return sum(total_never_valid_values(n, conditions) for n in nearby_tickets)


def run_part2(nearby_tickets: List[List[int]], conditions: List[List[int]],
              condition_names: List[str], ticket: List[int]):

    nearby_tickets = np.array(
        [n
         for n in nearby_tickets
         if total_never_valid_values(n, conditions) == 0
         ]
    )

    mat = np.array(
        [[all_valid(nearby_col, condition)
         for condition in conditions]
         for nearby_col in nearby_tickets.T]
    )

    while mat.sum() != mat.shape[0]:

        # For each row which sums to 1, set the column to zeroes
        for x in np.where(mat.sum(axis=0) == 1)[0]:
            y = np.where(mat[:, x] == 1)[0][0]
            mat[y, :] = 0
            mat[y, x] = 1

        # Transpose and repeat
        mat = mat.T

    one_indices = np.where(mat == 1)
    condition_to_col = dict(zip(one_indices[0], one_indices[1]))

    return prod(
        [ticket[condition_to_col[i]]
         for i, name in enumerate(condition_names)
         if "departure" in name
         ]
    )


if __name__ == '__main__':

    with open('input.txt') as file:
        conditions, ticket, nearby_tickets = [t.split("\n") for t in file.read().split('\n\n')]

    nearby_tickets = [list(map(int, line.split(","))) for line in nearby_tickets[1:]]
    condition_names = [line.split(":")[0] for line in conditions]
    conditions = [list(map(int, re.findall(r"(\d+)", line))) for line in conditions]
    ticket = [int(x) for x in ticket[1:][0].split(",")]

    print(f"The solution to part 1 = {run_part1(nearby_tickets, conditions)}")
    print(f"The solution to part 2 = {run_part2(nearby_tickets, conditions, condition_names, ticket)}")
