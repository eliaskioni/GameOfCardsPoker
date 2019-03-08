from constants import Ranks
from collections import Counter


class CardStrength(object):

    def __init__(self, cards: list):
        self.cards = cards

    @staticmethod
    def is_same_suit(cards):
        suits = [card.suit for card in cards]
        return len(set(suits)) == 1

    def order_cards_starting_from_highest_rank_to_lowest_rank(self):
        cards = self.cards
        cards.sort(key=lambda card: card.rank)
        cards.reverse()
        return cards

    @staticmethod
    def get_ranks_in_hand(cards):
        return [card.rank for card in cards]

    @staticmethod
    def get_suits_in_hands(cards):
        return [card.suit for card in cards]

    @staticmethod
    def cards_in_sequence(cards):
        card_ranks = CardStrength.get_ranks_in_hand(cards)
        expected_ranks = list(range(cards[0].rank, cards[4].rank - 1, -1))
        return card_ranks == expected_ranks

    def is_royal_flush(self):
        cards = self.order_cards_starting_from_highest_rank_to_lowest_rank()
        if not self.is_same_suit(cards):
            return False
        if not self.cards_in_sequence(cards):
            return False
        ranks = CardStrength.get_ranks_in_hand(cards)
        expected_ranks = [Ranks.A.value, Ranks.K.value, Ranks.Q.value, Ranks.J.value, Ranks.TEN.value]
        return expected_ranks == ranks

    def is_straight_flush(self):
        cards = self.order_cards_starting_from_highest_rank_to_lowest_rank()
        if not self.is_same_suit(cards):
            return False
        if not self.cards_in_sequence(cards):
            return False
        if self.is_royal_flush():
            return False
        return True

    @staticmethod
    def group_ranks_based_on_rank(ranks):
        counter = Counter()
        for rank in ranks:
            counter[rank] += 1
        return counter

    def cards_of_the_same_rank(self, number_of_cards, groups=2):
        ranks = CardStrength.get_ranks_in_hand(self.cards)
        if not len(set(ranks)) == groups:
            return False
        grouped_ranks = CardStrength.group_ranks_based_on_rank(ranks)
        return number_of_cards in grouped_ranks.values()

    def cards_of_the_same_suit(self, number_of_suits):
        counter = Counter()
        suits = CardStrength.get_suits_in_hands(self.cards)
        for suit in suits:
            counter[suit] += 1
        return number_of_suits in counter.values()

    def is_four_of_a_kind(self):
        return self.cards_of_the_same_rank(4)

    def is_full_house(self):
        return self.cards_of_the_same_rank(3) and self.cards_of_the_same_rank(2)

    def is_flush(self):
        if self.cards_in_sequence(self.cards):
            return False
        return self.is_same_suit(self.cards)

    def is_straight(self):
        if not self.cards_in_sequence(self.cards):
            return False
        return self.cards_of_the_same_suit(2)

    def is_three_of_a_kind(self):
        return self.cards_of_the_same_rank(number_of_cards=3, groups=3)

    def is_two_pair(self):
        if not self.cards_of_the_same_rank(number_of_cards=2, groups=3):
            return False
        ranks = CardStrength.get_ranks_in_hand(self.cards)
        grouped_ranks = CardStrength.group_ranks_based_on_rank(ranks)
        if not min(grouped_ranks.values()) == 1:
            return False
        if not list(grouped_ranks.values()).count(1) == 1:
            return False

        return list(grouped_ranks.values()).count(2) == 2

    def is_one_pair(self):
        if not self.cards_of_the_same_rank(number_of_cards=2, groups=4):
            return False
        ranks = CardStrength.get_ranks_in_hand(self.cards)
        grouped_ranks = CardStrength.group_ranks_based_on_rank(ranks)
        return list(grouped_ranks.values()).count(1) == 3

    def is_high_card(self):
        return self.cards_of_the_same_rank(number_of_cards=1, groups=5)
