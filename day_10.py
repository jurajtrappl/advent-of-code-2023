"""
--- Day 10: Pipe Maze ---
"""
from itertools import product

direction_offset = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
opposite_direction = {"N": "S", "S": "N", "E": "W", "W": "E"}
pipe_direction = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    "S": ["N", "E", "S", "W"],
}


def in_bounds(row: int, col: int, number_of_rows: int, number_of_columns: int) -> bool:
    return 0 <= row < number_of_rows and 0 <= col < number_of_columns


with open("10.in", "r", encoding="utf-8") as f:
    pipe_maze = [list(line) for line in f.read().strip().splitlines()]

M, N = len(pipe_maze), len(pipe_maze[0])
start = [(i, j) for i, j in product(range(M), range(N)) if pipe_maze[i][j] == "S"][0]

queue, visited = [start], set()
while queue:
    current = queue.pop()

    if current in visited:
        continue

    visited.add(current)

    r, c = current
    for direction in pipe_direction.get(pipe_maze[r][c], []):
        dr, dc = direction_offset[direction]
        nr, nc = r + dr, c + dc
        if not in_bounds(nr, nc, M, N):
            continue

        neighbour_pipe = pipe_maze[nr][nc]
        can_be_connected = opposite_direction[direction] in pipe_direction.get(
            neighbour_pipe, []
        )
        if can_be_connected:
            queue.append(((nr, nc)))

print(len(visited) // 2)
