#!/usr/bin/env python
class Problem4(object):
    def is_palindromic(self, number):
        halves = self.break_into_halves(number)
        return halves[0] == halves[1][::-1]

    def break_into_halves(self, number):
        number = str(number)
        half_length = len(number) // 2
        return (number[:half_length], number[-1 * half_length:])

if __name__ == '__main__':
    problem4 = Problem4()
    current_half = 997
    while current_half >= 100:
        current_divider = 999
        number = int(str(current_half) + str(current_half)[::-1])
        while current_divider >= 100:
            if number % current_divider == 0 and len(str(number / current_divider)) == 3:
                assert problem4.is_palindromic(number)
                print number, '=> %d * %d' % (current_divider, number / current_divider)
                exit()
            current_divider -= 1
        current_half -= 1