from constants import Ranks


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
    def cards_in_sequence(cards):
        card_ranks = [card.rank for card in cards]
        expected_ranks = list(range(cards[0].rank, cards[4].rank - 1, -1))
        return card_ranks == expected_ranks

    def is_royal_flush(self):
        cards = self.order_cards_starting_from_highest_rank_to_lowest_rank()
        if not self.is_same_suit(cards):
            return False
        if not self.cards_in_sequence(cards):
            return False
        ranks = [card.rank for card in cards]
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
