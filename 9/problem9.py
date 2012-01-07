#!/usr/bin/env python
'''
a2 + b2 = c2
a + b + c = 1000
a + b + (V a2 + b2) = 1000
'''
import math


class Problem9(object):
    def sum_triplet_for(self, a, b):
        return a + b + math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    problem9 = Problem9()

    for a in range(1, 1000):
        for b in range(a + 1, 1001):
            if problem9.sum_triplet_for(a, b) == 1000:
                print a, b # == 200 375