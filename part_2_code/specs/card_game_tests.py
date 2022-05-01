import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 5)
        self.card2 = Card  ("Spades", 10)

        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(False, result)

    def test_check_highest_card(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(10, result)

    def test_cards_total(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 15", result)