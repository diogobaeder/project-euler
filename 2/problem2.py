class Problem2(object):
    def sum_till(self, till):
        pair_sum = 0

        last = 2
        last_previous = 1
        current_number = 0

        while current_number <= till:
            if last % 2 == 0:
                pair_sum += last
            current_number = last_previous + last
            last_previous = last
            last = current_number
        return pair_sum


if __name__ == '__main__':
    problem2 = Problem2()
    print problem2.sum_till(1000000) # == 1089154