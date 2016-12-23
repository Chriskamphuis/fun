def exp(a, p):
    '''
    float a to the power int p
    Makes use of the following facts:
        A^(2*M) = (A^M)^2
        A^(M + N) = A^M * A^N
    '''
    binary = '{0:b}'.format(p)[::-1]
    n = a
    power = [a]
    while n <= p:
        power.append(power[-1] * power[-1])
        n *= a
    result = 1
    for i in range(len(binary)):
        if binary[i] is '1':
            result *= power[i]

    return result
