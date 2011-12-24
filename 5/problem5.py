#!/usr/bin/env python
class Problem5(object):
    def minimum_evenly_divisible(self, range_till):
        united_factors = self.united_factors(*range(2, range_till + 1))
        final_number = 1
        for factor, count in united_factors.iteritems():
            final_number *= (factor ** count)
        return final_number

    def decompose_counted_factors(self, number):
        remainder = number
        counted_factors = {}
        while remainder != 1:
            for i in xrange(2, remainder + 1):
                if remainder % i == 0:
                    if counted_factors.has_key(i):
                        counted_factors[i] += 1
                    else:
                        counted_factors[i] = 1
                    remainder = remainder / i
                    break
        return counted_factors

    def united_factors(self, *numbers):
        united_factors = {}
        for number in numbers:
            decompose_counted_factors = self.decompose_counted_factors(number)
            for factor, count in decompose_counted_factors.iteritems():
                if factor not in united_factors.keys() or count > united_factors[factor]:
                    united_factors[factor] = count
        return united_factors

if __name__ == '__main__':
    problem5 = Problem5()
    print problem5.minimum_evenly_divisible(20) # == 232792560