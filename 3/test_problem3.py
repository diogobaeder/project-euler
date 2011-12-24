from unittest import TestCase

from nose.tools import istest

from problem3 import Problem3


class Problem3Test(TestCase):
    @istest
    def largest_prime_from_1_is_1(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(1), 1)

    @istest
    def largest_prime_from_2_is_2(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(2), 2)

    @istest
    def largest_prime_from_3_is_3(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(3), 3)

    @istest
    def largest_prime_from_4_is_2(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(4), 2)

    @istest
    def largest_prime_from_5_is_5(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(5), 5)

    @istest
    def largest_prime_from_6_is_3(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(6), 3)

    @istest
    def largest_prime_from_8_is_2(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(8), 2)

    @istest
    def largest_prime_from_29_is_29(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(29), 29)

    @istest
    def largest_prime_from_13195_is_29(self):
        problem3 = Problem3()
        self.assertEqual(problem3.largest_prime_from(13195), 29)

    @istest
    def detects_1_as_prime(self):
        problem3 = Problem3()
        self.assertTrue(problem3.is_prime(1))

    @istest
    def detects_2_as_prime(self):
        problem3 = Problem3()
        self.assertTrue(problem3.is_prime(2))

    @istest
    def detects_3_as_prime(self):
        problem3 = Problem3()
        self.assertTrue(problem3.is_prime(3))

    @istest
    def detects_4_not_as_prime(self):
        problem3 = Problem3()
        self.assertFalse(problem3.is_prime(4))

    @istest
    def detects_5_as_prime(self):
        problem3 = Problem3()
        self.assertTrue(problem3.is_prime(5))

    @istest
    def detects_6_not_as_prime(self):
        problem3 = Problem3()
        self.assertFalse(problem3.is_prime(6))

    @istest
    def detects_6857_as_prime(self):
        problem3 = Problem3()
        self.assertTrue(problem3.is_prime(6857))
