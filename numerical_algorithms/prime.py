import math as m


class prime:

    def find_factors(self, number):
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
