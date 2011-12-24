class Problem3(object):
    def largest_prime_from(self, which):
        counter = 1
        last_prime = 1
        remaining = which
        while counter <= remaining // 1:
            if self.is_prime(counter) and remaining % counter == 0:
                last_prime = counter
                remaining = remaining // counter
            counter += 1
        return last_prime

    def is_prime(self, number):
        counter = 2
        while counter <= number // 2:
            if number % counter == 0:
                return False
            counter += 1
        return True


if __name__ == '__main__':
    problem3 = Problem3()
    print problem3.largest_prime_from(600851475143) # == 6857
