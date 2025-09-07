import unittest
import sys
sys.path.append('..')
from money.money import Money

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Money = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Money.doller(5) == (Money.doller(5)))
        self.assertFalse(Money.doller(5) == (Money.doller(6)))
        self.assertFalse(Money.franc(5) == (Money.doller(5)))

    def testCurrency(self):
        self.assertEqual("USD", Money.doller(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())
