class Card(object):

    def __init__(self, rank):
        self.validate_rank(rank)
        self.rank = rank

    @staticmethod
    def validate_rank(rank):
        if 2 <= rank <= 14:
            return True
        raise Exception

    suit = 'Diamonds'
