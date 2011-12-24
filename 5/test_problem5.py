from unittest import TestCase

from nose.tools import istest

from problem5 import Problem5


class Problem5Test(TestCase):
    @istest
    def gets_minimum_evenly_divisible_by_range_to_4_as_24(self):
        problem5 = Problem5()
        self.assertEqual(problem5.minimum_evenly_divisible(4), 12)

    @istest
    def gets_minimum_evenly_divisible_by_range_to_5_as_120(self):
        problem5 = Problem5()
        self.assertEqual(problem5.minimum_evenly_divisible(5), 60)

    @istest
    def gets_minimum_evenly_divisible_by_range_to_6_as_120(self):
        problem5 = Problem5()
        self.assertEqual(problem5.minimum_evenly_divisible(6), 60)

    @istest
    def gets_minimum_evenly_divisible_by_range_to_7_as_840(self):
        problem5 = Problem5()
        self.assertEqual(problem5.minimum_evenly_divisible(7), 420)

    @istest
    def gets_minimum_evenly_divisible_by_range_to_10_as_2520(self):
        problem5 = Problem5()
        self.assertEqual(problem5.minimum_evenly_divisible(10), 2520)

    @istest
    def decomposes_3_into_counted_factors(self):
        problem5 = Problem5()
        self.assertEqual(problem5.decompose_counted_factors(3), {3: 1})

    @istest
    def decomposes_5_into_counted_factors(self):
        problem5 = Problem5()
        self.assertEqual(problem5.decompose_counted_factors(5), {5: 1})

    @istest
    def decomposes_4_into_counted_factors(self):
        problem5 = Problem5()
        self.assertEqual(problem5.decompose_counted_factors(4), {2: 2})

    @istest
    def decomposes_6_into_counted_factors(self):
        problem5 = Problem5()
        self.assertEqual(problem5.decompose_counted_factors(6), {2: 1, 3: 1})

    @istest
    def decomposes_12_into_counted_factors(self):
        problem5 = Problem5()
        self.assertEqual(problem5.decompose_counted_factors(12), {2: 2, 3: 1})

    @istest
    def finds_united_factors_between_12_and_30(self):
        problem5 = Problem5()
        self.assertEqual(problem5.united_factors(12, 30), {2: 2, 3: 1, 5: 1})

    @istest
    def finds_united_factors_between_2_and_3(self):
        problem5 = Problem5()
        self.assertEqual(problem5.united_factors(2, 3), {2: 1, 3: 1})

    @istest
    def finds_united_factors_between_2_and_3_and_5(self):
        problem5 = Problem5()
        self.assertEqual(problem5.united_factors(2, 3, 5), {2: 1, 3: 1, 5: 1})
