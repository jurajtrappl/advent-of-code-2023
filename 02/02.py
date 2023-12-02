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
possible_games_ids = set(id for id, _ in games)   # part 1
power = 0                                           # part 2

for id, record in games:
    fewest_cubes_bag = {"red": 0, "green": 0, "blue": 0}
    for r in record:
        record_bag = {
            color: int(count)
            for count, color in (cube.split() for cube in r.split(","))
        }
        if any(bag[color] - record_bag.get(color, 0) < 0 for color in bag):
            possible_games_ids.discard(id)

        fewest_cubes_bag = {
            color: max(fewest_cubes_bag[color], record_bag.get(color, 0)) for color in bag
        }

    power += fewest_cubes_bag["red"] * fewest_cubes_bag["green"] * fewest_cubes_bag["blue"]

print(sum(possible_games_ids))
print(power)
