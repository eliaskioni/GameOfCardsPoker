from unittest import TestCase
from card import Card
from constants import Ranks, Suits
from hand_strength import HandStrength
from hand import Hand


class TestRoyalFlush(TestCase):

    def setUp(self):
        suit = Suits.DIAMONDS.value
        self.royal_flush_hand: Hand = Hand(Card(rank=Ranks.J.value, suit=suit),
                                           Card(rank=Ranks.K.value, suit=suit),
                                           Card(rank=Ranks.Q.value, suit=suit),
                                           Card(rank=Ranks.A.value, suit=suit),
                                           Card(rank=Ranks.TEN.value, suit=suit))

        self.hand_strength = HandStrength(self.royal_flush_hand)

        self.not_royal_flush_hand: Hand = Hand(Card(rank=Ranks.J.value, suit=Suits.SPADES.value),
                                               Card(rank=Ranks.K.value, suit=suit),
                                               Card(rank=Ranks.Q.value, suit=suit),
                                               Card(rank=Ranks.A.value, suit=suit),
                                               Card(rank=Ranks.TEN.value, suit=suit))

        self.failing_hand_strength = HandStrength(self.not_royal_flush_hand)

    def test_is_royal_flush_returns_true_for_royal_flush(self):
        self.assertTrue(self.hand_strength.is_royal_flush())

    def test_is_royal_flush_returns_false_for_not_royal_flush(self):
        self.assertFalse(self.failing_hand_strength.is_royal_flush())


class TestStraightFlush(TestCase):

    def setUp(self):
        suit = Suits.DIAMONDS.value
        self.straight_flush_hand: Hand = Hand(Card(rank=Ranks.TEN.value, suit=suit),
                                              Card(rank=Ranks.NINE.value, suit=suit),
                                              Card(rank=Ranks.EIGHT.value, suit=suit),
                                              Card(rank=Ranks.SEVEN.value, suit=suit),
                                              Card(rank=Ranks.SIX.value, suit=suit))

        self.royal_flush_hand: Hand = Hand(Card(rank=Ranks.J.value, suit=suit),
                                           Card(rank=Ranks.K.value, suit=suit),
                                           Card(rank=Ranks.Q.value, suit=suit),
                                           Card(rank=Ranks.A.value, suit=suit),
                                           Card(rank=Ranks.TEN.value, suit=suit))

        self.not_valid_straight_hand: Hand = Hand(Card(rank=Ranks.TEN.value, suit=suit),
                                                  Card(rank=Ranks.TWO.value, suit=suit),
                                                  Card(rank=Ranks.SIX.value, suit=suit),
                                                  Card(rank=Ranks.A.value, suit=suit),
                                                  Card(rank=Ranks.FOUR.value, suit=suit))

        self.hand_strength = HandStrength(self.straight_flush_hand)

        self.royal_hand_strength = HandStrength(self.royal_flush_hand)

        self.not_valid_straight_hand_strength = HandStrength(self.not_valid_straight_hand)

    def test_straight_flush_returns_true_when_valid_hand_is_provided(self):
        self.assertTrue(self.hand_strength.is_straight_flush())

    def test_straight_flush_returns_false_a_unbeatable_royal_flush_is_provided(self):
        self.assertFalse(self.royal_hand_strength.is_straight_flush())

    def test_straight_flush_returns_false_on_hand_that_not_valid_for_straight_hand(self):
        self.assertFalse(self.not_valid_straight_hand_strength.is_straight_flush())


class TestFourOfAKind(TestCase):
    def setUp(self):
        self.four_of_a_kind_hand: Hand = Hand(Card(rank=Ranks.FIVE.value, suit=Suits.DIAMONDS.value),
                                              Card(rank=Ranks.FIVE.value, suit=Suits.SPADES.value),
                                              Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                              Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value),
                                              Card(rank=Ranks.THREE.value, suit=Suits.HEARTS.value))

        self.invalid_four_of_a_kind_hand: Hand = Hand(Card(rank=Ranks.FIVE.value, suit=Suits.DIAMONDS.value),
                                                      Card(rank=Ranks.FIVE.value, suit=Suits.SPADES.value),
                                                      Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                                      Card(rank=Ranks.THREE.value, suit=Suits.CLUBS.value),
                                                      Card(rank=Ranks.THREE.value, suit=Suits.HEARTS.value))

        self.hand_strength = HandStrength(self.four_of_a_kind_hand)

        self.invalid_four_of_kind_hand_strength = HandStrength(self.invalid_four_of_a_kind_hand)

    def test_is_four_of_kind_returns_true_for_valid_four_of_a_kind_hand(self):
        self.assertTrue(self.hand_strength.is_four_of_a_kind())

    def test_is_four_of_kind_returns_false_for_invalid_four_of_a_kind_hand(self):
        self.assertFalse(self.invalid_four_of_kind_hand_strength.is_four_of_a_kind())


