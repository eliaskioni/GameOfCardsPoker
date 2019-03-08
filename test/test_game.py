from unittest import TestCase
from constants import Suits, LOWEST_CARD_RANK, HIGHEST_CARD_RANK
from card import Card
from typing import List
from game import Game
from random import shuffle


class TestGame(TestCase):

    def setUp(self):
        deck: List[Card] = []
        for suit in [Suits.CLUBS.value,
                     Suits.HEARTS.value,
                     Suits.SPADES.value,
                     Suits.DIAMONDS.value]:
            for rank in range(LOWEST_CARD_RANK, HIGHEST_CARD_RANK + 1):
                card: Card = Card(rank=rank, suit=suit)
                deck.append(card)
        self.deck = deck
        self.assertEqual(len(self.deck), 52)

    @staticmethod
    def get_rank_and_suit_in_string_form(card: Card):
        return str(card.rank) + card.suit

    def test_game_plays(self):
        deck = self.deck
        shuffle(deck)
        hands: List[Card] = [deck[i:i + 5] for i in range(0, len(deck), 5)]
        for hand in hands:
            cards: List[Card] = [card for card in hand]
            if len(cards) == 5:
                raw_hand = "{} {} {} {} {}".format(
                    self.get_rank_and_suit_in_string_form(cards[0]),
                    self.get_rank_and_suit_in_string_form(cards[1]),
                    self.get_rank_and_suit_in_string_form(cards[2]),
                    self.get_rank_and_suit_in_string_form(cards[3]),
                    self.get_rank_and_suit_in_string_form(cards[4])
                )
                Game(raw_hand)
