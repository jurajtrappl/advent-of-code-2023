"""
--- Day 8: Haunted Wasteland ---
"""
from math import lcm
from typing import Callable, List

with open("08.in", "r", encoding="utf-8") as f:
    content = f.read().strip().splitlines()
    directions, maps = content[0], [line.split(" = ") for line in content[2:]]
    maps = {node: d[1:-1].split(", ") for node, d in maps}


def count_steps_for_node(start_node: str, is_end_node: Callable[[str], bool]) -> int:
    i = 0
    steps = 0
    current_node = start_node
    while not is_end_node(current_node):
        current_direction = 1 if directions[i] == "R" else 0
        i = (i + 1) % len(directions)
        current_node = maps[current_node][current_direction]
        steps += 1

    return steps


p1_steps = count_steps_for_node("AAA", lambda node: node == "ZZZ")
p2_steps: List[int] = [
    count_steps_for_node(start_node, lambda node: node.endswith("Z"))
    for start_node in [node for node in maps if node.endswith("A")]
]

print(p1_steps, lcm(*p2_steps))