class TestFullHouse(TestCase):
    def setUp(self):
        self.full_house_hand: Hand = Hand(Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                          Card(rank=Ranks.K.value, suit=Suits.DIAMONDS.value),
                                          Card(rank=Ranks.K.value, suit=Suits.SPADES.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                          Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value))

        self.not_full_house_hand: Hand = Hand(Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                              Card(rank=Ranks.K.value, suit=Suits.DIAMONDS.value),
                                              Card(rank=Ranks.SEVEN.value, suit=Suits.SPADES.value),
                                              Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                              Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value))

        self.hand_strength = HandStrength(self.full_house_hand)

        self.not_valid_full_house_hand = HandStrength(self.not_full_house_hand)

    def test_is_full_house_returns_true_for_valid_full_house_hand(self):
        self.assertTrue(self.hand_strength.is_full_house())

    def test_not_is_full_house_returns_true_for_valid_full_house_hand(self):
        self.assertFalse(self.not_valid_full_house_hand.is_full_house())


class TestFlush(TestCase):

    def setUp(self):
        self.flush_hand: Hand = Hand(Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.TWO.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.FIVE.value, suit=Suits.HEARTS.value),
                                     Card(rank=Ranks.FOUR.value, suit=Suits.HEARTS.value))

        self.not_flush_hand: Hand = Hand(Card(rank=Ranks.A.value, suit=Suits.HEARTS.value),
                                         Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                         Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                         Card(rank=Ranks.J.value, suit=Suits.HEARTS.value),
                                         Card(rank=Ranks.TEN.value, suit=Suits.HEARTS.value))

        self.hand_strength = HandStrength(self.flush_hand)

        self.not_valid_flush_hand_strength = HandStrength(self.not_flush_hand)

    def test_is_flush_returns_true_for_valid_flush_hand(self):
        self.assertTrue(self.hand_strength.is_flush())

    def test_is_flush_returns_false_for_invalid_flush_hand(self):
        self.assertFalse(self.not_valid_flush_hand_strength.is_flush())


class TestStraightHand(TestCase):

    def setUp(self):
        self.straight_hand: Hand = Hand(Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                        Card(rank=Ranks.J.value, suit=Suits.DIAMONDS.value),
                                        Card(rank=Ranks.TEN.value, suit=Suits.CLUBS.value),
                                        Card(rank=Ranks.NINE.value, suit=Suits.SPADES.value),
                                        Card(rank=Ranks.EIGHT.value, suit=Suits.HEARTS.value))

        self.not_straight_hand: Hand = Hand(Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.J.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.TEN.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.EIGHT.value, suit=Suits.HEARTS.value))

        self.hand_strength = HandStrength(self.straight_hand)

        self.not_valid_straight_hand_strength = HandStrength(self.not_straight_hand)

    def test_is_straight_returns_true_for_valid_flush_hand(self):
        self.assertTrue(self.hand_strength.is_straight())

    def test_is_straight_returns_false_for_valid_flush_hand(self):
        self.assertFalse(self.not_valid_straight_hand_strength.is_straight())


