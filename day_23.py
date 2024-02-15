"""
--- Day 23: A Long Walk ---
"""
from pprint import pprint

PATH = "."
FOREST = "#"
SLOPES = ["^", ">", "v", "<"]

with open("23-test.in", "r", encoding="utf-8") as f:
    hiking_trail_map = [list(line) for line in f.read().strip().splitlines()]

pprint(hiking_trail_map)
