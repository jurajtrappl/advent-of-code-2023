with open("04.in", "r", encoding="utf-8") as f:
    scratch_cards = [
        (winning.split()[2:], scratched.split())
        for winning, scratched in [
            line.split("|") for line in f.read().strip().splitlines()
        ]
    ]

N = len(scratch_cards)
matching_numbers, copies = {}, {card_number: 1 for card_number in range(1, N + 1)}
for card_number, (winning_numbers, scratch_numbers) in enumerate(
    scratch_cards, start=1
):
    matching_numbers[card_number] = sum(
        [num in scratch_numbers for num in winning_numbers]
    )

    for card_copy in range(
        card_number + 1, card_number + matching_numbers[card_number] + 1
    ):
        copies[card_copy] += copies[card_number]

print(sum(int(2 ** (x - 1)) for x in matching_numbers.values()))
print(sum(copies.values()))
