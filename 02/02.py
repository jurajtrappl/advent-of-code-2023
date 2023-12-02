import regex as re


def parse_record(record):
    cubes = re.findall(r"(\d+)\s+(\w+)", record)
    return {color: int(count) for count, color in cubes}


with open("02.in", "r") as f:
    games = [
        (int(id), [parse_record(record) for record in records.split(";")])
        for id, records in [
            re.match(r"Game (\d+): (.*)", line).groups()
            for line in f.read().strip().splitlines()
        ]
    ]

bag = {"red": 12, "green": 13, "blue": 14}
possible_games_ids = set(id for id, _ in games)
power = 0
for id, records_bags in games:
    max_cubes_bag = {
        color: max(record_bag.get(color, 0) for record_bag in records_bags)
        for color in bag
    }

    if any(bag[color] - max_cubes_bag[color] < 0 for color in bag):
        possible_games_ids.discard(id)

    power += max_cubes_bag["red"] * max_cubes_bag["green"] * max_cubes_bag["blue"]

print(sum(possible_games_ids))
print(power)
