import requests

def load_file():
    try:
        response = requests.get('https://aoc-trox667.vercel.app/inputs/input01')
        if response.status_code == 200:
            return response.text
    except Exception:
        return ''
    return ''

def part1():
    d = {'(': 1, ')': -1}
    input_string = load_file()
    floor = 0
    for c in input_string:
        if c in d:
            floor += d[c]
    return floor

    #         print(f'Part 1: {floor}')


def part2():
    d = {'(': 1, ')': -1}
    input_string = load_file()
    floor = 0
    for i, c in enumerate(input_string):
        if c in d:
            floor += d[c]
        if floor == -1:
            #                 print(f'Part 2: {i + 1}')
            return i + 1
