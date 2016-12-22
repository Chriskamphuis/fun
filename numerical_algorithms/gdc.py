def gdc(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
