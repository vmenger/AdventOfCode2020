from typing import Tuple


def run_code(input: Tuple[str, str]) -> (int, bool):
    """
    Returns: accumulator, terminated
    """

    visited_lines = set()
    accumulator = 0
    current_line = 0

    while (current_line not in visited_lines) & (current_line < len(input)):

        visited_lines.add(current_line)
        command, val = input[current_line]
        d_line = 1

        if command == "acc":
            accumulator += int(val)
        elif command == "jmp":
            d_line = int(val)

        current_line += d_line

    else:
        return accumulator, (current_line == len(input))


def run_part1(input: Tuple[str, str]):

    accumulator, _ = run_code(input)
    return accumulator


def run_part2(input: Tuple[str, str]):

    for i, (acc, val) in enumerate(input):

        new_input = input.copy()

        if acc == "nop":
            new_input[i] = ('jmp', val)
        elif acc == 'jmp':
            new_input[i] = ('nop', val)
        else:
            continue

        accumulator, terminated = run_code(new_input)

        if terminated:
            return accumulator


if __name__ == '__main__':

    with open('input.txt') as file:
        input = [tuple(line.split(" ")) for line in file.read().splitlines()]

    print(f"The solution to part 1 = {run_part1(input)}")
    print(f"The solution to part 2 = {run_part2(input)}")
