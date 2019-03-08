from unittest import TestCase
from enum import Enum

from card import Card


class Ranks(Enum):
    A = 14
    K = 13
    Q = 12
    J = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


class TestCard(TestCase):

    def test_card_has_rank_attribute(self):
        card: Card = Card()
        self.assertTrue(hasattr(card, 'rank'))

    def test_card_has_suit_attribute(self):
        card: Card = Card()
        self.assertTrue(hasattr(card, 'suit'))

    def test_card_rank_attribute_only_holds_valid_values(self):
        card: Card = Card(rank=14)
        self.assertTrue(card.rank == 14)