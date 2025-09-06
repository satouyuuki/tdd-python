import unittest
from money import Doller

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Doller = Doller(5)
        product: Doller = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def testEquality(self):
        self.assertTrue(Doller(5).equals(Doller(5)))

