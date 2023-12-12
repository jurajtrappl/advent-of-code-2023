"""
--- Day 12: Hot Springs ---
"""
from itertools import product
from typing import List

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


def generate_combinations(springs_to_repair: str) -> List[str]:
    question_mark_count = springs_to_repair.count("?")
    combinations = product(".#", repeat=question_mark_count)

    result = []
    for combo in combinations:
        temp_springs = springs_to_repair
        for char in combo:
            temp_springs = temp_springs.replace("?", char, 1)
        result.append(temp_springs)

    return result


def is_solution(repaired_springs: str, sizes: List[int]) -> bool:
    contiguous_groups, current_group = [], []
    for i, spring in enumerate(repaired_springs):
        if spring == DAMAGED:
            current_group.append(i)
        else:
            if current_group:
                contiguous_groups.append(current_group)
                current_group = []

    if current_group:
        contiguous_groups.append(current_group)

    return list(map(len, contiguous_groups)) == sizes


with open("12.in", "r", encoding="utf-8") as f:
    condition_records = [line.split() for line in f.read().splitlines()]

p1_total_arrangements, p2_total_arrangements = 0, 0
for springs, contiguous_sizes in condition_records:
    p1_contiguous_sizes = list(map(int, contiguous_sizes.split(",")))
    p1_total_arrangements += sum(
        is_solution(s, p1_contiguous_sizes) for s in generate_combinations(springs)
    )

    # p2_contiguous_sizes = list(map(int, (contiguous_sizes * 5).split(",")))
    # p2_springs = "?".join(springs * 5)
    # p2_total_arrangements += sum(
    #     is_solution(s, p2_contiguous_sizes)
    #     for s in generate_combinations(p2_springs, sum(p2_contiguous_sizes))
    # )

print(p1_total_arrangements, p2_total_arrangements)
