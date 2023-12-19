"""
--- Day 13: Point of Incidence ---
"""
import os
from typing import List

TEST = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

test_patterns = [block.split() for block in TEST.split(f"{os.linesep}{os.linesep}")]


def find_equal(grid: List[List[str]]) -> List[int]:
    result = []
    for (i1, r1), (i2, r2) in zip(enumerate(grid), enumerate(grid[1:], start=1)):
        if r1 == r2:
            result.append((i1, i2))

    return result


assert find_equal([list(col) for col in zip(*test_patterns[0])]) == [(4, 5)]
assert find_equal(test_patterns[1]) == [(3, 4)]


def count_reflections(grid: List[List[str]], left: int, right: int):
    current_left, current_right = left, right
    while (
        0 <= current_left
        and current_right < len(grid)
        and grid[current_left] == grid[current_right]
    ):
        current_left, current_right = current_left - 1, current_right + 1

    return left - current_left - 1


test_summarization = 0
for block in test_patterns:
    rows_reflections = find_equal(block)
    for top, bottom in rows_reflections:
        print(count_reflections(block, top, bottom))
    test_summarization += sum(
        count_reflections(block, top, bottom) * 100 for top, bottom in rows_reflections
    )

    transposed_block = [list(col) for col in zip(*block)]
    columns_reflections = find_equal(transposed_block)
    test_summarization += sum(
        count_reflections(transposed_block, left, right)
        for left, right in columns_reflections
    )

print(test_summarization)
assert test_summarization == 405
