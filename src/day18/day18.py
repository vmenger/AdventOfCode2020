import re
from typing import List

class CustomInt:

    def __init__(self, a): self.a = a
    def __int__(self): return int(self.a)


def input_to_custom(input: str, replacement_dict: dict, custom_int_class: str):
    input = "".join([replacement_dict[char] if char in replacement_dict else char for char in input])
    input = re.sub(r"(\d+)", f"{custom_int_class}(\\1)", input)
    return input


class CustomIntPart1(CustomInt):

    def __add__(self, o): return CustomIntPart1(self.a + o.a)
    def __sub__(self, o): return CustomIntPart1(self.a * o.a)


class CustomIntPart2(CustomInt):
    def __add__(self, o): return CustomIntPart2(self.a * o.a)
    def __mul__(self, o): return CustomIntPart2(self.a + o.a)


def run_part1(input: List[str]):
    return sum(
        int(eval(input_to_custom(line, {'*': '-'}, 'CustomIntPart1')))
        for line in input
    )


def run_part2(input: List[str]):
    return sum(
        int(eval(input_to_custom(line, {'*': '+', '+': '*'}, 'CustomIntPart2')))
        for line in input
    )


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    print(f"The solution to part 1 = {run_part1(input)}")
    print(f"The solution to part 2 = {run_part2(input)}")
