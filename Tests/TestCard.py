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
        card: Card = Card(rank=Ranks.A.value)
        self.assertTrue(hasattr(card, 'rank'))

    def test_card_has_suit_attribute(self):
        card: Card = Card(rank=Ranks.A.value)
        self.assertTrue(hasattr(card, 'suit'))

    def test_card_rank_attribute_holds_valid_values(self):
        card: Card = Card(rank=Ranks.A.value)
        self.assertTrue(card.rank == 14)

        card: Card = Card(rank=Ranks.K.value)
        self.assertTrue(card.rank == 13)

        card: Card = Card(rank=Ranks.Q.value)
        self.assertTrue(card.rank == 12)

        card: Card = Card(rank=Ranks.J.value)
        self.assertTrue(card.rank == 11)

        card: Card = Card(rank=Ranks.TEN.value)
        self.assertTrue(card.rank == 10)

        card: Card = Card(rank=Ranks.NINE.value)
        self.assertTrue(card.rank == 9)

        card: Card = Card(rank=Ranks.EIGHT.value)
        self.assertTrue(card.rank == 8)

        card: Card = Card(rank=Ranks.SEVEN.value)
        self.assertTrue(card.rank == 7)

        card: Card = Card(rank=Ranks.SIX.value)
        self.assertTrue(card.rank == 6)

        card: Card = Card(rank=Ranks.FIVE.value)
        self.assertTrue(card.rank == 5)

        card: Card = Card(rank=Ranks.FOUR.value)
        self.assertTrue(card.rank == 4)

        card: Card = Card(rank=Ranks.THREE.value)
        self.assertTrue(card.rank == 3)

        card: Card = Card(rank=Ranks.TWO.value)
        self.assertTrue(card.rank == 2)

    def test_card_rank_attribute_throws_exception_on_invalid_values(self):
        with self.assertRaises(Exception):
            Card(rank=15)
            Card(rank=None)
            Card(rank=1)
            Card()