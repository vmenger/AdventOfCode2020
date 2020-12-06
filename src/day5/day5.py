from typing import List
import re


def seat_id(boarding_pass: str) -> int:

    boarding_pass = re.sub("[FL]", "0", boarding_pass)
    boarding_pass = re.sub("[BR]", "1", boarding_pass)

    return int(boarding_pass, 2)


def run_part1(boarding_passes: List[str]) -> int:
    return max(seat_id(boarding_pass) for boarding_pass in boarding_passes)


def run_part2(boarding_passes: List[str]) -> int:

    filled_seats = {seat_id(boarding_pass) for boarding_pass in boarding_passes}
    open_seats = set(range(2**len(boarding_passes[0]))) - filled_seats

    for i in open_seats:
        if {i-1, i+1}.issubset(filled_seats):
            return i


if __name__ == "__main__":

    with open("input.txt") as file:
        boarding_passes = file.read().splitlines()

    print(f"The solution to part 1 = {run_part1(boarding_passes)}")
    print(f"The solution to part 2 = {run_part2(boarding_passes)}")
