"""
--- Day 7: Camel Cards ---
"""
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

p1_camel_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
p2_camel_cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
type_frequencies = {
    "FIVE_OF_A_KIND": (5,),
    "FOUR_OF_A_KIND": (4, 1),
    "FULL_HOUSE": (3, 2),
    "THREE_OF_A_KIND": (3, 1, 1),
    "TWO_PAIR": (2, 2, 1),
    "ONE_PAIR": (2, 1, 1, 1),
    "HIGH_CARD": (1, 1, 1, 1, 1),
}

def cards_to_relative_strength(cards: List[str], hand: str) -> List[int]:
    return [cards.index(card_on_hand) for card_on_hand in hand]

def total_winnings(types: Dict[Tuple[int, ...], List[int]]) -> int:
    hand_counter, total = 1, 0
    for hands in reversed(types.values()):
        ranked_hands = sorted(hands, key=lambda x: x[0])
        for _, bid in ranked_hands:
            total += hand_counter * bid
            hand_counter += 1

    return total

with open("07.in", "r", encoding="utf-8") as f:
    hands_with_bids = [line.split() for line in f.read().strip().splitlines()]

p1, p2 = defaultdict(list), defaultdict(list)
for hand, str_bid in hands_with_bids:
    hand_counts = tuple(f[1] for f in Counter(hand).most_common())
    p1[hand_counts].append(
        (cards_to_relative_strength(p1_camel_cards, hand), int(str_bid))
    )

    hand_without_joker = Counter(hand.replace("J", "")).most_common()
    if not hand_without_joker:
        p2[type_frequencies["FIVE_OF_A_KIND"]].append(
            (cards_to_relative_strength(p2_camel_cards, hand), int(str_bid))
        )
        continue

    most_frequent_card_without_joker = hand_without_joker[0][0]
    joker_hand = hand.replace("J", most_frequent_card_without_joker)
    joker_hand_counts = tuple(f[1] for f in Counter(joker_hand).most_common())
    p2[joker_hand_counts].append(
        (cards_to_relative_strength(p2_camel_cards, hand), int(str_bid))
    )

print(total_winnings(p1), total_winnings(p2))
