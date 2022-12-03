if __name__ == '__main__':

    from math import sqrt
    from time import monotonic

    iterations = 1000000
    start = monotonic()
    for a in range(iterations):
        x = sqrt(4)
    print('sqrt time: {:>.3f}'.format(monotonic() - start) + ' seconds')
    start = monotonic()
    for a in range(iterations):
        x = 4 ** 0.5
    print('** time: {:>.3f}'.format(monotonic() - start) + ' seconds')
    start = monotonic()
    for a in range(iterations):
        x = pow(4, 0.5)
    print('pow time: {:>.3f}'.format(monotonic() - start) + ' seconds')

