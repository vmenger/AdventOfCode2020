import numpy as np
from itertools import product


def count_neighbours(grid: np.array, i: int, j: int, max_n: int):

    counter = 0

    for di, dj, n in {(a, b, 1) for a, b in product((-1, 0, 1), repeat=2)} - {(0, 0)}:

        while (n <= max_n) and (0 <= i+di*n < grid.shape[0]) and (0 <= j+dj*n < grid.shape[1]):
            val = grid[i+di*n, j+dj*n]

            if val == '.':
                n += 1
                continue
            elif val == '#':
                counter += 1

            break

    return counter


def simulate(grid: np.array, max_neighbours: int, max_radius: int):

    changes = True

    while changes:

        next_grid = grid.copy()
        changes = False

        for i, j in np.ndindex(grid.shape):

            num_neighbours = count_neighbours(grid, i, j, max_radius)

            if (grid[i, j] == 'L') and (num_neighbours == 0):
                changes = True
                next_grid[i, j] = '#'

            if (grid[i, j] == '#') and (num_neighbours >= max_neighbours):
                changes = True
                next_grid[i, j] = 'L'

        grid = next_grid

    return sum(sum(grid == '#'))


def run_part1(grid):
    return simulate(grid, max_neighbours=4, max_radius=1)

def run_part2(grid):
    return simulate(grid, max_neighbours=5, max_radius=max(grid.shape))


if __name__ == '__main__':

    with open('input.txt') as file:
        grid = np.array([list(x) for x in file.read().splitlines()])

    print(f"The solution to part 1 = {run_part1(grid)}")
    print(f"The solution to part 2 = {run_part2(grid)}")










