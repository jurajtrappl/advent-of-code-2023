"""
--- Day 21: Step Counter ---
"""
from itertools import product
from pprint import pprint

REMAINING_STEPS = 64
START = "S"  # counts as a garden plot
GARDEN_PLOT = "."
ROCK = "#"

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open("21-test.in", "r", encoding="utf-8") as f:
    garden = [list(line) for line in f.read().splitlines()]

M, N = len(garden), len(garden[0])
start = None
for i, j in product(range(M), range(N)):
    if garden[i][j] == START:
        start = (i, j)
        break


def expand_reach(grid, reach):
    new_reach = set(reach)

    for row, col in reach:
        for dr, dc in DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and grid[new_row][new_col] == GARDEN_PLOT
            ):
                new_reach.add((new_row, new_col))

    return new_reach - reach


def draw(grid, reach):
    for i, j in reach:
        grid[i][j] = "O"

    pprint(grid)


STEPS = 6
current_reach = set([start])
for _ in range(STEPS):
    current_reach = expand_reach(garden, current_reach)
    print(current_reach)
    print(len(current_reach))
    draw(garden.copy(), current_reach)
    print("---------------------")
