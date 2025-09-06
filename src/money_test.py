import unittest
from money import Doller

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five: Doller = Doller(5)
        self.assertEqual(Doller(10), five.times(2))
        self.assertEqual(Doller(15), five.times(3))

    def testEquality(self):
        self.assertTrue(Doller(5).equals(Doller(5)))
        self.assertFalse(Doller(5).equals(Doller(6)))

