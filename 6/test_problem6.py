from unittest import TestCase

from nose.tools import istest

from problem6 import Problem6


class Problem6Test(TestCase):
    @istest
    def gets_difference_of_1(self):
        problem6 = Problem6()
        self.assertEqual(problem6.difference_of(1), 0)

    @istest
    def gets_difference_of_2(self):
        problem6 = Problem6()
        expected = (1 + 2) ** 2 - (1 ** 2 + 2 ** 2)
        self.assertEqual(problem6.difference_of(2), expected)

    @istest
    def gets_difference_of_3(self):
        problem6 = Problem6()
        expected = (1 + 2 + 3) ** 2 - (1 ** 2 + 2 ** 2 + 3 ** 2)
        self.assertEqual(problem6.difference_of(3), expected)

    @istest
    def gets_difference_of_4(self):
        problem6 = Problem6()
        expected = (1 + 2 + 3 + 4) ** 2 - (1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
        self.assertEqual(problem6.difference_of(4), expected)

    @istest
    def gets_difference_of_10(self):
        problem6 = Problem6()
        self.assertEqual(problem6.difference_of(10), 2640)