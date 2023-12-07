from functools import reduce

with open("06.in", "r", encoding="utf-8") as f:
    competition_data = [
        (int(x), int(y))
        for x, y in zip(*[line.split()[1:] for line in f.read().strip().splitlines()])
    ]

p1_competition_data = competition_data
p2_competition_data = reduce(
    lambda x, y: (int(f"{x[0]}{y[0]}"), int(f"{x[1]}{y[1]}")), competition_data
)

records = []
for time, distance in p1_competition_data + [p2_competition_data]:
    distances = [(time - i) * i for i in range(time)]
    records.append(sum(distance < d for d in distances))

print(reduce(lambda x, y: x * y, records[:-1]))
print(records[-1])
