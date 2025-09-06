import unittest

class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        Doller five = Doller(5)
        five.times(2)
        self.assertEqual(10, five.amount)
        
