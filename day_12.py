"""
--- Day 12: Hot Springs ---
"""
from typing import List

from tqdm import tqdm

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"

memo = {}


def count_arrangements(springs: str, sizes: List[int]) -> int:
    sizes_hashable = ",".join(map(str, sizes))
    if res := memo.get((springs, sizes_hashable), None):
        return res

    if "?" not in springs:
        memo[(springs, sizes_hashable)] = is_solution(springs, sizes)
        return memo[(springs, sizes_hashable)]

    question_i = springs.index("?")
    arrangements_with_dot = count_arrangements(
        springs[:question_i] + "." + springs[question_i + 1 :], sizes
    )
    arrangements_with_hashtag = count_arrangements(
        springs[:question_i] + "#" + springs[question_i + 1 :], sizes
    )
    memo[(springs, sizes_hashable)] = arrangements_with_dot + arrangements_with_hashtag
    return arrangements_with_dot + arrangements_with_hashtag


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
for springs, contiguous_sizes in tqdm(condition_records):
    p1_contiguous_sizes = list(map(int, contiguous_sizes.split(",")))
    p1_total_arrangements += count_arrangements(springs, contiguous_sizes)

    p2_contiguous_sizes = list(map(int, (contiguous_sizes * 5).split(",")))
    p2_springs = "?".join(springs * 5)
    p2_total_arrangements += count_arrangements(p2_springs, p2_contiguous_sizes)

print(p1_total_arrangements, p2_total_arrangements)
