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
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))
        self.assertFalse(Franc(5).__eq__(Money.doller(5)))

    def testFrancMultiplication(self):
        five: Franc = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))
