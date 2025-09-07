import unittest
from typing import cast
import sys
sys.path.append('..')
from money.money import Money
from money.expression import Expression
from money.bank import Bank
from money.sum import Sum

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

    def testSimpleAddition(self):
        five: Money = Money.doller(5)
        sum: Expression = five.plus(five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(10), reduced);

    def testPlusReturnsSum(self):
        five: Money = Money.doller(5)
        result: Expression = five.plus(five)
        sum: Sum = cast(Sum, result)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def testReduceSum(self):
        sum: Expression = Sum(Money.doller(3), Money.doller(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(7), result)

    def testReduceMoney(self):
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.doller(1), "USD")
        self.assertEqual(Money.doller(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result: Money = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.doller(1), result)

    # もしかするとpythonではlist, dictをハッシュテーブルのキーに使うことができるかもしれない
    # def testArrayEquals(self):
    #     self.assertEqual(["abc"], ["abc"])

    def testIdentityTest(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))

    def testMixedAddition(self):
        fiveBucks: Expression = Money.doller(5)
        tenFrancs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result: Money = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        self.assertEqual(Money.doller(10), result)

    def testSumPlusMoney(self):
        fiveBucks: Expression = Money.doller(5)
        tenFrancs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum: Expression = Sum(fiveBucks, tenFrancs).plus(fiveBucks)
        result: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(15), result)
