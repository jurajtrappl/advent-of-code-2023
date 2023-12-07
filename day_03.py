from itertools import product

with open("03.in", "r", encoding="utf-8") as f:
    engine_schematic = [list(line) for line in f.read().strip().splitlines()]

M, N = len(engine_schematic), len(engine_schematic[0])
directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
part_numbers, gear_ratios = 0, 0


def in_bounds(x, y):
    return 0 <= x < M and 0 <= y < N


for current_row, current_col in product(range(M), range(N)):
    if (
        engine_schematic[current_row][current_col] == "."
        or engine_schematic[current_row][current_col].isdigit()
    ):
        continue

    part_numbers_around, seen_positions = [], set()
    for dr, dc in directions:
        new_row, new_col = current_row + dr, current_col + dc
        if (
            not in_bounds(new_row, new_col)
            or not engine_schematic[new_row][new_col].isdigit()
            or (new_row, new_col) in seen_positions
        ):
            continue

        number_buffer = [engine_schematic[new_row][new_col]]
        col_left = new_col - 1
        while (
            in_bounds(new_row, col_left)
            and engine_schematic[new_row][col_left].isdigit()
        ):
            number_buffer = [engine_schematic[new_row][col_left]] + number_buffer
            col_left -= 1

        col_right = new_col + 1
        while (
            in_bounds(new_row, col_right)
            and engine_schematic[new_row][col_right].isdigit()
        ):
            number_buffer += [engine_schematic[new_row][col_right]]
            col_right += 1

        part_numbers_around.append(int("".join(number_buffer)))
        seen_positions.update(
            [(new_row, position) for position in range(col_left, col_right + 1)]
        )

    part_numbers += sum(part_numbers_around)
    if (
        engine_schematic[current_row][current_col] == "*"
        and len(part_numbers_around) == 2
    ):
        gear_ratios += part_numbers_around[0] * part_numbers_around[1]

print(part_numbers)
print(gear_ratios)
