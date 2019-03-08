from unittest import TestCase
from hand import Hand
from constants import Ranks, Suits
from card import Card


class TestHandOfCards(TestCase):

    def test_hand_accepts_five_hands(self):
        hand = Hand(Card(rank=Ranks.A.value, suit=Suits.CLUBS.value),
                    Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                    Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                    Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value),
                    Card(rank=Ranks.FOUR.value, suit=Suits.DIAMONDS.value))

        self.assertEqual(len(hand.cards), 5)

    def test_hand_throws_exemption_when_less_than_five_cards_are_provided_for_a_hand(self):
        with self.assertRaises(TypeError):
            Hand(Card(rank=Ranks.A.value, suit=Suits.CLUBS.value),
                 Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                 Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                 Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value))

    def test_hand_raises_exemption_when_more_than_five_cards_are_provided_for_a_hand(self):
        with self.assertRaises(TypeError):
            Hand(Card(rank=Ranks.A.value, suit=Suits.CLUBS.value),
                 Card(rank=Ranks.A.value, suit=Suits.DIAMONDS.value),
                 Card(rank=Ranks.NINE.value, suit=Suits.HEARTS.value),
                 Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value),
                 Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value),
                 Card(rank=Ranks.SIX.value, suit=Suits.SPADES.value))
