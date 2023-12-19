"""
--- Day 17: Clumsy Crucible ---
"""

import heapq


def min_heat(start, end, grid):
    visited = set()
    # q = [(0, start, "D", 1), (0, start, "R", 1)]
    q = [(0, start, "R", 0)]
    heapq.heapify(q)
    while q:
        heat, position, direction, steps = heapq.heappop(q)

        if position == end:
            return heat

        if (position, direction) in visited:
            continue
        visited.add((position, direction))

        for (nr, nc), neighbour_direction, neighbour_steps in neighbours(
            position, direction, steps
        ):
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and ((nr, nc), neighbour_direction) not in visited
            ):
                neighbour_heat = heat + grid[nr][nc]
                heapq.heappush(
                    q, (neighbour_heat, (nr, nc), neighbour_direction, neighbour_steps)
                )


def neighbours(position, direction, steps):
    r, c = position
    moves = []

    if steps == 3:
        if direction == "D":
            moves.append(((r, c - 1), "R", 1))
            moves.append(((r, c + 1), "L", 1))
        elif direction == "U":
            moves.append(((r, c - 1), "L", 1))
            moves.append(((r, c + 1), "R", 1))
        else:
            moves.append(((r - 1, c), "U", 1))
            moves.append(((r + 1, c), "D", 1))
    else:
        if direction == "U":
            moves.append(((r - 1, c), "U", steps + 1))
            moves.append(((r, c - 1), "L", 1))
            moves.append(((r, c + 1), "R", 1))
        elif direction == "R":
            moves.append(((r, c + 1), "R", steps + 1))
            moves.append(((r - 1, c), "U", 1))
            moves.append(((r + 1, c), "D", 1))
        elif direction == "L":
            moves.append(((r, c - 1), "L", steps + 1))
            moves.append(((r - 1, c), "U", 1))
            moves.append(((r + 1, c), "D", 1))
        elif direction == "D":
            moves.append(((r + 1, c), "D", steps + 1))
            moves.append(((r, c - 1), "L", 1))
            moves.append(((r, c + 1), "R", 1))

    return moves


with open("17-test.in", "r", encoding="utf-8") as f:
    heatmap = [list(map(int, list(line))) for line in f.read().strip().splitlines()]

R, C = len(heatmap), len(heatmap[0])
print(min_heat((0, 0), (R - 1, C - 1), heatmap))
