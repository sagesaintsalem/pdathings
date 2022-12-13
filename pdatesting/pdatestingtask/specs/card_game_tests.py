import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("hearts", 6)
        self.cards = [self.card1, self.card2, Card("diamonds", 7)]

    def test_for_ace(self):
        card1 = self.card1
        testValue = True
        shouldBeTrue = CardGame.check_for_ace(self, card1)
        self.assertEqual(testValue, shouldBeTrue)

    
    def test_highest(self):
        card1 = self.card1
        card2 = self.card2
        comparison = CardGame.highest_card(self, card1, card2)
        self.assertEqual(card2, comparison)        

    
    def test_total(self):
        cards = self.cards
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 14", result)

