from enum import Enum


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


class Suits(Enum):
    CLUBS = 'C'
    HEARTS = 'H'
    SPADES = 'S'
    DIAMONDS = 'D'


class HandsName(Enum):

    ROYAL_FLUSH = 'ROYAL FLUSH'
    STRAIGHT_FLUSH = 'STRAIGHT FLUSH'
    FOUR_OF_A_KIND = 'FOUR OF A KIND'
    FULL_HOUSE = 'FULL HOUSE'
    FLUSH = 'FLUSH'
    STRAIGHT = 'STRAIGHT'
    THREE_OF_A_KIND = 'THREE OF A KIND'
    TWO_OF_A_KIND = 'TWO OF A KIND'
    ONE_OF_A_PAIR = 'ONE OF A PAIR'
    HIGH_CARD = 'HIGH CARD'


LOWEST_CARD_RANK: int = 2

HIGHEST_CARD_RANK: int = 14
