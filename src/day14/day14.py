from typing import List
import re


def mask_value(mask: str, input: str) -> int:

    masked_input = [input_bit if mask_bit == "X" else mask_bit
                    for mask_bit, input_bit in zip(mask, f"{int(input):036b}")]

    return int("".join(masked_input), 2)


def mask_address(mask: str, addr: str) -> str:

    masked_address = [input_bit if mask_bit == "0" else mask_bit
                      for mask_bit, input_bit in zip(mask, f"{int(addr):036b}")]

    return "".join(masked_address)


def expand(key: str):

    x_indices = [i for i, val in enumerate(key) if val == "X"]
    output = []

    for repl in range(2**len(x_indices)):
        repl_binary = f"{repl:b}".zfill(len(x_indices))

        new_key = str(key)

        for i, i2 in enumerate(x_indices):
            new_key = new_key[:i2] + repl_binary[i] + new_key[i2+1:]

        output.append(new_key)

    return output

def run_part1(input: List[str]):

    mem = dict()

    for line in input:
        if "mask" in line:
            mask = line[7:]
        else:
            addr, val = re.findall("mem\[(\d+)\] = (\d+)", line)[0]
            mem[addr] = mask_value(mask, val)

    return sum(mem.values())


def run_part2(input):

    address_to_val = dict()

    for line in input:
        if "mask" in line:
            mask = line[7:]
        else:

            addr, val = re.findall(r"mem\[(\d+)] = (\d+)", line)[0]
            masked_address = mask_address(mask, addr)

            for new_key in expand(masked_address):
                address_to_val[new_key] = int(val)

    return sum(address_to_val.values())


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    print(f"The solution to part 1 = {run_part1(input)}")
    print(f"The solution to part 2 = {run_part2(input)}")