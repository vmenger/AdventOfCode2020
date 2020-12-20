import numpy as np
import math
from itertools import product


def grid_orientations(grid: np.array):
    for _ in range(4):
        yield grid
        yield np.flipud(grid)
        grid = np.rot90(grid)


class Tile:

    def __init__(self, input_str: str):

        input_str = input_str.split("\n")
        self.id = int(input_str[0][5:9])
        self.grid = np.array([list(x) for x in input_str[1:]])


NEIGHBOURS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


VALIDATORS = [
    lambda a, b: (a[-1, :] == b[0, :]).all(),
    lambda a, b: (a[0, :] == b[-1, :]).all(),
    lambda a, b: (a[:, 0] == b[:, -1]).all(),
    lambda a, b: (a[:, -1] == b[:, 0]).all(),
]


def search(current_tile: Tile, x: int, y: int):

    tile_grid[current_tile] = (x, y)

    for (dx, dy), validator in zip(NEIGHBOURS, VALIDATORS):

        for candidate_match in available_tiles.copy():

            for grid_orient in grid_orientations(candidate_match.grid):

                if validator(grid_orient, current_tile.grid):

                    candidate_match.grid = grid_orient
                    available_tiles.remove(candidate_match)

                    # Recurse
                    search(candidate_match, x+dx, y+dy)

                    break


def count_monsters(grid: np.array, monster: np.array):

    num_monsters = 0

    for grid_orientation in grid_orientations(grid):

        c = 0

        for i in range(grid_orientation.shape[0]-monster.shape[0]):
            for j in range(grid_orientation.shape[1]-monster.shape[1]):
                if (grid_orientation[i:i+monster.shape[0], j:j+monster.shape[1]] >= monster).all():
                    c += 1

        if c > num_monsters:
            num_monsters = c

    return num_monsters


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().split("\n\n")

    n = int(math.sqrt(len(input)))  # number of tiles

    tiles = [Tile(x) for x in input]
    available_tiles = set(tiles)
    tile_grid = dict()  # tile -> (x,y)

    x, y = 0, 0
    search(available_tiles.pop(), x, y)

    min_x = min(v[0] for v in tile_grid.values())
    min_y = min(v[1] for v in tile_grid.values())

    for tile, (x, y) in tile_grid.items():
        tile_grid[tile] = (x-min_x, y-min_y)

    ## Part 1
    p = math.prod(tile.id for tile, loc in tile_grid.items() if loc in [*product([0, n-1], repeat=2)])
    print(f"The solution to part 1 = {p}")

    ## Part 2
    monster = ['..................#.', '#....##....##....###', '.#..#..#..#..#..#...']
    monster = np.array([list(x) for x in monster]) == "#"

    tile_size = 8  # part 2 tile size

    final_grid = np.zeros((n*tile_size, n*tile_size))

    for tile, (x, y) in tile_grid.items():
        x1 = tile_size*x
        y1 = tile_size*((n-1)-y)  # why does numpy not use cartesian coordinates again?
        final_grid[y1:(y1+tile_size), x1:(x1+tile_size)] = (tile.grid[1:-1, 1:-1] == '#')

    water_roughness = (int(final_grid.sum() - count_monsters(final_grid, monster) * monster.sum()))
    print(f"The solution to part 2 = {water_roughness}")
