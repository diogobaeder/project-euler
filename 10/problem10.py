#!/usr/bin/env python
'''
Note: runs hugely faster in PyPy! Check out these results in my machine:

$ time 10/problem10.py
142913828922

real	0m33.280s
user	0m33.248s
sys	0m0.007s

$ time pypy 10/problem10.py
142913828922

real	0m2.561s
user	0m2.303s
sys	0m0.013s
'''
import math


class Problem10(object):
    def is_prime(self, number):
        counter = 2
        square = math.sqrt(number)
        while counter <= square:
            if number % counter == 0:
                return False
            counter += 1
        return True

    def sum_primes_below(self, number):
        summed = 0
        for current in range(2, number):
            if self.is_prime(current):
                summed += current
        return summed


if __name__ == '__main__':
    problem10 = Problem10()

    print problem10.sum_primes_below(2*1000*1000) # == 142913828922