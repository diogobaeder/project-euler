class Problem1(object):
    def sum_below(self, threshold):
        current_number = 1
        total = 0
        while current_number < threshold:
            if (current_number % 3 == 0) or (current_number % 5 == 0):
                total += current_number
            current_number += 1
        return total


if __name__ == '__main__':
    problem1 = Problem1()
    print problem1.sum_below(1000) # == 233168