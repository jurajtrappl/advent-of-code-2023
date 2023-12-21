"""
--- Day 18: Lavaduct Lagoon ---
"""
from itertools import product
from pprint import pprint

GROUND = "."
TRENCH = "#"

DIRECTIONS = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1)}

MAX_HEIGHT, MAX_WIDTH = 600, 600
START = 300, 0

with open("18-test.in", "r", encoding="utf-8") as f:
    dig_plan = [
        (direction, int(meters), color[1:-1])
        for direction, meters, color in [
            instruction.split() for instruction in f.read().strip().splitlines()
        ]
    ]


def count_trenches(plan):
    return sum(
        plan[r][c] == TRENCH for r, c in product(range(MAX_HEIGHT), range(MAX_WIDTH))
    )


def dig(plan):
    lagoon = [[GROUND for _ in range(MAX_WIDTH)] for _ in range(MAX_HEIGHT)]
    r, c = START
    for direction, meters, _ in plan:
        current_meters = meters
        while current_meters:
            lagoon[r][c] = TRENCH
            dr, dc = DIRECTIONS[direction]
            r, c = r + dr, c + dc
            current_meters -= 1

    borders = count_trenches(lagoon)
    print(borders)

    plan_rows = [i for i, r in enumerate(lagoon) if "#" in r]
    for r in range(plan_rows[0], plan_rows[-1]):
        trench_locations = [i for i, c in enumerate(lagoon[r]) if c == TRENCH]
        for c in range(trench_locations[0], trench_locations[-1]):
            lagoon[r][c] = TRENCH

    return lagoon


print(count_trenches(dig(dig_plan)))
