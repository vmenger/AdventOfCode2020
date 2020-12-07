import re
from typing import List, Tuple


def run_part1(parents: List[str], children: List[List[Tuple[int, str]]]):

    def is_parent_of(color, target):
        return any((child == target) | is_parent_of(child, target) for _, child in children[parents.index(color)])

    return sum(is_parent_of(color, target='shiny gold') for color in parents)


def run_part2(parents: List[str], children: List[List[Tuple[int, str]]]):

    def count_bags(color):
        return sum(int(amount) * (1+count_bags(child)) for amount, child in children[parents.index(color)])

    return count_bags("shiny gold")


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    parents = [re.findall(r"([a-z\s]+) bags contain", line)[0] for line in input]
    children = [re.findall(r"(\d)+ ([a-z\s]+) bag[s]?", line) or [] for line in input]

    print(f"Print the solution to part 1 = {run_part1(parents, children)}")
    print(f"Print the solution to part 1 = {run_part2(parents, children)}")