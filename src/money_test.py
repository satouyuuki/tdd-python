import unittest
from money import Doller

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Doller = Doller(5)
        five.times(2)
        self.assertEqual(10, five.amount)
        
