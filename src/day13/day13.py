import itertools
from typing import List, Tuple


def run_part1(timestamp: int, input: List[Tuple[int, int]]):
    first_bus_id = max(input, key=lambda x: timestamp % x[0])[0]
    return first_bus_id * (first_bus_id - (timestamp % first_bus_id))


def run_part2(input: List[Tuple[int, int]]):

    timestamp, period = 0, 1

    for bus_period, bus_offset in input:

        timestamp, period = next(
            (next_timestamp, period * bus_period)
            for i in itertools.count()
            if ((next_timestamp := timestamp + period * i) + bus_offset) % bus_period == 0
        )

    return timestamp


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    timestamp = int(input[0])
    input = [(int(i), offset) for offset, i in enumerate(input[1].split(",")) if i != 'x']

    print(f"The solution to part 1 = {run_part1(timestamp, input)}")
    print(f"The solution to part 2 = {run_part2(input)}")
