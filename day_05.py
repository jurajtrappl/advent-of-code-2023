import os
from intervaltree import IntervalTree

with open("05.in", "r", encoding="utf-8") as f:
    sections = f.read().strip().split(f"{os.linesep}{os.linesep}")
    raw_seeds, raw_maps = sections[0].split()[1:], [
        m.split(os.linesep)[1:] for m in sections[1:]
    ]
    seeds, maps = [int(seed) for seed in raw_seeds], [
        [[int(x) for x in row.split()] for row in m] for m in raw_maps
    ]

p1_values = seeds
p2_values = [
    (seed_start, seed_start + range_length)
    for seed_start, range_length in zip(seeds[::2], seeds[1::2])
]
for m in maps:
    tree = IntervalTree()
    for destination_start, source_start, range_length in m:
        tree.addi(
            source_start,
            source_start + range_length,
            (destination_start, destination_start + range_length),
        )

    p1_new_values = []
    for seed in p1_values:
        if not (interval := list(tree[seed])):
            p1_new_values.append(seed)
            continue

        p1_new_values.append(interval[0].data[0] + (seed - interval[0].begin))

    p2_new_values = []
    for start, end in p2_values:
        if not (intervals := list(tree[start:end])):
            p2_new_values.append((start, end))
            continue

        current_start = start
        for interval in sorted(intervals):
            if current_start < interval.begin:
                p2_new_values.append((start, interval.begin))

            overlapping_start = max(current_start, interval.begin)
            overlapping_end = min(end, interval.end)
            p2_new_values.append(
                (
                    interval.data[0] + overlapping_start - interval.begin,
                    interval.data[0] - interval.begin + overlapping_end,
                )
            )

            current_start = interval.end

        if current_start < end:
            p2_new_values.append((current_start, end))

    p1_values, p2_values = p1_new_values, p2_new_values

print(min(p1_values))
print(min(x[0] for x in p2_values))
