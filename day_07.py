from collections import Counter

with open("test.in", "r", encoding="utf-8") as f:
    hands_with_bids = [line.split() for line in f.read().strip().splitlines()]

camel_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
types = {
    t: []
    for t in [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
}

for hand, bid in hands_with_bids:
    freq = tuple([f[1] for f in Counter(hand).most_common()])
    types[freq].append(([camel_cards.index(card) for card in hand], int(bid)))

hand_counter, total = 1, 0
for t, hands in reversed(types.items()):
    ranked_hands = sorted(hands, key=lambda x: x[0])
    for hand, bid in ranked_hands:
        total += hand_counter * bid
        hand_counter += 1
