from unittest import TestCase
from card import Card
from constants import Ranks, Suits
from card_strength import CardStrength


class TestRoyalFlush(TestCase):

    def setUp(self):
        suit = Suits.DIAMONDS.value
        self.royal_flush_hand: list = [Card(rank=Ranks.J.value, suit=suit),
                                       Card(rank=Ranks.K.value, suit=suit),
                                       Card(rank=Ranks.Q.value, suit=suit),
                                       Card(rank=Ranks.A.value, suit=suit),
                                       Card(rank=Ranks.TEN.value, suit=suit)]

        self.hand_strength = CardStrength(self.royal_flush_hand)

        self.not_royal_flush_hand: list = [Card(rank=Ranks.J.value, suit=Suits.SPADES.value),
                                           Card(rank=Ranks.K.value, suit=suit),
                                           Card(rank=Ranks.Q.value, suit=suit),
                                           Card(rank=Ranks.A.value, suit=suit),
                                           Card(rank=Ranks.TEN.value, suit=suit)]

        self.failing_hand_strength = CardStrength(self.not_royal_flush_hand)

    def test_is_royal_flush_returns_true_for_royal_flush(self):
        self.assertTrue(self.hand_strength.is_royal_flush())

    def test_is_royal_flush_returns_false_for_not_royal_flush(self):
        self.assertFalse(self.failing_hand_strength.is_royal_flush())


class TestStraightFlush(TestCase):

    def setUp(self):
        suit = Suits.DIAMONDS.value
        self.straight_flush_hand: list = [Card(rank=Ranks.TEN.value, suit=suit),
                                          Card(rank=Ranks.NINE.value, suit=suit),
                                          Card(rank=Ranks.EIGHT.value, suit=suit),
                                          Card(rank=Ranks.SEVEN.value, suit=suit),
                                          Card(rank=Ranks.SIX.value, suit=suit)]

        self.royal_flush_hand: list = [Card(rank=Ranks.J.value, suit=suit),
                                       Card(rank=Ranks.K.value, suit=suit),
                                       Card(rank=Ranks.Q.value, suit=suit),
                                       Card(rank=Ranks.A.value, suit=suit),
                                       Card(rank=Ranks.TEN.value, suit=suit)]

        self.not_valid_straight_hand: list = [Card(rank=Ranks.TEN.value, suit=suit),
                                              Card(rank=Ranks.TWO.value, suit=suit),
                                              Card(rank=Ranks.SIX.value, suit=suit),
                                              Card(rank=Ranks.A.value, suit=suit),
                                              Card(rank=Ranks.FOUR.value, suit=suit)]

        self.hand_strength = CardStrength(self.straight_flush_hand)

        self.royal_hand_strength = CardStrength(self.royal_flush_hand)

        self.not_valid_straight_hand_strength = CardStrength(self.not_valid_straight_hand)

    def test_straight_flush_returns_true_when_valid_hand_is_provided(self):
        self.assertTrue(self.hand_strength.is_straight_flush())

    def test_straight_flush_returns_false_a_unbeatable_royal_flush_is_provided(self):
        self.assertFalse(self.royal_hand_strength.is_straight_flush())

    def test_straight_flush_returns_false_on_hand_that_not_valid_for_straight_hand(self):
        self.assertFalse(self.not_valid_straight_hand_strength.is_straight_flush())
