from unittest import TestCase

from nose.tools import istest

from problem1 import problem1


class Problem1Test(TestCase):
    @istest
    def sum_below_10_is_23(self):
        self.assertEqual(problem1.sum_below(10), 23)