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


class TestFourOfAKind(TestCase):
    def setUp(self):
        self.four_of_a_kind_hand: list = [Card(rank=Ranks.FIVE.value, suit=Suits.DIAMONDS.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.SPADES.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value),
                                          Card(rank=Ranks.THREE.value, suit=Suits.HEARTS.value)]

        self.invalid_four_of_a_kind_hand: list = [Card(rank=Ranks.FIVE.value, suit=Suits.DIAMONDS.value),
                                                  Card(rank=Ranks.FIVE.value, suit=Suits.SPADES.value),
                                                  Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                                  Card(rank=Ranks.THREE.value, suit=Suits.CLUBS.value),
                                                  Card(rank=Ranks.THREE.value, suit=Suits.HEARTS.value)]

        self.hand_strength = CardStrength(self.four_of_a_kind_hand)

        self.invalid_four_of_kind_hand_strength = CardStrength(self.invalid_four_of_a_kind_hand)

    def test_is_four_of_kind_returns_true_for_valid_four_of_a_kind_hand(self):
        self.assertTrue(self.hand_strength.is_four_of_a_kind())

    def test_is_four_of_kind_returns_false_for_invalid_four_of_a_kind_hand(self):
        self.assertFalse(self.invalid_four_of_kind_hand_strength.is_four_of_a_kind())


class TestFullHouse(TestCase):
    def setUp(self):
        self.full_house_hand: list = [Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                      Card(rank=Ranks.K.value, suit=Suits.DIAMONDS.value),
                                      Card(rank=Ranks.K.value, suit=Suits.SPADES.value),
                                      Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                      Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value)]

        self.not_full_house_hand: list = [Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                          Card(rank=Ranks.K.value, suit=Suits.DIAMONDS.value),
                                          Card(rank=Ranks.SEVEN.value, suit=Suits.SPADES.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value)]

        self.hand_strength = CardStrength(self.full_house_hand)

        self.not_valid_full_house_hand = CardStrength(self.not_full_house_hand)

    def test_is_full_house_returns_true_for_valid_full_house_hand(self):
        self.assertTrue(self.hand_strength.is_full_house())

    def test_not_is_full_house_returns_true_for_valid_full_house_hand(self):
        self.assertFalse(self.not_valid_full_house_hand.is_full_house())


class TestFlush(TestCase):

    def setUp(self):
        self.flush_hand: list = [Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                 Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                 Card(rank=Ranks.TWO.value, suit=Suits.HEARTS.value),
                                 Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                 Card(rank=Ranks.FOUR.value, suit=Suits.HEARTS.value)]

        self.not_flush_hand: list = [Card(rank=Ranks.A.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.J.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.TEN.value, suit=Suits.HEARTS.value)]

        self.hand_strength = CardStrength(self.flush_hand)

        self.not_valid_flush_hand_strength = CardStrength(self.not_flush_hand)

    def test_is_flush_returns_true_for_valid_flush_hand(self):
        self.assertTrue(self.hand_strength.is_flush())

    def test_is_flush_returns_false_for_invalid_flush_hand(self):
        self.assertFalse(self.not_valid_flush_hand_strength.is_flush())