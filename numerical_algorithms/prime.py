import math as m
import prng


class prime:

    def find_factors(self, number):
        '''
        Finds the prime factors of a number
        '''
        factors = []
        while number % 2 == 0:
            factors.append(2)
            number /= 2
        i = 3
        max_factor = m.sqrt(number)
        while i <= max_factor:
            while number % i == 0:
                factors.append(i)
                number /= i
                max_factor = m.sqrt(number)
            i += 2
        if number > 1:
            factors.append(round(number))
        return factors

    def is_prob_prime(self, p, max_tests):
        '''
        Test if p is prime
        0.5^max_tests probabilty of giving false positive
        Making use of Fermats little theorem
        '''
        for i in range(max_tests):
            sampler = prng.prng(minimum=1, maximum=p)
            n = sampler.sample()
            if n**(p-1) % p is not 1:
                return False
        return True
