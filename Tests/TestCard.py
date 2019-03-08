from unittest import TestCase

from card import Card


class TestCard(TestCase):

    def test_card_has_rank_attribute(self):
        card : Card = Card()
        self.assertTrue(hasattr(card, 'rank'))

    def test_card_has_suit_attribute(self):
        card : Card = Card()
        self.assertTrue(hasattr(card, 'suit'))
