#!/usr/bin/env python3

def calc(n):
    pi = 3
    a = -1
    for i in range(2, n, 2):
        a = -a
        pi +=  a * (4 / (i * (i + 1) * (i + 2)))
    return pi


for i in range(50):
    counter = (10 ** i) + 1
    pi = calc(counter)
    print(f'{counter:50}: {pi:.100f}')

# copilot didnt write this one ;p
