"""
--- Day 11: Cosmic Expansion ---
"""
from itertools import product

EMPTY_SPACE = "."
GALAXY = "#"
P1_EXPANSION_RATE, P2_EXPANSION_RATE = 2, 1_000_000


def distance(x1: int, y1: int, x2: int, y2: int, expansion_rate: int) -> int:
    left, right = min(y1, y2), max(y1, y2)
    col = [expansion_rate if col_i in empty_cols else 1 for col_i in range(left, right)]
    down, up = max(x1, x2), min(x1, x2)
    row = [expansion_rate if row_i in empty_rows else 1 for row_i in range(up, down)]
    return sum(col) + sum(row)


with open("11.in", "r", encoding="utf-8") as f:
    image = [list(line) for line in f.read().splitlines()]

M, N = len(image), len(image[0])
empty_rows = set(i for i, row in enumerate(image) if "#" not in row)
empty_cols = set(i for i, col in enumerate(zip(*image)) if "#" not in col)
galaxies = [(i, j) for i, j in product(range(M), range(N)) if image[i][j] == "#"]

p1_total_distance, p2_total_distance = 0, 0
for i, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[i + 1 :]:
        p1_total_distance += distance(x1, y1, x2, y2, P1_EXPANSION_RATE)
        p2_total_distance += distance(x1, y1, x2, y2, P2_EXPANSION_RATE)

print(p1_total_distance, p2_total_distance)
