from constants import Ranks


class CardStrength(object):

    def __init__(self, cards: list):
        self.cards = cards

    def is_royal_flush(self):
        cards = self.cards
        cards.sort(key=lambda card: card.rank)
        cards.reverse()
        suits = [card.suit for card in cards]
        if not len(set(suits)) == 1:
            return False
        ranks = [card.rank for card in cards]
        expected_ranks = [Ranks.A.value, Ranks.K.value, Ranks.Q.value, Ranks.J.value, Ranks.TEN.value]
        return expected_ranks == ranks
