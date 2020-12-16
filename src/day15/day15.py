from common.utils import timeit
from typing import List

@timeit
def run(input: List[int], target: int):

    current_number = input.pop()
    last_index = {val: i for i, val in enumerate(input)}

    for current_turn in range(len(input), target-1):
        next_number = current_turn - last_index[current_number] if current_number in last_index else 0
        last_index[current_number] = current_turn
        current_number = next_number

    return current_number


if __name__ == '__main__':

    print(f"The solution to part 1 = {run([18,11,9,0,5,1], 2020)}")
    print(f"The solution to part 2 = {run([18,11,9,0,5,1], 30000000)}")
