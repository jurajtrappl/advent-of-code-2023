"""
--- Day 9: Mirage Maintenance ---
"""
from typing import List


def all_zero(history: List[int]) -> bool:
    return all(step == 0 for step in history)


def find_differences(history: List[int]) -> List[int]:
    return [y - x for x, y in zip(history, history[1:])]


with open("09.in", "r", encoding="utf-8") as f:
    report = [
        [int(step) for step in history.split()]
        for history in f.read().strip().splitlines()
    ]

p1_extrapolated, p2_extrapolated = 0, 0
for history in report:
    sequences_of_differences = [find_differences(history)]
    while not all_zero(sequences_of_differences[-1]):
        sequences_of_differences.append(find_differences(sequences_of_differences[-1]))

    predicted_next, predicted_before = [0], [0]
    for seq in reversed([history] + sequences_of_differences[:-1]):
        predicted_next.append(seq[-1] + predicted_next[-1])
        predicted_before.append(seq[0] - predicted_before[-1])

    p1_extrapolated += predicted_next[-1]
    p2_extrapolated += predicted_before[-1]

print(p1_extrapolated, p2_extrapolated)
