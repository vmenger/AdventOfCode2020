from typing import List, Dict
import re


def has_valid_keys(passport: Dict):
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(set(passport.keys()))


def is_valid_height(height: str):

    if height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    elif height[-2:] == 'in':
        return 59 <= int(height[:-2]) <= 76
    else:
        return False


def is_valid_passport(passport: Dict):

    if not has_valid_keys(passport):
        return False

    validators = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: is_valid_height(x),
        'hcl': lambda x: re.match(r"^#[0-9a-f]{6}$", x) is not None,
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: re.match(r"^[0-9]{9}$", x) is not None
    }

    return all(validator(passport[prop]) for prop, validator in validators.items())


def run_part1(passports: List[Dict]):
    return sum(has_valid_keys(p) for p in passports)


def run_part2(passports: List[Dict]):
    return sum(is_valid_passport(p) for p in passports)


if __name__ == '__main__':

    with open('input.txt') as file:
        input = [line.replace("\n", " ") for line in file.read().split("\n\n")]

    passports = [dict(token.split(":") for token in line.split(" ")) for line in input]

    print(f"The solution to part 1 = {run_part1(passports)}")
    print(f"The solution to part 2 = {run_part2(passports)}")