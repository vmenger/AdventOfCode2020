from collections import defaultdict
import re

directions = ["ne", "nw", "sw", "se", "e", "w"]
deltas = [(1, 1), (0, 1), (-1, -1), (0, -1), (1, 0), (-1, 0)]


if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    floor = defaultdict(lambda: False)
    direction_to_delta = dict(zip(directions, deltas))

    for line in input:
        x = y = 0

        for direction in re.findall("|".join(directions), line):

            dx, dy = direction_to_delta[direction]
            x += dx
            y += dy

        floor[(x, y)] = not floor[(x, y)]

    # Part 1
    print(sum(x for x in floor.values()))

    for _ in range(100):

        black_neighbours = defaultdict(lambda: 0)
        new_floor = defaultdict(lambda: False)

        for x, y in floor.keys():
            if floor[(x, y)]:
                for dx, dy in deltas:
                    black_neighbours[(x+dx, y+dy)] += 1

        for (x, y), val in black_neighbours.items():
            if not floor[(x, y)] and (val == 2):
                new_floor[(x, y)] = True

        for x, y in floor.keys():
            n = black_neighbours[(x, y)]
            if floor[(x, y)] and not((n == 0) or (n > 2)):
                new_floor[(x, y)] = True

        floor = new_floor

    # Part 2
    print(sum(x for x in floor.values()))
