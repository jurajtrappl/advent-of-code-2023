"""
--- Day 1: Trebuchet?! ---
"""
import regex as re

with open("01.in", "r", encoding="utf-8") as f:
    calibration_document = f.read().strip().splitlines()

p1_digits = {str(d): str(d) for d in range(1, 10)}
p2_digits = p1_digits | {
    d: str(i + 1)
    for i, d in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
}


def solve(digits):
    return sum(
        int(digits[digit[0]] + digits[digit[-1]])
        for digit in [
            re.findall(r"|".join(digits), line, overlapped=True)
            for line in calibration_document
        ]
    )


print(solve(p1_digits), solve(p2_digits))
