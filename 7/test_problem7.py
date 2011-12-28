from unittest import TestCase

from nose.tools import istest

from problem7 import Problem7


class Problem7Test(TestCase):
    @istest
    def identifies_prime_1_as_2(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(1), 2)

    @istest
    def identifies_prime_2_as_3(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(2), 3)

    @istest
    def identifies_prime_3_as_5(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(3), 5)

    @istest
    def identifies_prime_4_as_7(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(4), 7)

    @istest
    def identifies_prime_5_as_11(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(5), 11)

    @istest
    def identifies_prime_6_as_13(self):
        problem7 = Problem7()
        self.assertEqual(problem7.prime(6), 13)