import os
import sys


class prng:

    def __init__(self, seed=int.from_bytes(os.urandom(4), sys.byteorder),
                 minimum=0, maximum=2**31):
        '''
        A, B and M as suggested by the ISO/IEC 9899
        '''
        self.A = 1103515245
        self.B = 12345
        self.M = 2**31
        self.minimum = minimum
        self.maximum = maximum
        self.last = seed
        self.gen = self.generator()

    def generator(self):
        while True:
            self.last = (self.A * self.last + self.B) % self.M
            yield round(self.minimum + float(self.last)/(self.M) *
                        (self.maximum - self.minimum))

    def sample(self):
        return next(self.gen)

    def randomize_list(self, lis):
        '''
        Randomizes an array, so it can be used more easy for some sorting
        algorithms.
        '''
        max_i = len(lis)
        for i in range(max_i - 1):
            self.last = (self.A * self.last + self.B) % self.M
            j = round(i + float(self.last)/(self.M) * (max_i - 1 - i))
            lis[i], lis[j] = lis[j], lis[i]
        return lis
