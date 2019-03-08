class Card(object):

    def __init__(self, rank, suit):
        self.validate_rank(rank)
        self.validate_suit(suit)
        self.rank = rank
        self.suit = suit

    @staticmethod
    def validate_rank(rank):
        if 2 <= rank <= 14:
            return True
        raise Exception

    @staticmethod
    def validate_suit(suit):
        if suit in ['C', 'S', 'H', 'D']:
            return True
        raise Exception
