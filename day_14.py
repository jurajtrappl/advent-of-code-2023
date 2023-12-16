"""
--- Day 14: Parabolic Reflector Dish ---
"""
from itertools import product
from pprint import pprint
from typing import List

ROUNDED_ROCK = "O"
CUBE_SHAPED_ROCK = "#"
EMPTY_SPACE = "."


def calculate_total_load(dish: List[List[str]]):
    total_load = 0
    for row, score in zip(dish, range(len(dish), 0, -1)):
        total_load += len(list(filter(lambda rock: rock == ROUNDED_ROCK, row))) * score

    return total_load


test_load = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""

assert calculate_total_load(list(test_load.split())) == 136


def roll_north(dish: List[List[str]], r: int, c: int):
    current_row, new_dish = r, dish
    while 0 <= current_row - 1 and new_dish[current_row - 1][c] == EMPTY_SPACE:
        new_dish[current_row][c] = EMPTY_SPACE
        new_dish[current_row - 1][c] = ROUNDED_ROCK
        current_row -= 1

    return new_dish


test = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def solve_p1(input: str):
    dish = list(list(line) for line in list(input.split()))
    for r, c in product(range(len(dish)), range(len(dish[0]))):
        if dish[r][c] == ROUNDED_ROCK:
            dish = roll_north(dish, r, c)

    return dish


assert list(list(line) for line in list(test_load.split())) == solve_p1(test)

with open("14.in", "r", encoding="utf-8") as f:
    parabolic_reflector_dish = f.read().strip()

print(calculate_total_load(solve_p1(parabolic_reflector_dish)))
