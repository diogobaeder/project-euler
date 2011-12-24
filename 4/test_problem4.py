from unittest import TestCase

from nose.tools import istest

from problem4 import Problem4


class Problem4Test(TestCase):
    @istest
    def detects_9009_as_palindromic_number(self):
        problem4 = Problem4()
        self.assertTrue(problem4.is_palindromic(9009))

    @istest
    def detects_9119_as_palindromic_number(self):
        problem4 = Problem4()
        self.assertTrue(problem4.is_palindromic(9119))

    @istest
    def detects_9120_as_non_palindromic_number(self):
        problem4 = Problem4()
        self.assertFalse(problem4.is_palindromic(9120))

    @istest
    def detects_9191_as_non_palindromic_number(self):
        problem4 = Problem4()
        self.assertFalse(problem4.is_palindromic(9191))

    @istest
    def detects_9229_as_palindromic_number(self):
        problem4 = Problem4()
        self.assertTrue(problem4.is_palindromic(9229))

    @istest
    def detects_92129_as_palindromic_number(self):
        problem4 = Problem4()
        self.assertTrue(problem4.is_palindromic(92129))

    @istest
    def breaks_9009_into_90_and_09(self):
        problem4 = Problem4()
        self.assertEqual(problem4.break_into_halves(9009), ('90', '09'))

    @istest
    def breaks_9119_into_91_and_19(self):
        problem4 = Problem4()
        self.assertEqual(problem4.break_into_halves(9119), ('91', '19'))

    @istest
    def breaks_91319_into_91_and_19(self):
        problem4 = Problem4()
        self.assertEqual(problem4.break_into_halves(91319), ('91', '19'))

    @istest
    def minimum_multiplication_result_with_3_digit_numbers_is_10000(self):
        self.assertEqual(100 * 100, 10000)

    @istest
    def maximum_multiplication_result_with_3_digit_numbers_is_998001(self):
        self.assertEqual(999 * 999, 998001)