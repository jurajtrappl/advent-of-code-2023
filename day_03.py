"""
--- Day 3: Gear Ratios ---
"""
from itertools import product
from typing import List


def is_gear(c: str, current_part_numbers: List[int]) -> bool:
    return c == "*" and len(current_part_numbers) == 2


def is_symbol(c: str) -> bool:
    return c == "." or c.isdigit()


def in_bounds(x: int, y: int, number_of_rows: int, number_of_columns: int) -> bool:
    return 0 <= x < number_of_rows and 0 <= y < number_of_columns


with open("03.in", "r", encoding="utf-8") as f:
    engine_schematic = [list(line) for line in f.read().strip().splitlines()]

M, N = len(engine_schematic), len(engine_schematic[0])
directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
part_numbers, gear_ratios = 0, 0

for current_row, current_col in product(range(M), range(N)):
    if is_symbol(engine_schematic[current_row][current_col]):
        continue

    part_numbers_around, seen_positions = [], set()
    for dr, dc in directions:
        new_row, new_col = current_row + dr, current_col + dc
        
        symbol_was_processed = (new_row, new_col) in seen_positions
        if (
            not in_bounds(new_row, new_col, M, N)
            or not engine_schematic[new_row][new_col].isdigit()
            or symbol_was_processed
        ):
            continue

        number_buffer = [engine_schematic[new_row][new_col]]
        col_left = new_col - 1
        while (
            in_bounds(new_row, col_left, M, N)
            and engine_schematic[new_row][col_left].isdigit()
        ):
            number_buffer = [engine_schematic[new_row][col_left]] + number_buffer
            col_left -= 1

        col_right = new_col + 1
        while (
            in_bounds(new_row, col_right, M, N)
            and engine_schematic[new_row][col_right].isdigit()
        ):
            number_buffer += [engine_schematic[new_row][col_right]]
            col_right += 1

        part_numbers_around.append(int("".join(number_buffer)))
        seen_positions.update(
            [(new_row, position) for position in range(col_left, col_right + 1)]
        )

    part_numbers += sum(part_numbers_around)
    if is_gear(engine_schematic[current_row][current_col], part_numbers_around):
        gear_ratios += part_numbers_around[0] * part_numbers_around[1]

print(part_numbers, gear_ratios)
