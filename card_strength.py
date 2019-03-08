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

    def cards_of_the_same_rank(self, number_of_cards):
        counter = Counter()
        ranks = CardStrength.get_ranks_in_hand(self.cards)
        if not len(set(ranks)) == 2:
            return False
        for rank in ranks:
            counter[rank] += 1
        groups_of_ranks = list(set(ranks))
        if counter.get(groups_of_ranks[0]) == number_of_cards:
            return True
        if counter.get(groups_of_ranks[1]) == number_of_cards:
            return True
        return False

    def is_four_of_a_kind(self):
        return self.cards_of_the_same_rank(4)

    def is_full_house(self):
        return self.cards_of_the_same_rank(3) and self.cards_of_the_same_rank(2)
