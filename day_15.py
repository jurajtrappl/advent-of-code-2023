"""
--- Day 15: Lens Library ---
"""


def hashing_algorithm(s: str) -> int:
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        _, remainder = divmod(current_value, 256)
        current_value = remainder

    return current_value


assert hashing_algorithm("HASH") == 52

test_init_sequence_hash = sum(
    map(
        hashing_algorithm,
        "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(","),
    )
)
assert test_init_sequence_hash == 1320

with open("15.in", "r", encoding="utf-8") as f:
    init_sequence = f.read().strip()

p1_hash = sum(map(hashing_algorithm, init_sequence.split(",")))

print(p1_hash)