class TestThreeOfAKind(TestCase):

    def setUp(self):
        self.three_of_a_kind_hand: Hand = Hand(Card(rank=Ranks.Q.value, suit=Suits.SPADES.value),
                                               Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                               Card(rank=Ranks.Q.value, suit=Suits.DIAMONDS.value),
                                               Card(rank=Ranks.FIVE.value, suit=Suits.SPADES.value),
                                               Card(rank=Ranks.NINE.value, suit=Suits.CLUBS.value))

        self.not_three_of_a_kind_hand: Hand = Hand(Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                                   Card(rank=Ranks.J.value, suit=Suits.HEARTS.value),
                                                   Card(rank=Ranks.TEN.value, suit=Suits.HEARTS.value),
                                                   Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                                                   Card(rank=Ranks.EIGHT.value, suit=Suits.HEARTS.value))

        self.hand_strength = HandStrength(self.three_of_a_kind_hand)

        self.not_valid_three_of_a_kind_hand_strength = HandStrength(self.not_three_of_a_kind_hand)

    def test_is_three_of_a_kind_returns_true_for_valid_three_of_a_kind_hand(self):
        self.assertTrue(self.hand_strength.is_three_of_a_kind())


class TestTwoPair(TestCase):

    def setUp(self):
        self.two_pair_hand: Hand = Hand(Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                        Card(rank=Ranks.K.value, suit=Suits.SPADES.value),
                                        Card(rank=Ranks.J.value, suit=Suits.CLUBS.value),
                                        Card(rank=Ranks.J.value, suit=Suits.DIAMONDS.value),
                                        Card(rank=Ranks.NINE.value, suit=Suits.DIAMONDS.value))

        self.not_two_pair_hand: Hand = Hand(Card(rank=Ranks.Q.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.J.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.TEN.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.EIGHT.value, suit=Suits.HEARTS.value))

        self.hand_strength = HandStrength(self.two_pair_hand)

        self.not_valid_two_pair_hand_strength = HandStrength(self.not_two_pair_hand)

    def test_is_two_pair_returns_true_for_valid_two_pair_hand(self):
        self.assertTrue(self.hand_strength.is_two_pair())

    def test_is_two_pair_returns_false_for_invalid_two_pair_hand(self):
        self.assertFalse(self.not_valid_two_pair_hand_strength.is_two_pair())


class TestOnePair(TestCase):

    def setUp(self):
        self.one_pair_hand: Hand = Hand(Card(rank=Ranks.A.value, suit=Suits.CLUBS.value),
                                        Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                                        Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                                        Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value),
                                        Card(rank=Ranks.FOUR.value, suit=Suits.DIAMONDS.value))

        self.not_one_pair_hand: Hand = Hand(Card(rank=Ranks.K.value, suit=Suits.HEARTS.value),
                                            Card(rank=Ranks.K.value, suit=Suits.SPADES.value),
                                            Card(rank=Ranks.J.value, suit=Suits.CLUBS.value),
                                            Card(rank=Ranks.J.value, suit=Suits.DIAMONDS.value),
                                            Card(rank=Ranks.NINE.value, suit=Suits.DIAMONDS.value))

        self.hand_strength = HandStrength(self.one_pair_hand)

        self.not_valid_one_pair_hand_strength = HandStrength(self.not_one_pair_hand)

    def test_is_one_pair_returns_true_for_valid_one_pair_hand(self):
        self.assertTrue(self.hand_strength.is_one_pair())

    def test_is_one_pair_returns_false_for_invalid_one_pair_hand(self):
        self.assertFalse(self.not_valid_one_pair_hand_strength.is_one_pair())


class TestHighCard(TestCase):

    def setUp(self):
        self.high_card_hand: Hand = Hand(Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                                         Card(rank=Ranks.SEVEN.value, suit=Suits.HEARTS.value),
                                         Card(rank=Ranks.FIVE.value, suit=Suits.CLUBS.value),
                                         Card(rank=Ranks.THREE.value, suit=Suits.DIAMONDS.value),
                                         Card(rank=Ranks.TWO.value, suit=Suits.SPADES.value))

        self.not_high_card_hand: Hand = Hand(Card(rank=Ranks.A.value, suit=Suits.CLUBS.value),
                                             Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                                             Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                                             Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value),
                                             Card(rank=Ranks.FOUR.value, suit=Suits.DIAMONDS.value))

        self.hand_strength = HandStrength(self.high_card_hand)

        self.not_valid_one_pair_hand_strength = HandStrength(self.not_high_card_hand)

    def test_is_high_hand_returns_true_for_valid_high_card_hand(self):
        self.assertTrue(self.hand_strength.is_high_card())

    def test_is_high_hand_returns_false_for_invalid_high_card_hand(self):
        self.assertFalse(self.not_valid_one_pair_hand_strength.is_high_card())
