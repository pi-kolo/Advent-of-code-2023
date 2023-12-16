from collections import Counter
from enum import Enum
from functools import cmp_to_key


CARDS_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10} | {
    str(x): x for x in range(2, 10)
}


CARDS_VALUES_JOKER = {"A": 13, "K": 12, "Q": 11, "T": 10, "J": 1} | {
    str(x): x for x in range(2, 10)
}


class Hand(Enum):
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


def parse_input(filename):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            hand, bid = line.split()
            bid = int(bid)
            data.append((hand, bid))
        return data


def get_hand_rank(hand, with_joker=False):
    if with_joker:
        cards_occurences = [
            el[1] for el in Counter(hand).most_common(5) if el[0] != "J"
        ]
        # case of 5 Jokers
        if len(cards_occurences) == 0:
            cards_occurences = [5]
        else:
            cards_occurences[0] += hand.count("J")
    else:
        cards_occurences = [el[1] for el in Counter(hand).most_common(5)]

    hand_type = None
    if cards_occurences[0] == 5:
        hand_type = Hand.FIVE
    elif cards_occurences[0] == 4:
        hand_type = Hand.FOUR
    elif cards_occurences[0] == 3 and cards_occurences[1] == 2:
        hand_type = Hand.FULL_HOUSE
    elif cards_occurences[0] == 3 and cards_occurences[1] == 1:
        hand_type = Hand.THREE
    elif cards_occurences[0] == 2 and cards_occurences[1] == 2:
        hand_type = Hand.TWO_PAIRS
    elif cards_occurences[0] == 2 and cards_occurences[1] == 1:
        hand_type = Hand.ONE_PAIR
    else:
        hand_type = Hand.HIGH_CARD

    return (hand_type, hand)


def compare_hands(hand1, hand2, with_joker=False):
    rank1 = get_hand_rank(hand1, with_joker)
    rank2 = get_hand_rank(hand2, with_joker)

    if rank1[0] != rank2[0]:
        return rank1[0].value - rank2[0].value

    cards_mapping = CARDS_VALUES_JOKER if with_joker else CARDS_VALUES
    for i in range(5):
        if rank1[1][i] != rank2[1][i]:
            return cards_mapping[rank1[1][i]] - cards_mapping[rank2[1][i]]


def count_total_winning(hands_list, with_joker=False):
    sorted_by_ranks = sorted(
        hands_list, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0], with_joker))
    )
    return sum(el[1] * i for i, el in enumerate(sorted_by_ranks, 1))


hands_list = parse_input("input.txt")

# part 1
print(count_total_winning(hands_list))

# part 2: with Jokers
print(count_total_winning(hands_list, True))
