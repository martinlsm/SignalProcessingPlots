import os
import math
import numpy as np

def __fill_array__(array_to, array_from):
    for s in array_from:
        s = s.split(', ')
        abs, angle = float(s[0]), 2 * math.pi * float(s[1])
        array_to.append(complex(abs * math.cos(angle), abs * math.sin(angle)))
        if math.sin(angle) != 0:
            array_to.append(complex(abs * math.cos(angle), - abs * math.sin(angle)))

def pad_shortest(list1, list2):
    if len(list1) < len(list2):
        shortest = list1
        longest = list2
    else:
        shortest = list2
        longest = list1
    while len(shortest) < len(longest):
        shortest.append(0)

class PolesAndZeros:

    def __init__(self, filename):
        self.filename = filename
        self.zeros = []
        self.poles = []
        self.update()

    def update(self):
        with open(self.filename, mode='r') as file:
            lines = file.read().splitlines()
            split_index = lines.index('zeros')
            __fill_array__(self.poles, lines[1:split_index])
            __fill_array__(self.zeros, lines[split_index + 1:])
            pad_shortest(self.poles, self.zeros)


if __name__ == '__main__':
    poz = PolesAndZeros('poles_and_zeros.txt')
    poz.update()
