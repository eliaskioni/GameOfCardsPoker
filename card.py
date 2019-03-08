from constants import Suits, LOWEST_CARD_RANK, HIGHEST_CARD_RANK


class Card(object):

    def __init__(self, rank, suit):
        self.validate_rank(rank)
        self.validate_suit(suit)
        self.rank = rank
        self.suit = suit

    @staticmethod
    def validate_rank(rank):
        if LOWEST_CARD_RANK <= rank <= HIGHEST_CARD_RANK:
            return True
        raise Exception

    @staticmethod
    def validate_suit(suit):
        if suit in [Suits.CLUBS.value,
                    Suits.HEARTS.value,
                    Suits.SPADES.value,
                    Suits.DIAMONDS.value]:
            return True
        raise Exception
