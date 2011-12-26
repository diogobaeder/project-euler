#!/usr/bin/env python
from operator import add


class Problem6(object):
    def difference_of(self, number):
        squared_sum_elements = []
        squared_elements = []
        for element in range(1, number + 1):
            squared_sum_elements.append(element)
            squared_elements.append(element ** 2)
        squared_sum = reduce(add, squared_sum_elements) ** 2
        sum_of_squares = reduce(add, squared_elements)
        return squared_sum - sum_of_squares

if __name__ == '__main__':
    problem6 = Problem6()
    print problem6.difference_of(100) # == 25164150