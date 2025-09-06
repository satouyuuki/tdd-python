import unittest
import sys
sys.path.append('..')
from money.doller import Doller
from money.franc import Franc

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Doller = Doller(5)
        self.assertEqual(Doller(10), five.times(2))
        self.assertEqual(Doller(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Doller(5).__eq__(Doller(5)))
        self.assertFalse(Doller(5).__eq__(Doller(6)))
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))
        self.assertFalse(Franc(5).__eq__(Doller(5)))

    def testFrancMultiplication(self):
        five: Franc = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))
