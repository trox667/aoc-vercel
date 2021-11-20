import requests
import os
from dotenv import load_dotenv


def is_debug():
    load_dotenv()
    DEBUG = os.getenv('AOC_DEBUG')
    print('AOC_DEBUG', DEBUG)
    return DEBUG is not None


def load_file():
    if is_debug():
        try:
            print('using local file')
            file = open('public/inputs/input01')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input01')
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
