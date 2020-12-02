from typing import List, Tuple
import re

REGEXP_MATCH = r"(\d+)-(\d+)\s([a-z]):\s([a-z]+)"


def parse_input(lines: List[str]):
    return [re.findall(REGEXP_MATCH, line)[0] for line in lines]


def is_valid_sled_rental_row(row: Tuple):
    min_count, max_count, match_letter, password = row
    return int(min_count) <= password.count(match_letter) <= int(max_count)


def is_valid_toggoban_row(row: Tuple):
    first_index, second_index, match_letter, password = row
    return (password[int(first_index)-1] == match_letter) != (password[int(second_index)-1] == match_letter)  # xor


def run_part1(parsed_input: List[Tuple]):
    return sum(is_valid_sled_rental_row(i) for i in parsed_input)


def run_part2(parsed_input: List[Tuple]):
    return sum(is_valid_toggoban_row(i) for i in parsed_input)


if __name__ == '__main__':

    with open('input.txt') as file:
        rules = file.readlines()

    parsed_input = parse_input(rules)

    print(f"The solution to part 1 is {run_part1(parsed_input)}")
    print(f"The solution to part 1 is {run_part2(parsed_input)}")
