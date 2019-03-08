from typing import List
from card import Card


class Hand(object):

    def __init__(self, first_card: Card, second_card: Card, third_card: Card, fourth_card: Card, fifth_card: Card):
        self.cards: List[Card] = [first_card, second_card, third_card, fourth_card, fifth_card]
        if len(self.cards) > 5:
            raise TypeError('Expected Five cards but received {}'.format(len(self.cards)))
