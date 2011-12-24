from unittest import TestCase

from nose.tools import istest

from problem2 import Problem2


class Problem2Test(TestCase):
    @istest
    def sums_pair_fibos_till_3_as_2(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(3), 2)

    @istest
    def sums_pair_fibos_till_5_as_2(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(5), 2)

    @istest
    def sums_pair_fibos_till_8_as_10(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(8), 10)

    @istest
    def sums_pair_fibos_till_13_as_10(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(13), 10)

    @istest
    def sums_pair_fibos_till_21_as_10(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(21), 10)

    @istest
    def sums_pair_fibos_till_34_as_44(self):
        problem2 = Problem2()
        self.assertEqual(problem2.sum_till(34), 44)
