"""
--- Day 16: The Floor Will Be Lava ---
"""
from pprint import pprint

EMPTY_SPACE = "."
VERTICAL_SPLITTER, HORIZONTAL_SPLITTER = "|", "-"

BEAM_START = 0, 0

DIRECTIONS = {"UP": (-1, 0), "LEFT": (0, -1), "DOWN": (1, 0), "RIGHT": (0, 1)}


def in_bounds(r: int, c: int, number_of_rows: int, number_of_columns: int) -> bool:
    return 0 <= r < number_of_rows and 0 <= c < number_of_columns


with open("16-test.in", "r", encoding="utf-8") as f:
    test_grid = [list(line) for line in f.read().strip().split()]

R, C = len(test_grid), len(test_grid[0])
current_beams, energized = [(BEAM_START, (0, 1))], set()
while current_beams:
    position, direction = current_beams.pop()
    x, y = position
    if not in_bounds(x, y, R, C):
        continue

    energized.add((x, y))

    dx, dy = direction
    nx, ny = x + dx, y + dy
    if not in_bounds(nx, ny, R, C):
        continue

    if test_grid[nx][ny] == EMPTY_SPACE:
        current_beams.append(((nx, ny), direction))
    elif test_grid[nx][ny] == "/":
        energized.add((nx, ny))

        if direction == DIRECTIONS["UP"]:
            new_direction = DIRECTIONS["RIGHT"]
        elif direction == DIRECTIONS["LEFT"]:
            new_direction = DIRECTIONS["DOWN"]
        elif direction == DIRECTIONS["DOWN"]:
            new_direction = DIRECTIONS["LEFT"]
        elif direction == DIRECTIONS["RIGHT"]:
            new_direction = DIRECTIONS["UP"]

        dnx, dny = new_direction
        current_beams.append(((nx + dnx, ny + dny), new_direction))
    elif test_grid[nx][ny] == "\\":
        energized.add((nx, ny))

        if direction == DIRECTIONS["UP"]:
            new_direction = DIRECTIONS["LEFT"]
        elif direction == DIRECTIONS["LEFT"]:
            new_direction = DIRECTIONS["UP"]
        elif direction == DIRECTIONS["DOWN"]:
            new_direction = DIRECTIONS["RIGHT"]
        elif direction == DIRECTIONS["RIGHT"]:
            new_direction = DIRECTIONS["DOWN"]

        dnx, dny = new_direction
        current_beams.append(((nx + dnx, ny + dny), new_direction))
    elif test_grid[nx][ny] == VERTICAL_SPLITTER:
        energized.add((nx, ny))

        if direction in (DIRECTIONS["UP"], DIRECTIONS["DOWN"]):
            current_beams.append(((nx + dx, ny + dy), direction))
            continue

        current_beams.append(((nx - 1, ny), DIRECTIONS["UP"]))
        current_beams.append(((nx + 1, ny), DIRECTIONS["DOWN"]))
    elif test_grid[nx][ny] == HORIZONTAL_SPLITTER:
        energized.add((nx, ny))

        if direction in (DIRECTIONS["LEFT"], DIRECTIONS["RIGHT"]):
            current_beams.append(((nx + dx, ny + dy), direction))
            continue

        current_beams.append(((nx, ny + 1), DIRECTIONS["RIGHT"]))
        current_beams.append(((nx, ny - 1), DIRECTIONS["LEFT"]))

print(len(energized))

# print energized map
energized_map = [["." for _ in range(C)] for _ in range(R)]
for r, c in energized:
    energized_map[r][c] = "#"

pprint(energized_map)
