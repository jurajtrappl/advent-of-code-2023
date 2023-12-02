import regex as re

with open("01.in", "r") as f:
    input = f.read().strip()

def solve(digits):
    return sum(int(digits[candidates[0]] + digits[candidates[-1]]) for candidates in [re.findall(r"|".join(digits), l, overlapped=True) for l in input.splitlines()])

print(solve({str(d): str(d) for d in range(1, 10)})) # 1-9
print(solve({str(d): str(d) for d in range(1, 10)} | {d: str(i+1) for i, d in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])})) # + digits using letters