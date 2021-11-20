import os


def part1():
    d = {'(': 1, ')': -1}
    print('day1', os.getcwd())
    with open('../../inputs/input01') as file:
        input_string = file.read()
        floor = 0
        for c in input_string:
            if c in d:
                floor += d[c]
        return floor

    #         print(f'Part 1: {floor}')


def part2():
    d = {'(': 1, ')': -1}
    with open('../../inputs/input01') as file:
        input_string = file.read()
        floor = 0
        for i, c in enumerate(input_string):
            if c in d:
                floor += d[c]
            if floor == -1:
                #                 print(f'Part 2: {i + 1}')
                return i + 1
