from unittest import TestCase

from nose.tools import istest

from problem8 import Problem8


class Problem8Test(TestCase):
    @istest
    def finds_greatest_product_in_22222_as_32(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(22222), 2*2*2*2*2)

    @istest
    def finds_greatest_product_in_22223_as_48(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(22223), 2*2*2*2*3)

    @istest
    def finds_greatest_product_in_222223_as_48(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(222223), 2*2*2*2*3)

    @istest
    def finds_greatest_product_in_322222_as_48(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(322222), 3*2*2*2*2)

    @istest
    def finds_greatest_product_in_322224_as_64(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(322224), 2*2*2*2*4)

    @istest
    def finds_greatest_product_in_3222242323_as_144(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(3222242323), 4*2*3*2*3)

    @istest
    def finds_greatest_product_in_10000_as_0(self):
        problem8 = Problem8()

        self.assertEqual(problem8.greatest_product_in(10000), 1*0*0*0*0)