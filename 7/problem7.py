#!/usr/bin/env python
from math import sqrt


class Problem7(object):
    def prime(self, element):
        prime_counter = 0
        number_to_test = 1

        while prime_counter < element:
            number_to_test += 1
            if self.is_prime(number_to_test):
                prime_counter += 1
        return number_to_test

    def is_prime(self, number):
        for possible_divider in xrange(2, int(sqrt(number)) + 1):
            if number % possible_divider == 0:
                return False
        return True

if __name__ == '__main__':
    problem7 = Problem7()
    print problem7.prime(10001) # == 104743