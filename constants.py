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