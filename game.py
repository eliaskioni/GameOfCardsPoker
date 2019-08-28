from card import Card
from typing import List
from hand import Hand
from hand_strength import HandStrength
from constants import HandsName


class Game(object):

    def __init__(self, raw_hand=None):
        self.cards: List[Card] = []
        self.hand: Hand = None
        if not raw_hand:
            raw_hand = input('Enter cards to deal:   ')
        else:
            raw_hand = raw_hand
        raw_cards = raw_hand.split()
        for raw_card in raw_cards:
            length = len(raw_card)
            raw_rank = int(raw_card[0:length - 1])
            raw_suit = raw_card[length - 1:]
            self.cards.append(Card(rank=raw_rank, suit=raw_suit))
        if len(self.cards) != 5:
            print('Not valid')
        else:
            self.make_hand()
            print(self.get_hand_strength())

    def make_hand(self):
        self.hand = Hand(first_card=self.cards[0],
                         second_card=self.cards[1],
                         third_card=self.cards[2],
                         fourth_card=self.cards[3],
                         fifth_card=self.cards[4])

    def get_hand_strength(self):
        hand_strength = HandStrength(self.hand)
        if hand_strength.is_royal_flush():
            return HandsName.ROYAL_FLUSH.value
        if hand_strength.is_straight_flush():
            return HandsName.STRAIGHT_FLUSH.value
        if hand_strength.is_four_of_a_kind():
            return HandsName.FOUR_OF_A_KIND.value
        if hand_strength.is_full_house():
            return HandsName.FULL_HOUSE.value
        if hand_strength.is_flush():
            return HandsName.FLUSH.value
        if hand_strength.is_straight():
            return HandsName.STRAIGHT.value
        if hand_strength.is_three_of_a_kind():
            return HandsName.THREE_OF_A_KIND.value
        if hand_strength.is_two_pair():
            return HandsName.TWO_OF_A_KIND.value
        if hand_strength.is_one_pair():
            return HandsName.ONE_OF_A_PAIR.value
        if hand_strength.is_high_card():
            return HandsName.HIGH_CARD.value
        else:
            raise Exception('Unknown Kind')


Game()
