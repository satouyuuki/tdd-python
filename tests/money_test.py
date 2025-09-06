import unittest
import sys
sys.path.append('..')
from money.franc import Franc
from money.money import Money

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Money = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Money.doller(5).__eq__(Money.doller(5)))
        self.assertFalse(Money.doller(5).__eq__(Money.doller(6)))
        self.assertTrue(Money.franc(5).__eq__(Money.franc(5)))
        self.assertFalse(Money.franc(5).__eq__(Money.franc(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.doller(5)))

    def testFrancMultiplication(self):
        five: Franc = Franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))
