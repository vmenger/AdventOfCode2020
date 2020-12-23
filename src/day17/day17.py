import numpy as np
from itertools import product

from typing import Tuple


def count_neighbours(loc: Tuple, grid: np.array):
    neighbours_slice = tuple(slice(max(k-1, 0), min(k+1, max_k)+1) for k, max_k in zip(loc, grid.shape))
    return np.sum(grid[neighbours_slice]) - grid[loc]


def run(input_grid: np.array, iterations: int, size: int, fourth_dimension: bool):

    x_size = y_size = size+2*iterations
    z_size = 2*iterations+1
    w_size = 2*iterations+1 if fourth_dimension else 1

    grid = np.zeros((x_size, y_size, z_size, w_size))
    input_grid_slice = slice(iterations, iterations+size)
    grid[input_grid_slice, input_grid_slice, iterations, int(w_size/2)] = (input_grid == '#')

    for _ in range(iterations):

        next_grid = np.zeros((x_size, y_size, z_size, w_size))

        for loc in product(*[range(x) for x in grid.shape]):

            num_neighbours = count_neighbours(loc, grid)

            if grid[loc] == 1:
                next_grid[loc] = 1 if (2 <= num_neighbours <= 3) else 0
            elif num_neighbours == 3:
                next_grid[loc] = 1

        grid = next_grid

    return grid.sum()


if __name__ == '__main__':

    with open('input.txt') as file:
        i = np.array([list(x) for x in file.read().splitlines()])

    print(f"The solution to part 1 = {run(i, 6, 8, False)}")
    print(f"The solution to part 2 = {run(i, 6, 8, True)}")
