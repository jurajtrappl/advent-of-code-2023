from functools import reduce
import regex as re

with open("02.in", "r") as f:
    games = [
        (int(id), record.split(";"))
        for id, record in [
            re.match(r"Game (\d+): (.*)", line).groups()
            for line in f.read().strip().splitlines()
        ]
    ]

bag = {"red": 12, "green": 13, "blue": 14}
possible_games_ids = set([id for id, _ in games])
min_set_cubes = 0

for id, record in games:
    max_bag = {"red": 0, "green": 0, "blue": 0}
    for r in record:
        record_bag = {
            color: int(count)
            for count, color in (cube.split() for cube in r.split(","))
        }
        if any(bag[color] - record_bag.get(color, 0) < 0 for color in bag):
            possible_games_ids.discard(id)

        max_bag = {
            color: max(max_bag[color], record_bag.get(color, 0)) for color in bag.keys()
        }

    min_set_cubes += reduce(lambda x, y: x * y, max_bag.values())

print(sum(possible_games_ids))
print(min_set_cubes)
