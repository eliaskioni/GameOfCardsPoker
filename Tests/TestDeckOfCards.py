from unittest import TestCase
from deck_of_cards import DeckOfCards


class TestDeckOfCards(TestCase):

    def test_deck_of_cards_has_52_cards(self):
        deck_of_cards: DeckOfCards = DeckOfCards()
        self.assertTrue(len(deck_of_cards.cards) == 52)