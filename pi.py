#!/usr/bin/env python3

# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

def calc(n):
    # use loop to calculate pi
    pi = 0
    sign = 1
    for i in range(1, n, 2):
        pi += sign * 4 / i
        sign *= -1
    return pi

# pi = round(pi, 3)
# print(pi)

max = 100000000000000000000
counter = 1

while counter <= max:
    pi = calc(counter)
    print(f'{counter:21}: {pi}')
    counter *= 10


