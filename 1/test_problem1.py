from unittest import TestCase

from nose.tools import istest

from problem1 import Problem1


class Problem1Test(TestCase):
    @istest
    def sum_below_10_is_23(self):
        problem1 = Problem1()
        self.assertEqual(problem1.sum_below(10), 23)

    @istest
    def sum_below_4_is_3(self):
        problem1 = Problem1()
        self.assertEqual(problem1.sum_below(4), 3)

    @istest
    def sum_below_6_is_8(self):
        problem1 = Problem1()
        self.assertEqual(problem1.sum_below(6), 8)

    @istest
    def sum_below_5_is_3(self):
        problem1 = Problem1()
        self.assertEqual(problem1.sum_below(5), 3)