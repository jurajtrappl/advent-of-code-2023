import regex as re

with open("01.in", "r") as f:
    input = f.read().strip()

digits_vocabulary = {str(d): str(d) for d in range(1, 10)}
letter_digits_vocabulary = {d: str(i + 1) for i, d in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]) }

def solve(vocabulary):
    return sum(
        int(vocabulary[digit[0]] + vocabulary[digit[-1]])
        for digit in [
            re.findall(r"|".join(vocabulary), line, overlapped=True)
            for line in input.splitlines()
        ]
    )

print(solve(digits_vocabulary))
print(solve(digits_vocabulary | letter_digits_vocabulary))