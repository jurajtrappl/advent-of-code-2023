"""
--- Day 2: Cube Conundrum ---
"""
from typing import Dict
import regex as re

BAG = {"red": 12, "green": 13, "blue": 14}


def elf_used_more_cubes(used_cubes_bag: Dict[str, int]) -> bool:
    return any(BAG[color] - used_cubes_bag[color] < 0 for color in BAG)


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

possible_games_ids = set(game_id for game_id, _ in games_records)
power = 0
for game_id, records_bags in games_records:
    max_cubes_bag = {
        color: max(record_bag.get(color, 0) for record_bag in records_bags)
        for color in BAG
    }

    if elf_used_more_cubes(max_cubes_bag):
        possible_games_ids.discard(game_id)

    power += max_cubes_bag["red"] * max_cubes_bag["green"] * max_cubes_bag["blue"]

print(sum(possible_games_ids), power)
