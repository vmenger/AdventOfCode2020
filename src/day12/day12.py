from typing import List, Tuple


HEADINGS = ['N', 'E', 'S', 'W']


def run_part1(instructions: List[Tuple[str, int]]):

    x, y, heading = 0, 0, 1

    for instruction, val in instructions:

        if instruction == "L":
            heading -= int(val/90)

        elif instruction == "R":
            heading += int(val/90)

        elif instruction == "F":
            instruction = HEADINGS[heading % len(HEADINGS)]

        if instruction == "N":
            y += val

        elif instruction == "E":
            x += val

        elif instruction == "S":
            y -= val

        elif instruction == "W":
            x -= val

    return abs(x) + abs(y)


def run_part2(instructions: List[Tuple[str, int]]):

    x, y, wx, wy = 0, 0, 10, 1

    for instruction, val in instructions:

        if instruction == "F":
            x += val*wx
            y += val*wy

        elif instruction == "N":
            wy += val

        elif instruction == "E":
            wx += val

        elif instruction == "S":
            wy -= val

        elif instruction == "W":
            wx -= val

        elif instruction == "L":
            for _ in range(int(val/90)):
                wx, wy = -wy, wx

        elif instruction == "R":
            for _ in range(int(val / 90)):
                wx, wy = wy, -wx

    return abs(x) + abs(y)


if __name__ == '__main__':

    with open('input.txt') as file:
        instructions = [(line[0], int(line[1:])) for line in file.read().splitlines()]

    print(f"The solution to part 1 = {run_part1(instructions)}")
    print(f"The solution to part 2 = {run_part2(instructions)}")






