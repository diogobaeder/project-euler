from unittest import TestCase

from nose.tools import istest

from problem10 import Problem10


class Problem10Test(TestCase):
    @istest
    def sums_primes_below_4_as_5(self):
        problem10 = Problem10()

        self.assertEqual(problem10.sum_primes_below(4), 5)

    @istest
    def sums_primes_below_5_as_5(self):
        problem10 = Problem10()

        self.assertEqual(problem10.sum_primes_below(5), 5)

    @istest
    def sums_primes_below_6_as_10(self):
        problem10 = Problem10()

        self.assertEqual(problem10.sum_primes_below(6), 10)

    @istest
    def recognizes_2_as_a_prime(self):
        problem10 = Problem10()

        self.assertTrue(problem10.is_prime(2))

    @istest
    def recognizes_3_as_a_prime(self):
        problem10 = Problem10()

        self.assertTrue(problem10.is_prime(3))

    @istest
    def recognizes_4_as_not_a_prime(self):
        problem10 = Problem10()

        self.assertFalse(problem10.is_prime(4))

    @istest
    def recognizes_29_as_a_prime(self):
        problem10 = Problem10()

        self.assertTrue(problem10.is_prime(29))
