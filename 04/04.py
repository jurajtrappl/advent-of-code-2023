with open("04.in", "r") as f:
    scratch_cards = [(winning.split()[2:], scratched.split()) for winning, scratched in [line.split("|") for line in f.read().strip().splitlines()]]

N = len(scratch_cards)
matching_numbers = {}
copies = {card_number: 1 for card_number in range(1, N + 1)}
for card_number, (winning_numbers, scratch_numbers) in enumerate(scratch_cards, start=1):
    matching_numbers[card_number] = sum([num in scratch_numbers for num in winning_numbers])

    card_copies = list(range(card_number + 1, min(card_number + matching_numbers[card_number], N) + 1))
    for card_copy in card_copies:
        copies[card_copy] += copies[card_number]

print(sum(2 ** (x - 1) if x else 0 for x in matching_numbers.values()))
print(sum(copies.values()))