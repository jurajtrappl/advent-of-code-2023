from typing import Dict
import regex as re


def parse_record(raw_record: str) -> Dict[str, int]:
    return {
        color: int(count) for count, color in re.findall(r"(\d+)\s+(\w+)", raw_record)
    }


with open("02.in", "r", encoding="utf-8") as f:
    games_records = [
        (int(id), [parse_record(record) for record in records.split(";")])
        for id, records in [
            re.match(r"Game (\d+): (.*)", line).groups()
            for line in f.read().strip().splitlines()
        ]
    ]

bag = {"red": 12, "green": 13, "blue": 14}
possible_games_ids = set(game_id for game_id, _ in games_records)
power = 0
for game_id, records_bags in games_records:
    max_cubes_bag = {
        color: max(record_bag.get(color, 0) for record_bag in records_bags)
        for color in bag
    }

    if any(bag[color] - max_cubes_bag[color] < 0 for color in bag):
        possible_games_ids.discard(game_id)

    power += max_cubes_bag["red"] * max_cubes_bag["green"] * max_cubes_bag["blue"]

print(sum(possible_games_ids))
print(power)
