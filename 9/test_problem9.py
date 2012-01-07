from unittest import TestCase

from nose.tools import istest

from problem9 import Problem9


class Problem9Test(TestCase):
    @istest
    def sums_triplet_for_3_and_4_as_12(self):
        problem9 = Problem9()

        self.assertEqual(problem9.sum_triplet_for(3, 4), 12)